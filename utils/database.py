from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import config
# from utils.singleton import singleton


# @singleton
# class create_engine(sqlalchemy.create_engine):
#     pass

Base = declarative_base()
game_engine = create_engine('mysql://%s:%s@%s/%s?charset=utf8' %
                            (config.game_mysql_option["user"], config.game_mysql_option["password"],
                             config.game_mysql_option["host"], config.game_mysql_option["database"]),
                            encoding='utf-8', echo=False, pool_size=100, pool_recycle=10)

logs_engine = create_engine('mysql://%s:%s@%s/%s?charset=utf8' %
                            (config.logs_mysql_option["user"], config.logs_mysql_option["password"],
                             config.logs_mysql_option["host"], config.logs_mysql_option["database"]),
                            encoding='utf-8', echo=False, pool_size=100, pool_recycle=10)
