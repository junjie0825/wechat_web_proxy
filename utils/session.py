import json
import uuid
import config
import logging


class Session(object):
    """session类"""

    def __init__(self, request_handler):
        """
        request_handler - 请求处理类对象实例
        sid - session_id
        data - session数据, 字典类型
        """
        self.request_handler = request_handler
        # 从请求中读取cookie获取session_id
        self.sid = request_handler.get_secure_cookie("session_id")
        if isinstance(self.sid, bytes):
            self.sid = str(self.sid, encoding="utf-8")
        print("*****************")
        print("!!!!!!!!!!!!!!!!!!!!get_secure_cookie", self.sid)
        print("get_secure_cookie,type=", type(self.sid))
        if self.sid:
            try:
                session_data = request_handler.redis.get("sess_%s" % self.sid)
            except Exception as e:
                logging.error(e)
                raise e

            # session_data已过期，返回None
            if session_data:
                self.data = json.loads(session_data)
            else:
                self.data = {}
        # 如用户未session_id，需要新生成一个session_id与这个用户对应
        else:
            self.sid = uuid.uuid4().hex
            print("type=", type(self.sid))
            print(self.sid)
            self.data = {}
            self.request_handler.set_secure_cookie("session_id", self.sid)

    def save(self):
        """保存"""
        # 将session_data序列化为json字符串
        json_data = json.dumps(self.data)
        # 将session_data序列化为json字符串
        try:
            self.request_handler.redis.setex("sess_%s" % self.sid, config.session_expires, json_data)
        except Exception as e:
            logging.error(e)
            raise e

    def clear(self):
        """清除"""
        self.request_handler.clear_cookie("session_id")
        try:
            self.request_handler.redis.delete("sess_%s" % self.sid)
        except Exception as e:
            logging.error(e)
            raise e
