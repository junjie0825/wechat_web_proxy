import time
import hashlib
import datetime
import json
import random
import server
import os
# from api.wechat import conf
# from urllib.parse import quote
from PIL import Image
import single_redis


from jsmin import jsmin
# from models.base_model import redis_client
# import qrcode
import uuid

redis_client = single_redis.redis_client


# 返回 月日 时分秒 的时间字符串
def time_mdh():
    return time.strftime("%m-%d %X ", time.localtime())


# 返回 UUID
def uuid4():
    return uuid.uuid4()


# def __make_qrcode(text):
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_H,
#         box_size=6,
#         border=2,
#     )
#     qr.add_data(text)
#     qr.make(fit=True)
#     img = qr.make_image()
#     return img


# def save_qrcode(img, file_name, type='', dir_name='static/qrcode'):
#     name = dir_name + "/" + type + "_" + str(file_name) + ".jpg"
#     if not os.path.exists(name):
#         img.save(name)


# def make_share_qrcode(uid):
#     name = "static/qrcode/share_" + str(uid) + ".jpg"
#     if os.path.exists(name):
#         return
#     url = "https://open.weixin.qq.com/connect/oauth2/authorize?appid={0}&" \
#           "redirect_uri={1}&response_type=code&scope=snsapi_userinfo&state={2}#wechat_redirect"
#     url = url.format(conf['wechat']['app_id'], quote(conf['wechat']['redirect_url'], safe=''), str(uid))
#     return __make_qrcode(url)
#
#
# def make_url_code(url):
#     return __make_qrcode(url)


# 从 Redis 中返回一个新的 UID
def make_uid(self):
    key = "all_uids"
    uid = redis_client.spop(key)
    if not uid:
        return 0
    return int(uid)


def create_qr_code(uid, croped_im):
    im = Image.open("./static/bg.png")
    im.paste(croped_im, (260, 654))
    icon = Image.open("./static/icon.png")
    im.paste(icon, (360, 760))
    im.save("./static/qrcode/share_" + str(uid) + ".jpg")


# 返回时间戳int型
def timestamp():
    return int(time.time())


# 返回当天0时的时间戳int型
def timestamp_today():
    any_day = datetime.date(2011, 11, 1)
    date_today = any_day.today()
    date_str = time.strptime(str(date_today), "%Y-%m-%d")
    return int(time.mktime(date_str))


# 返回昨天的0点的时间戳
def timestamp_yesterday():
    return timestamp_today() - 24 * 60 * 60


# 返回一个星期前的0点时间戳
def timestamp_prev_week():
    return timestamp_today() - 24 * 60 * 60 * 6


def md5(data):
    return hashlib.md5(data).hexdigest()


# 读json文件，并返回对应的对象，适用于小配置文件的读取
def read_json_file(filename):
    try:
        with open(filename) as js_file:
            mini_con = jsmin(js_file.read())
            obj = json.loads(mini_con, strict=False)
            return obj
    except Exception as data:
        print("read json file fail:", filename, data)
    return {}


# 对象到json字符串
def json_encode(data):
    return str(json.dumps(data, ensure_ascii=False))


# 获得随机数字，并返回字符串
def get_random_num(length=5):
    assert 0 < length <= 20
    min_num = 10 ** (length - 1)
    max_num = 10 ** length - 1
    return str(random.randint(min_num, max_num))


def randint(min_num=0, max_num=0):
    return random.randint(min_num, max_num)


def str_to_int(data):
    # 从字符串转换成INT
    if not data:
        return 0
    try:
        return int(data)
    except Exception as data:
        print(data)
    return 0


class ObjectDict(dict):
    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            return None

    def __setattr__(self, name, value):
        self[name] = value
