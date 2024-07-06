from abc import abstractmethod
from typing import Any, Optional

import redis
from pydantic import BaseModel


class RedisClientInterface(
    redis.commands.core.DataAccessCommands[Any], redis.commands.core.ManagementCommands
):
    # @abstractmethod
    # @property
    # # def data_access_commands(self) -> redis.commands.core.DataAccessCommands[Any]:
    # def data_access_commands(self) -> redis.commands.core.DataAccessCommands:
    #     pass

    @abstractmethod
    def pubsub(self) -> redis.client.PubSub:
        pass


class RedisClientConfig(BaseModel):
    host: str
    port: int
    db: int
    password: Optional[str]


def new_redis_client(config: RedisClientConfig) -> RedisClientInterface:
    return redis.StrictRedis(
        host=config.host, port=config.port, db=config.db, password=config.password
    )  # type: ignore

    # def publish(self, channel: str, message: str) -> None:
    #     pass

    # # @property
    # # def data_access_commands(self) -> redis.commands.core.DataAccessCommands[Any]:
    # #     return self.redis

    # def pubsub(self) -> redis.client.PubSub:
    #     return self.redis.pubsub()
