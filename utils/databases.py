import peewee_async
import config


def singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


@singleton
class PooledMySQLDatabase(peewee_async.PooledMySQLDatabase):
    pass


database = PooledMySQLDatabase(**config.mysql_option)
