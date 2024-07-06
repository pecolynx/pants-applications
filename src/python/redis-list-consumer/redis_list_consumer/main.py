import logging
import signal
import time
from typing import Any

from lib_redis.redis_client import RedisClientConfig, RedisClientInterface, new_redis_client
from pydantic import BaseModel
from redis_list_consumer.gateway.redis_list_consumer import (
    RedisListConsumer,
    RedisListConsumerConfig,
)


class Request(BaseModel):
    body: str


def message_deserializer(message: str) -> Request:
    return Request(body=message)


def message_processor(message: Request) -> None:
    print(message)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info("Starting Redis List Consumer")

    redis: RedisClientInterface = new_redis_client(
        config=RedisClientConfig(host="localhost", port=6379, db=0, password=None)
    )
    config = RedisListConsumerConfig(list_name="MyList")
    consumer = RedisListConsumer(
        redis=redis,
        config=config,
        message_deserializer=message_deserializer,
        message_processor=message_processor,
    )

    def handle_sigterm(signum: int, frame: Any) -> None:
        print(type(signum))
        print(type(frame))
        logger.info(f"Got signal. {signum}, {frame}")
        consumer.stop()
        time.sleep(5)

    signal.signal(signal.SIGTERM, handle_sigterm)

    consumer.run()
