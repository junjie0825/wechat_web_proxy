import peewee
import redis
import config
import utils.databases



# conf = anyconfig.load("configs/configs.json")
# game_conf = conf['db']['game_db']
# logs_conf = conf['db']['logs_db']
# game_db = PooledMySQLDatabase(**config.mysql_option)
# logs_db = PooledMySQLDatabase(host=logs_conf['host'], user=logs_conf['username'], password=logs_conf['password'],
#                         port=logs_conf['port'], database=logs_conf['db'])
# redis_client = redis.StrictRedis(host=conf['redis']['host'], port=conf['redis']['port'], db=conf['redis']['db'],
#                                  password=conf['redis']['password'], socket_timeout=conf['redis']['socket_timeout'])
database = utils.databases.database
print("1--------------", id(database))
print(database)


class BaseGameModel(peewee.Model):
    class Meta:
        database = database


# class BaseLogsModel(Model):
#     class Meta:
#         database = logs_db
