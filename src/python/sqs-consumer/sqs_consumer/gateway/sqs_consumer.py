import logging
import threading
import time
from typing import Any, Callable, Generic, TypeVar

import boto3
import sqs_extended_client  # noqa
from pydantic import BaseModel

T = TypeVar("T")

logger = logging.getLogger(__name__)


class SQSConfig(BaseModel):
    queue_url: str


class SQSConsumer(Generic[T]):
    def __init__(
        self,
        sqs_config: SQSConfig,
        message_deserializer: Callable[[dict[str, Any]], T],
        message_processor: Callable[[T], None],
    ) -> None:
        self.sqs_config = sqs_config
        self.message_deserializer = message_deserializer
        self.message_processor = message_processor
        self.sqs = boto3.client("sqs")
        self._is_stopped = False
        self.lock = threading.Lock()

    def run(self) -> None:
        while not self.is_stopped():
            try:
                response = self.sqs.receive_message(
                    QueueUrl=self.sqs_config.queue_url,
                    AttributeNames=["All"],
                    MaxNumberOfMessages=1,
                    MessageAttributeNames=["All"],
                    WaitTimeSeconds=20,
                )

                if "Messages" not in response:
                    time.sleep(1)
                    continue

                if len(response["Messages"]) == 0:
                    time.sleep(1)
                    continue

                message = response["Messages"][0]
                # print(type(message))
                # print(message)
                deserialized = self.message_deserializer(message)
                self.message_processor(deserialized)
                self._delete_message(message["ReceiptHandle"])

            except Exception as e:
                logger.exception(e)
        logger.warning("Stopped consumer")

    def stop(self) -> None:
        logger.warning("Stopping consumer")
        with self.lock:
            self._is_stopped = True

    def is_stopped(self) -> bool:
        with self.lock:
            return self._is_stopped

    def _delete_message(self, receipt_handle: str) -> None:
        self.sqs.delete_message(
            QueueUrl=self.sqs_config.queue_url,
            ReceiptHandle=receipt_handle,
        )
