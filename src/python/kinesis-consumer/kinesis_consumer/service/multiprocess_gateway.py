import multiprocessing

from kinesis_consumer.model.sequence_number import SequenceNumber
from kinesis_consumer.service.consumer import run_consumer


class MultiprocessGateway:
    def __init__(self) -> None:
        ...

    def run(self) -> None:
        multiprocessing.MultiProcess(target=run_consumer, daemon=True)

    def process_record(self, sequence_number: SequenceNumber, data: bytes) -> None:
        pass
