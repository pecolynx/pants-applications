import redis


class RedisClient:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.client = redis.Redis(host=host, port=port)

    def ping(self) -> None:
        self.client.ping()
