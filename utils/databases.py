import peewee_async


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
