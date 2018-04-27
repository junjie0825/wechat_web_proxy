from models.student import Students
from handlers.BaseHandler import BaseHandler


class DbHandler(BaseHandler):

    def get(self, *args, **kwargs):
        data = self.db.query(Students).all()
        for item in data:
            print(item.name)
