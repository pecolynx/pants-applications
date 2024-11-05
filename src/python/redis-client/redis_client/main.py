import logging
import time
from datetime import datetime, timezone
from lib_redis.redis_client import RedisClientConfig, new_redis_client

logger = logging.getLogger(__name__)


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    logger.info("Starting Redis Client")
    redis_client = new_redis_client(
        config=RedisClientConfig(host="localhost", port=6379, db=0, password=None)
    )
    result = redis_client.ping()
    logger.info(f"Redis ping result: {result}")
    logger.info("Ping successful")

    while True:
        result = redis_client.ping()
        logger.info(f"Redis ping result: {result}")
        time.sleep(9 * 60 * 60)  # 9 hour


if __name__ == "__main__":
    # a = new_redis_cluster_client()
    # main()
    # print('hello')

    print(datetime.fromisoformat("2024-08-27T17:12:13.000000+00:00"))
    print(datetime.fromisoformat("2024-08-27T17:12:13.00000+00:00"))
    print(datetime.fromisoformat("2024-08-27T17:12:13.0000+00:00"))
    print(datetime.fromisoformat("2024-08-27T17:12:13.000+00:00"))
    print(datetime.fromisoformat("2024-08-27T17:12:13.00+00:00"))
    print(datetime.fromisoformat("2024-08-27T17:12:13.0+00:00"))
    print(datetime.fromisoformat("2024-08-27T17:12:13+00:00"))
    print(datetime.fromisoformat("2024-08-27T17:12:13.000000"))
    print(datetime.fromisoformat("2024-08-27T17:12:13.00000"))
    print(datetime.fromisoformat("2024-08-27T17:12:13.0000"))
    print(datetime.fromisoformat("2024-08-27T17:12:13.000"))
    print(datetime.fromisoformat("2024-08-27T17:12:13.00"))
    print(datetime.fromisoformat("2024-08-27T17:12:13.0"))
    print(datetime.fromisoformat("2024-08-27T17:12:13"))
    while True:
        s = datetime.now(timezone.utc).isoformat()
        d = datetime.fromisoformat(s)
        print(s)
