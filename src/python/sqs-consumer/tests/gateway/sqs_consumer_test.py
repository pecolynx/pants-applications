from typing import Any, Generator
from unittest.mock import MagicMock

import boto3
import pytest
from moto import mock_aws
from sqs_consumer.gateway.sqs_consumer import SQSConsumer, SQSConsumerConfig


@pytest.fixture  # type: ignore[misc]
def env(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("AWS_DEFAULT_REGION", "us-east-1")
    monkeypatch.setenv("AWS_ACCESS_KEY_ID", "fake_key")
    monkeypatch.setenv("AWS_SECRET_ACCESS_KEY", "fake_secret")


@pytest.fixture  # type: ignore[misc]
def sqs() -> Generator[tuple[boto3.client, str], None, None]:
    with mock_aws():
        sqs_client = boto3.client("sqs")
        resp = sqs_client.create_queue(QueueName="MyQueue")
        yield sqs_client, resp["QueueUrl"]


class TestMessageDeserializer:
    def __init__(self) -> None:
        self.message = ""

    def execute(self, message: dict[str, Any]) -> str:
        self.message = message["Body"]
        return self.message


def test_a(env, sqs) -> None:  # type: ignore[no-untyped-def]
    sqs_client, queue_url = sqs
    config = SQSConsumerConfig(queue_url=queue_url)
    deserializer = TestMessageDeserializer()
    consumer = SQSConsumer[str](
        config=config,
        message_deserializer=deserializer.execute,
        message_processor=lambda x: None,
    )
    consumer.is_running = MagicMock(side_effect=[True, False])  # type: ignore[method-assign]
    sqs_client.send_message(QueueUrl=queue_url, MessageBody="Hello")
    consumer.run()

    assert deserializer.message == "Hello"
