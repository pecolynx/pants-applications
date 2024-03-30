import logging

from kinesis_consumer.model.sequence_number_pair import SequenceNumberPair


class AppService:
    def __init__(self, logger: logging.Logger):
        self.logger = logger

    def process(
        self, partition_key: str, sequence_number_pair: SequenceNumberPair, message: str
    ) -> None:
        self.logger.info(f"Processing message: {message}")
        # Process the message
        self.logger.info(f"Finished processing message: {message}")
