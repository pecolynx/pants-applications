import logging
import multiprocessing
import time
from logging.handlers import QueueHandler, QueueListener

from lib_logging.json_formatter import JsonFormatter
from multiprocessing_app.worker import Worker

# from lib_logging.custom_logger import CustomLogger

logger = logging.getLogger(__name__)


def worker_process_1() -> None:
    logger = logging.getLogger("worker_process_1")
    logger.warning("worker_process")


def worker_process_2() -> None:
    logger = multiprocessing.get_logger()
    logger.warning("worker_process2")


def main() -> None:
    log_queue = multiprocessing.Queue()

    formatter = JsonFormatter("%(asctime)s")
    log_handler = logging.StreamHandler()
    log_handler.setFormatter(formatter)

    logging.basicConfig(
        handlers=[QueueHandler(log_queue)], format="%(message)s", level=logging.INFO
    )

    logger.warning("WARNING")

    log_listener = QueueListener(log_queue, log_handler)

    log_listener.start()

    multiprocessing.Process(target=worker_process_1, daemon=True).start()
    multiprocessing.Process(target=worker_process_2, daemon=True).start()

    worker1 = Worker()
    multiprocessing.Process(target=worker1.run, daemon=True).start()

    worker2 = Worker()
    multiprocessing.Process(target=worker2.run, daemon=True).start()

    time.sleep(3)
    log_listener.enqueue_sentinel()
    log_listener.stop()


if __name__ == "__main__":
    main()
