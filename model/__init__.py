import redis
from config import redis_config


class RedisClient:
    def __init__(self, client: redis.Redis):
        self._client = client

    def set(self, key, value):
        return self._client.set(key, value)

    def get(self, key):
        return self._client.get(key)

    def delete(self, key):
        return self._client.delete(key)

pool = redis.ConnectionPool(host=redis_config.get('host'), port=redis_config.get('port'), db=redis_config.get('db'))
original_client = redis.Redis(connection_pool=pool)
redis_client = RedisClient(original_client)
