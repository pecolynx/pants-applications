import logging
from datetime import datetime

from pydantic import BaseModel
from typing import Any
from sqs_consumer.gateway.sqs_consumer import SQSConfig, SQSConsumer
import signal
from signal import Signals
import time

class Request(BaseModel):
    body: str
    sent_at: datetime


def message_deserializer(message: dict[str, Any]) -> Request:
    if "Body" not in message:
        raise ValueError("Body is required")
    if "Attributes" not in message:
        raise ValueError("Attributes is required")
    attributes:dict[str,str] = message["Attributes"]
    if "SentTimestamp" not in attributes:
        raise ValueError("SentTimestamp is required")

    timestamp = int(attributes["SentTimestamp"]) / 1000
    return Request(
        body=message["Body"],
        sent_at=datetime.fromtimestamp(timestamp),
    )


def message_processor(message: Request) -> None:
    print(message)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("Starting SQS Consumer")


    sqs_config = SQSConfig(
        queue_url="http://sqs.ap-northeast-1.localhost.localstack.cloud:4566/000000000000/test-queue"
    )
    sqs_consumer = SQSConsumer(
        sqs_config=sqs_config,
        message_deserializer=message_deserializer,
        message_processor=message_processor,
    )

    def handle_sigterm(signum: int, frame) -> None:
        print(type(signum))
        print(type(frame))
        logger.info(f"Got signal. {signum}, {frame}")
        sqs_consumer.stop()
        time.sleep(5)
    signal.signal(signal.SIGTERM, handle_sigterm)

    sqs_consumer.run()
