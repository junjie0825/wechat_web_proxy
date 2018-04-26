from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import config
from utils.singleton import singleton


# @singleton
# class create_engine(sqlalchemy.create_engine):
#     pass

Base = declarative_base()
engine = create_engine('mysql://%s:%s@%s/%s?charset=utf8' %
                       (config.mysql_option["user"], config.mysql_option["password"],
                        config.mysql_option["host"], config.mysql_option["database"]),
                       encoding='utf-8', echo=False, pool_size=100, pool_recycle=10)
