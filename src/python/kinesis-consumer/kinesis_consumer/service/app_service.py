import logging

from kinesis_consumer.domain.sequence_number import SequenceNumber


class AppService:
    def __init__(self, logger: logging.Logger):
        self.logger = logger

    def process(self, partition_key: str, sequence_number: SequenceNumber, message: str) -> None:
        self.logger.info(f"Processing message: {message}")
        # Process the message
        self.logger.info(f"Finished processing message: {message}")
