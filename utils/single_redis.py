import redis
import config
from singleton import singleton


@singleton
class StrictRedis(redis.StrictRedis):
    pass


redis_client = StrictRedis(**config.redis_option)
