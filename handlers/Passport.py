from .BaseHandler import BaseHandler
import logging


class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        logging.error("error msg")
        logging.info("info msg")
        logging.warning("warning msg")
        logging.debug("error msg")
        print("print msg")
        # self.application.db
        # self.application.redis
        self.write("hello itcast")
