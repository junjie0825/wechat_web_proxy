from tornado.web import RequestHandler
from utils.session import Session

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

    def get_current_user(self):
        """
        判断用户是否登录成功
        :return: 登录成功返回用户的昵称，否则返回None
        """
        self.session = Session(self)
        return self.session.data.get('name')

