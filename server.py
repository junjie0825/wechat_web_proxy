import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import config
import redis
import torndb

from tornado.options import define, options
from urls import handlers

define("port", type=int, default=8000, help="run sever on the given port")


class Application(tornado.web.Application):
    """"""
    def __init__(self, *args, **kwargs):
        super(Application, self).__init__(*args, **kwargs)
        self.db = torndb.Connection(**config.mysql_option)
        self.redis = redis.StrictRedis(**config.redis_option)


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