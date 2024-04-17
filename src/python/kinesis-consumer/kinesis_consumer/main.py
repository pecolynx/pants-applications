# Copyright 2014-2015 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Amazon Software License (the "License").
# You may not use this file except in compliance with the License.
# A copy of the License is located at
#
# http://aws.amazon.com/asl/
#
# or in the "license" file accompanying this file. This file is distributed
# on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied. See the License for the specific language governing
# permissions and limitations under the License.


import logging
import time

import amazon_kclpy
from amazon_kclpy import kcl
from amazon_kclpy.v3 import processor
from kinesis_consumer.domain.sequence_number import SequenceNumber
from kinesis_consumer.service.app_service import AppService
from kinesis_consumer.service.multiprocess_gateway import MultiprocessGateway
from lib_loggin.json_formatter import JsonFormatter
from lib_logging.custom_logger import CustomLogger

logger = logging.getLogger(__name__)


class RecordProcessor(processor.RecordProcessorBase):  # type: ignore
    """A RecordProcessor processes data from a shard in a stream. Its methods
    will be called with this pattern:

    * initialize will be called once
    * process_records will be called zero or more times
    * shutdown will be called if this MultiLangDaemon instance loses the lease to this shard,
        or the shard ends due a scaling change.
    """

    def __init__(self, app_service: AppService) -> None:
        self._SLEEP_SECONDS = 5
        self._CHECKPOINT_RETRIES = 5
        self._CHECKPOINT_FREQ_SECONDS = 60
        self._largest_sequence_numer: SequenceNumber = SequenceNumber(0, 0)
        self._last_checkpoint_time = time.time()
        self._shard_id = ""
        self._shutdown_requested = False
        self._app_service = app_service
        self._multiprocess_gateway = MultiprocessGateway()

    def initialize(self, initialize_input: amazon_kclpy.messages.InitializeInput) -> None:
        """Called once by a KCLProcess before any calls to process_records.

        :param amazon_kclpy.messages.InitializeInput initialize_input: Information about the lease
            that this record processor has been assigned.
        """
        logger.warning("_________INITIALIZE_________")
        self._shard_id = initialize_input.shard_id
        self._logger = CustomLogger(logger, extra={"shard_id": self._shard_id})
        self._logger.warning("TEST 1")
        self._logger.warning("TEST 2", extra={"ABC": "DEF"})

    def checkpoint(
        self,
        checkpointer: amazon_kclpy.kcl.Checkpointer,
        sequence_number: str,
        sub_sequence_number: int,
    ) -> None:
        """Checkpoints with retries on retryable exceptions.

        :param amazon_kclpy.kcl.Checkpointer checkpointer: the checkpointer provided to either
            process_records or shutdown
        :param str or None sequence_number: the sequence number to checkpoint at.
        :param int or None sub_sequence_number: the sub sequence number to checkpoint at.
        """
        for n in range(0, self._CHECKPOINT_RETRIES):
            try:
                checkpointer.checkpoint(sequence_number, sub_sequence_number)
                return
            except kcl.CheckpointError as e:
                if "ShutdownException" == e.value:
                    #
                    # A ShutdownException indicates that this record processor should be shutdown.
                    # This is due to some failover event, e.g. another MultiLangDaemon has taken
                    # the lease for this shard.
                    #
                    self._logger.warning("Encountered shutdown exception, skipping checkpoint")
                    return
                elif "ThrottlingException" == e.value:
                    #
                    # A ThrottlingException indicates that one of our dependencies is is over
                    #    burdened, e.g. too many dynamo writes. We will sleep temporarily to let
                    #    it recover.
                    #
                    if self._CHECKPOINT_RETRIES - 1 == n:
                        self._logger.warning(f"Failed to checkpoint after {n} attempts, giving up.")
                        return

                    self._logger.warning(
                        "Was throttled while checkpointing, "
                        + f"will attempt again in {self._SLEEP_SECONDS} seconds"
                    )
                elif "InvalidStateException" == e.value:
                    self._logger.warning(
                        "MultiLangDaemon reported an invalid state while checkpointing."
                    )
                else:  # Some other error
                    self._logger.warning(
                        f"Encountered an error while checkpointing, error was {e}."
                    )
            time.sleep(self._SLEEP_SECONDS)

    def process_record(
        self, data: str, partition_key: str, sequence_number: SequenceNumber
    ) -> None:
        """Called for each record that is passed to process_records.

        :param str data: The blob of data that was contained in the record.
        :param str partition_key: The key associated with this recod.
        :param SequenceNumberPair sequence_number_pair: The pair of the sequence number associated
            with this record
        """

        ####################################
        # Insert your processing logic here
        ####################################
        self._logger.warning(
            f"Record (Partition Key: {partition_key}, "
            + f"Sequence Number: {sequence_number.sequence_number}, "
            + f"Subsequence Number: {sequence_number.sub_sequence_number}, "
            + f"Data Size: {len(data)}"
        )
        self._app_service.process(partition_key, sequence_number, data)

    def process_records(
        self, process_records_input: amazon_kclpy.messages.ProcessRecordsInput
    ) -> None:
        """Called by a KCLProcess with a list of records to be processed and a
        checkpointer which accepts sequence numbers from the records to
        indicate where in the stream to checkpoint.

        :param amazon_kclpy.messages.ProcessRecordsInput process_records_input: the records,
            and metadata about the records.
        """
        if self._shutdown_requested:
            return
        try:
            for record in process_records_input.records:
                data = record.binary_data
                seq = int(record.sequence_number)
                sub_seq = record.sub_sequence_number
                key = record.partition_key
                current_sequence_number = SequenceNumber(seq, sub_seq)
                self.process_record(data, key, current_sequence_number)

                if self._largest_sequence_numer < current_sequence_number:
                    self._largest_sequence_numer = current_sequence_number

            #
            # Checkpoints every self._CHECKPOINT_FREQ_SECONDS seconds
            #
            if time.time() - self._last_checkpoint_time > self._CHECKPOINT_FREQ_SECONDS:
                self.checkpoint(
                    process_records_input.checkpointer,
                    str(self.largest_sequence_numer_pair.sequence_number),
                    self.largest_sequence_numer_pair.sub_sequence_number,
                )
                self._last_checkpoint_time = time.time()
        except Exception as e:
            self._logger.warning(
                "Encountered an exception while processing records. Exception was {e}\n".format(e=e)
            )

    def lease_lost(self, lease_lost_input: amazon_kclpy.messages.LeaseLostInput) -> None:
        self._logger.warning("Lease has been lost")

    def shard_ended(self, shard_ended_input: amazon_kclpy.messages.ShardEndedInput) -> None:
        self._logger.warning("Shard has ended checkpointing")
        shard_ended_input.checkpointer.checkpoint()

    def shutdown_requested(
        self, shutdown_requested_input: amazon_kclpy.messages.ShutdownRequestedInput
    ) -> None:
        self._logger.warning("Shutdown has been requested, checkpointing.")
        self._shutdown_requested = True
        time.sleep(5)
        shutdown_requested_input.checkpointer.checkpoint()


if __name__ == "__main__":
    formatter = JsonFormatter("%(asctime)s")
    log_handler = logging.StreamHandler()
    log_handler.setFormatter(formatter)
    logging.basicConfig(handlers=[log_handler], level=logging.INFO)

    logger.info("HELLO")
    logger.info("HELLO", extra={"ABC": "DEF"})

    logger1 = logging.LoggerAdapter(logger, extra={"shard_id": "shard-0001"})
    logger1.info("WORLD")
    logger1.info("WORLD", extra={"ABC": "DEF"})
    logger2 = CustomLogger(logger, extra={"shard_id": "shard-0001"})
    logger2.info("WORLD")
    logger2.info("WORLD", extra={"ABC": "DEF"})
    logger3 = CustomLogger(logger)
    logger3.info("WORLD")
    logger3.info("WORLD", extra={"ABC": "DEF"})

    kcl_process = kcl.KCLProcess(RecordProcessor(app_service=AppService(logger=logger)))
    kcl_process.run()
