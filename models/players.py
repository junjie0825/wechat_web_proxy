import peewee
from models.base_model import BaseGameModel
from handlers.BaseHandler import BaseHandler
from utils import utils


WECHAT_CHANNEL = 5
DEFAULT_DIAMOND = 5
OFFICIAL = 0


class Players(BaseGameModel):
    uid = peewee.PrimaryKeyField(default=utils.make_uid)
    nick_name = peewee.CharField(max_length=32, help_text="昵称")
    avatar = peewee.CharField(max_length=255, help_text="头像")
    sex = peewee.SmallIntegerField(help_text="性别 0=女 1=男 2=未知")
    imei = peewee.CharField(max_length=32)
    imsi = peewee.CharField(max_length=32)
    bank = peewee.CharField(max_length=512)
    mac = peewee.CharField(max_length=32)
    model = peewee.CharField(max_length=50, help_text="设备型号")
    reg_time = peewee.BigIntegerField(default=utils.timestamp, help_text="注册时间")
    channel_id = peewee.IntegerField(default=WECHAT_CHANNEL, help_text="注册渠道")
    platform = peewee.IntegerField(default=1, help_text="平台")
    ver = peewee.CharField(max_length=20, help_text="版本")
    diamond = peewee.IntegerField(default=DEFAULT_DIAMOND, help_text="钻石")
    token = peewee.CharField(max_length=255, help_text="玩家 Token")
    refresh_token = peewee.CharField(max_length=255, help_text="刷新 Token")
    expires_at = peewee.IntegerField(help_text="过期时间")
    auto_token = peewee.CharField(max_length=40, help_text="自动登录 Token")
    openid = peewee.CharField(max_length=100, help_text="开放平台 ID")
    unionid = peewee.CharField(max_length=100, help_text="开放平台统一 ID")
    agent = peewee.SmallIntegerField(help_text="0=用户 1=代理")
    phone = peewee.CharField(max_length=20, help_text="手机号码")
    pwd = peewee.CharField(max_length=32, help_text="密码")
    verify_code = peewee.CharField(max_length=32, help_text="验证码")
    verify_expire_at = peewee.BigIntegerField(help_text="验证码过期时间")
    login_time = peewee.BigIntegerField(help_text="最后登录时间")
    ip = peewee.BigIntegerField(help_text="登录 IP")
    money = peewee.FloatField(index=True, default=0, help_text="余额")
    agent_parent_1_id = peewee.BigIntegerField(default=-1, index=True, help_text="上级代理 ID")
    agent_parent_2_id = peewee.BigIntegerField(default=-1, index=True, help_text="最高级代理 ID")
    promote_parent_1_id = peewee.BigIntegerField(default=-1, index=True, help_text="上级推广员 ID")
    promote_parent_2_id = peewee.BigIntegerField(default=-1, index=True, help_text="最高级推广员 ID")
    wechat_temp_time = peewee.IntegerField(default=-1, help_text="微信二维码创建时间")
    wechat_temp_id = peewee.CharField(default=1, help_text="微信二维码临时 ID")
    wechat_openid = peewee.CharField(default=1, help_text="微信公众号 OPENID")
    agent_permission = peewee.IntegerField(default=1, help_text="是否有开通代理的权限")
