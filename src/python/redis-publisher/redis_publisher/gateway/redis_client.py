from abc import ABC, abstractmethod
from typing import Any

import redis


class RedisClientInterface(ABC):
    @abstractmethod
    @property
    def data_access_commands(self) -> redis.commands.core.DataAccessCommands[Any]:
        pass


class RedisConfig:
    pass


class RedisClient(RedisClientInterface):
    def __init__(self, config: RedisConfig) -> None:
        self.redis = redis.StrictRedis(host="localhost", port=6379, db=0)

    def publish(self, channel: str, message: str) -> None:
        pass

    @property
    def data_access_commands(self) -> redis.commands.core.DataAccessCommands[Any]:
        return self.redis
