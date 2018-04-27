import os

# Application配置参数
setting = {
    "static_path": os.path.join(os.path.dirname(__file__), "static"),
    "template_path": os.path.join(os.path.dirname(__file__), "html"),
    "debug": True,
    "cookie_secret": "ECFEF0SlQxOOadqt4MdXkVggvy5fJk38u8JxzwSAUtQ=",
    "xsrf_cookie": True
}

# mysql
game_mysql_option = dict(
    host="127.0.0.1",
    # database="test5",
    database="wechat_web",
    user="root",
    password="f0afa525de",
    # password="root",
)

logs_mysql_option = dict(
    host="127.0.0.1",
    # database="test5_logs",
    database="wechat_web_logs",
    user="root",
    password="f0afa525de",
    # password="root",
)

redis_option = dict(
    host="127.0.0.1",
    port=6379
)

log_file = os.path.join(os.path.dirname(__name__), 'logs/log')
log_level = "debug"


# Session
# session数据有效期
session_expires = 86400
