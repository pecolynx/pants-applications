from abc import ABC, abstractmethod
from typing import Any, Optional

import redis
from pydantic import BaseModel


class RedisClientInterface(ABC):
    @abstractmethod
    @property
    def data_access_commands(self) -> redis.commands.core.DataAccessCommands[Any]:
        pass

    @abstractmethod
    def pubsub(self) -> redis.client.PubSub:
        pass


class RedisClientConfig(BaseModel):
    host: str
    port: int
    db: int
    password: Optional[str]


class RedisClient(RedisClientInterface):
    def __init__(self, config: RedisClientConfig) -> None:
        self.redis = redis.StrictRedis(
            host=config.host, port=config.port, db=config.db, password=config.password
        )

    def publish(self, channel: str, message: str) -> None:
        pass

    @property
    def data_access_commands(self) -> redis.commands.core.DataAccessCommands[Any]:
        return self.redis

    def pubsub(self) -> redis.client.PubSub:
        return self.redis.pubsub()
