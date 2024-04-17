import logging

from lib_logging.custom_logger import CustomLogger

logger = logging.getLogger(__name__)


class Worker:
    def __init__(self) -> None:
        self._logger = CustomLogger(logger, extra={"shard_id": "XXX"})

    def run(self) -> None:
        logger.info("worker run", extra={"a": "b"})
        self._logger.info("worker run", extra={"x": "y"})
