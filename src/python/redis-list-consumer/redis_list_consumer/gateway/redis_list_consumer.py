import logging
import threading
from typing import Callable, Generic, TypeVar

from lib_redis.redis_client import RedisClientInterface
from pydantic import BaseModel, Field

T = TypeVar("T")

logger = logging.getLogger(__name__)


class RedisListConsumerConfig(BaseModel):
    list_name: str
    wait_time_seconds: int = Field(default=20, ge=1)


class RedisListConsumer(Generic[T]):
    def __init__(
        self,
        redis: RedisClientInterface,
        config: RedisListConsumerConfig,
        message_deserializer: Callable[[str], T],
        message_processor: Callable[[T], None],
    ) -> None:
        self._redis = redis
        self._config = config
        self._message_deserializer = message_deserializer
        self._message_processor = message_processor
        self._is_running = True
        self._lock = threading.Lock()

    def run(self) -> None:
        with self._redis.pubsub() as pubsub:
            try:
                pubsub.subscribe(self._config.list_name)
                while self.is_running():
                    try:
                        response = pubsub.get_message(
                            timeout=self._config.wait_time_seconds, ignore_subscribe_messages=False
                        )
                        if response is None:
                            # timeout
                            continue
                        if "type" in response and response["type"] == "subscribe":
                            continue
                        if "data" not in response:
                            logger.warning("No data in redis response")
                            continue

                        message = response["data"]
                        deserialized = self._message_deserializer(message)
                        self._message_processor(deserialized)
                    except Exception as e:
                        logger.exception(e)
                logger.warning("Stopped consumer")
            finally:
                pubsub.unsubscribe(self._config.list_name)

    def stop(self) -> None:
        logger.warning("Stopping consumer")
        with self._lock:
            self._is_running = False

    def is_running(self) -> bool:
        with self._lock:
            return self._is_running
