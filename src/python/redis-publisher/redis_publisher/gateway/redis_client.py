from abc import ABC, abstractmethod

import redis


class RedisClientInterface(ABC):
    @abstractmethod
    @property
    def data_access_commands() -> redis.core.commands.DataAccessCommands:
        pass


class RedisConfig:
    pass


class RedisClient(RedisClientInterface):
    def __init__(self, config: RedisConfig):
        pass

    def publish(self, channel: str, message: str):
        pass

    @property
    def data_access_commands() -> redis.core.commands.DataAccessCommands:
        pass
