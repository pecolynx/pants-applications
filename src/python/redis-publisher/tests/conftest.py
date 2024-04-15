import pytest
import redis


@pytest.fixture
def redis_client() -> redis.Redis:
    return redis.Redis(host="localhost", port=6379, db=0)
