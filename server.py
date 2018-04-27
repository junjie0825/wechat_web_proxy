import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import config
import utils.database
from sqlalchemy.orm import sessionmaker, scoped_session

from tornado.options import define, options
from urls import handlers

define("port", type=int, default=8000, help="run sever on the given port")


class Application(tornado.web.Application):
    """"""
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        # self.db =
        # self.redis = redis.StrictRedis(**config.redis_option)
        game_database = utils.database.game_engine
        logs_database = utils.database.logs_engine
        self.game_db = scoped_session(sessionmaker(bind=game_database,
                                                   autocommit=False, autoflush=True,
                                                   expire_on_commit=False))

        self.logs_db = scoped_session(sessionmaker(bind=logs_database,
                                                   autocommit=False, autoflush=True,
                                                   expire_on_commit=False))


def main():

    options.logging = config.log_level
    options.log_file_prefix = config.log_file
    tornado.options.parse_command_line()
    app = Application(
        handlers, **config.setting
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
