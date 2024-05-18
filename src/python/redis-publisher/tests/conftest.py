from typing import Any

import pytest
import redis


@pytest.fixture  # type: ignore[misc]
def redis_client() -> "redis.StrictRedis[Any]":
    return redis.StrictRedis(host="localhost", port=6379, db=0)
