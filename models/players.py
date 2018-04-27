from sqlalchemy import Column, String, Integer, VARCHAR, ForeignKey, Float, BigInteger, SmallInteger
from utils import utils
from utils.database import Base


WECHAT_CHANNEL = 5
DEFAULT_DIAMOND = 5
OFFICIAL = 0


class Players(Base):
    __tablename__ = "players"
    uid = Column(BigInteger(), default=utils.make_uid, primary_key=True)
    # uid = Column(BigInteger(), default=999999, primary_key=True)
    nick_name = Column(VARCHAR(32), comment="昵称", default="abcdefg")
    avatar = Column(VARCHAR(255), comment="头像")
    sex = Column(SmallInteger(), comment="性别 0=女 1=男 2=未知")
    imei = Column(VARCHAR(32), default="0")
    imsi = Column(VARCHAR(32), default="0")
    # bank = Column(VARCHAR(512))
    mac = Column(VARCHAR(32))
    model = Column(VARCHAR(50), comment="设备型号", default="unknown")
    reg_time = Column(BigInteger(), default=utils.timestamp, comment="注册时间")
    channel_id = Column(Integer(), default=WECHAT_CHANNEL, comment="注册渠道")
    platform = Column(Integer(), default=1, comment="平台")
    ver = Column(Integer(), comment="版本", default=1)
    diamond = Column(Integer(), default=DEFAULT_DIAMOND, comment="钻石")
    token = Column(VARCHAR(255), comment="玩家 Token")
    refresh_token = Column(VARCHAR(255), comment="刷新 Token")
    expires_at = Column(Integer(), comment="过期时间", default=0)
    auto_token = Column(VARCHAR(40), comment="自动登录 Token")
    openid = Column(VARCHAR(256), comment="开放平台 ID")
    unionid = Column(VARCHAR(100), comment="开放平台统一 ID")
    agent = Column(SmallInteger(), comment="0=用户 1=普通代理 2=VIP代理")
    phone = Column(VARCHAR(20), comment="手机号码")
    pwd = Column(VARCHAR(32), comment="密码")
    verify_code = Column(VARCHAR(32), comment="验证码")
    verify_expire_at = Column(BigInteger(), comment="验证码过期时间")
    login_time = Column(BigInteger(), comment="最后登录时间", default=0)
    ip = Column(BigInteger(), comment="登录 IP", default=0)
    share_time = Column(BigInteger(), default=0)
    get_diamond = Column(Integer(), default=0)
    refer_uid = Column(Integer())
    refer_time = Column(Integer())
    withdraw_time = Column(Integer())
    withdraw_nickname = Column(VARCHAR(128))
    bind_after_login_time = Column(Integer())
    level = Column(Integer())

    # money = Column(Float(), index=True, default=0, comment="余额")
    # agent_parent_1_id = Column(BigInteger(), default=-1, index=True, comment="上级代理 ID")
    # agent_parent_2_id = Column(BigInteger(), default=-1, index=True, comment="最高级代理 ID")
    # promote_parent_1_id = Column(BigInteger(), default=-1, index=True, comment="上级推广员 ID")
    # promote_parent_2_id = Column(BigInteger(), default=-1, index=True, comment="最高级推广员 ID")
    # wechat_temp_time = Column(Integer(), default=-1, comment="微信二维码创建时间")
    # wechat_temp_id = Column(VARCHAR(32), default=1, comment="微信二维码临时 ID")
    # wechat_openid = Column(VARCHAR(32), default=1, comment="微信公众号 OPENID")
    # agent_permission = Column(Integer(), default=1, comment="是否有开通代理的权限")

    # def __str__(self):
    #     return self.unionid


