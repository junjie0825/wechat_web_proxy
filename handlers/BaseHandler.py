from tornado.web import RequestHandler


class BaseHandler(RequestHandler):
    """Handler基类"""
    def prepare(self):
        pass

    def write_error(self, status_code, **kwargs):
        pass

    def set_default_headers(self):
        pass

    def initialize(self):
        pass

    def on_finish(self):
        pass

    @property
    def game_db(self):
        return self.application.game_db

    @property
    def logs_db(self):
        return self.application.logs_db

    @property
    def redis(self):
        return self.application.redis
