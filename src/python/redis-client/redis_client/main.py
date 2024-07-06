import logging
import time

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
    main()
