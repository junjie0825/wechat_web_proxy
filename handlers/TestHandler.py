from handlers.BaseHandler import BaseHandler
from models.test_name_model import TestNameModel
import tornado.web


class RootHandler(BaseHandler):
    """
    Accepts GET methods.
    GET: get instance by id, `id` argument is required
    """
    async def get(self):
        obj_id = self.get_argument('id', None)
        try:
            obj = await self.application.objects.get(TestNameModel, id=obj_id)
            print(type(obj))
            print(obj)
            self.write({
                'id': obj.id,
                'name': obj.name,
            })
        except TestNameModel.DoesNotExist:
            raise tornado.web.HTTPError(404, "Object not found!")