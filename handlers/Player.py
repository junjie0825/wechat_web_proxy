from handlers.BaseHandler import BaseHandler
from models.players import Players


class UnionidHandler(BaseHandler):
    """
    Accepts GET methods.
    GET: get instance by id, `id` argument is required
    """
    def get(self, *args, **kwargs):
        data = self.db.query(Players).all()
        for item in data:
            print(item.uid)
