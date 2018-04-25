from handlers import Passport, Wechat_connect


handlers = [
    (r'/', Passport.IndexHandler),
    (r'/wechat8000', Wechat_connect.WechatHandler),
    (r'/qrcode', Wechat_connect.QrcodeHandler),
    (r'/wechat8000/profile', Wechat_connect.ProfileHandler),
    ]
