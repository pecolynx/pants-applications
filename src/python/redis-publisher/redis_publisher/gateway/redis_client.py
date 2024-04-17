from abc import ABC, abstractmethod

import redis


class RedisClientInterface(ABC):
    @abstractmethod
    @property
    def data_access_commands(self) -> redis.core.commands.DataAccessCommands:
        pass


class RedisConfig:
    pass


class RedisClient(RedisClientInterface):
    def __init__(self, config: RedisConfig) -> None:
        pass

    def publish(self, channel: str, message: str) -> None:
        pass

    @property
    def data_access_commands(self) -> redis.core.commands.DataAccessCommands:
        pass
