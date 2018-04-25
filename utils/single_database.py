import peewee_async
import config
from singleton import singleton


@singleton
class PooledMySQLDatabase(peewee_async.PooledMySQLDatabase):
    pass


database = PooledMySQLDatabase(**config.mysql_option)
