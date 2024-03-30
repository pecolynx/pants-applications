import redis


class RedisClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client = redis.Redis(host=host, port=port)

    def ping(self):
        return self.client.ping()
