import logging
import threading
from typing import Any, Callable, Generic, TypeVar

import boto3
import sqs_extended_client  # noqa
from pydantic import BaseModel, Field

T = TypeVar("T")

logger = logging.getLogger(__name__)


class SQSConsumerConfig(BaseModel):
    queue_url: str
    wait_time_seconds: int = Field(default=20, ge=1)


class SQSConsumer(Generic[T]):
    def __init__(
        self,
        config: SQSConsumerConfig,
        message_deserializer: Callable[[dict[str, Any]], T],
        message_processor: Callable[[T], None],
    ) -> None:
        self.config = config
        self.message_deserializer = message_deserializer
        self.message_processor = message_processor
        self.sqs = boto3.client("sqs")
        self._is_running = True
        self.lock = threading.Lock()

    def run(self) -> None:
        while self.is_running():
            try:
                response = self.sqs.receive_message(
                    QueueUrl=self.config.queue_url,
                    AttributeNames=["All"],
                    MaxNumberOfMessages=1,
                    MessageAttributeNames=["All"],
                    WaitTimeSeconds=self.config.wait_time_seconds,
                )

                if "Messages" not in response:
                    continue

                if len(response["Messages"]) == 0:
                    continue

                message = response["Messages"][0]
                deserialized = self.message_deserializer(message)
                self.message_processor(deserialized)
                self._delete_message(message["ReceiptHandle"])

            except Exception as e:
                logger.exception(e)
        logger.warning("Stopped consumer")

    def stop(self) -> None:
        logger.warning("Stopping consumer")
        with self.lock:
            self._is_running = False

    def is_running(self) -> bool:
        with self.lock:
            return self._is_running

    def _delete_message(self, receipt_handle: str) -> None:
        self.sqs.delete_message(
            QueueUrl=self.sqs_config.queue_url,
            ReceiptHandle=receipt_handle,
        )
