from handlers import Passport, Wechat_connect, TestHandler, Player


handlers = [
    (r'/', Passport.IndexHandler),
    (r'/wechat8000', Wechat_connect.WechatHandler),
    (r'/qrcode', Wechat_connect.QrcodeHandler),
    (r'/wechat8000/profile', Wechat_connect.ProfileHandler),
    (r'/alex', TestHandler.DbHandler),
    (r'/test', Player.UnionidHandler)
    ]
