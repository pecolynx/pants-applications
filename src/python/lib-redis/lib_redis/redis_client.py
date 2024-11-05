from abc import abstractmethod
from typing import Any, Optional

import redis
from pydantic import BaseModel


class RedisClientInterface(
    redis.commands.core.DataAccessCommands, # type: ignore
    redis.commands.core.ManagementCommands, 
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
# def new_redis_client(config: RedisClientConfig) -> redis.Redis[Any]:
    return redis.StrictRedis(
        host=config.host, port=config.port, db=config.db, password=config.password
    ) # type: ignore

    # def publish(self, channel: str, message: str) -> None:
    #     pass

    # # @property
    # # def data_access_commands(self) -> redis.commands.core.DataAccessCommands[Any]:
    # #     return self.redis

    # def pubsub(self) -> redis.client.PubSub:
    #     return self.redis.pubsub()

# def new_redis_cluster_client() -> redis.cluster.RedisCluster:
#     redis_client = redis.cluster.RedisCluster.from_url(
#         url="redis://localhost:6379",
#     )

#     print(type(redis_client))

#     return redis_client
