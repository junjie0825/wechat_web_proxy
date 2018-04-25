import tornado.web
import tornado.gen
import xmltodict
import hashlib
import time
import json
# from models.players import Players
from tornado.httpclient import AsyncHTTPClient, HTTPRequest
from constants import *

from handlers.BaseHandler import BaseHandler


class AccessToken(object):
    """access_token辅助类"""
    _access_token = None
    _create_time = 0
    _expires_in = 0

    @classmethod
    @tornado.gen.coroutine
    def update_access_token(cls):
        client = AsyncHTTPClient()
        url = "https://api.weixin.qq.com/cgi-bin/token?" \
              "grant_type=client_credential&appid=%s&secret=%s" % (WECHAT_APPID, WECHAT_APPSECRET)
        resp = yield client.fetch(url)
        dict_data = json.loads(resp.body)
        if "error" in dict_data:
            raise Exception("wechat server error")
        else:
            print(dict_data)
            cls._access_token = dict_data["access_token"]
            cls._expires_in = dict_data["expires_in"]
            cls._create_time = time.time()

    @classmethod
    @tornado.gen.coroutine
    def get_access_token(cls):
        if time.time() - cls._create_time > (cls._expires_in - 200):
            # 向微信获取access_token
            yield cls.update_access_token()
            raise tornado.gen.Return(cls._access_token)
        else:
            raise tornado.gen.Return(cls._access_token)


class WechatHandler(BaseHandler):
    """对接微信服务器"""
    def prepare(self):
        signature = self.get_argument("signature")
        timestamp = self.get_argument("timestamp")
        nonce = self.get_argument("nonce")
        tmp = [WECHAT_TOKEN, timestamp, nonce]
        tmp.sort()
        # sorted()
        tmp = "".join(tmp).encode("utf-8")
        real_signature = hashlib.sha1(tmp).hexdigest()
        if signature != real_signature:
            self.send_error(403)

    def get(self, *args, **kwargs):
        echostr = self.get_argument("echostr")
        self.write(echostr)

    def post(self, *args, **kwargs):
        """
        <xml>
        <ToUserName><![CDATA[粉丝号]]></ToUserName>
        <FromUserName><![CDATA[公众号]]></FromUserName>
        <CreateTime>1460541339</CreateTime>
        <MsgType><![CDATA[text]]></MsgType>
        <Content><![CDATA[test]]></Content>
        </xml>
        """
        xml_data = self.request.body
        dict_data = xmltodict.parse(xml_data)
        msg_type = dict_data["xml"]["MsgType"]
        to_user = dict_data["xml"]["FromUserName"]
        from_user = dict_data["xml"]["ToUserName"]
        c_time = int(time.time())

        if msg_type == "text":
            content_tmp = dict_data["xml"]["Content"]
            print("*********************")
            if bytes(content_tmp, encoding="utf-8") == (bytes("李红艳", encoding="utf-8")):
                # print("OKOKOKOKOKOK")
                content = "聪明聪明"
            else:
                content = "%s是笨蛋超级大笨蛋" % content_tmp
            # dict_data["xml"]["Content"]
            # resp_data = """<xml>
            #         <ToUserName><![CDATA[{0}]]></ToUserName>
            #         <FromUserName><![CDATA[{1}]]></FromUserName>
            #         <CreateTime>{2}</CreateTime>
            #         <MsgType><![CDATA[text]]></MsgType>
            #         <Content><![CDATA[{3}]]></Content>
            #         </xml>
            #       """.format(to_user, from_user, c_time, content)
            #
        elif msg_type == "event":
            content = "您总算是来了呀"
            # print(dict_data)
            if dict_data["xml"]["Event"] == "subscribe":
                """用户关注事件"""
                if not(dict_data["xml"]["EventKey"] is None):
                    print("**************************!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                    print(type(dict_data["xml"]["EventKey"]))
                    """场景值存在"""
                    event_key = dict_data["xml"]["EventKey"]
                    scene_id = event_key[8:]
                    content = "您来了，%s次" % scene_id
            elif dict_data["xml"]["Event"] == "SCAN":
                scene_id = dict_data["xml"]["EventKey"]
                content = "您扫描的是%s" % scene_id
        else:
            content = "除文字消息，其他消息未做处理"
        resp_data = """<xml>
                <ToUserName><![CDATA[{0}]]></ToUserName>
                <FromUserName><![CDATA[{1}]]></FromUserName>
                <CreateTime>{2}</CreateTime>
                <MsgType><![CDATA[text]]></MsgType>
                <Content><![CDATA[{3}]]></Content>
                </xml>
              """.format(to_user, from_user, c_time, content)
        self.write(resp_data)


class QrcodeHandler(BaseHandler):
    """请求微信服务器生成带参数的Qrcode返回给客户"""
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        scene_id = self.get_argument("sid")
        try:
            access_token = yield AccessToken.get_access_token()
        except Exception as e:
            self.write("errmsg: %s" % e)
        else:
            client = AsyncHTTPClient()
            url = "https://api.weixin.qq.com/cgi-bin/qrcode/create?access_token=%s" % access_token
            req_data = {"action_name": "QR_LIMIT_SCENE", "action_info": {"scene": {"scene_id": scene_id}}}
            req = HTTPRequest(
                url=url,
                method="POST",
                body=json.dumps(req_data)
            )
            resp = yield client.fetch(req)
            dict_data = json.loads(resp.body)
            if "errcode" in dict_data:
                self.write("errmsg: get qrcode failed")
            else:
                ticket = dict_data["ticket"]
                qrcode_url = dict_data["url"]
                self.write('<img src="https://mp.weixin.qq.com/cgi-bin/showqrcode?ticket=%s"><br/>' % ticket)
                self.write('<p>%s</p>' % qrcode_url)


class ProfileHandler(BaseHandler):
    def __create_user(self, ):
        pass

    def unionid_is_exist(self, tmp_unionid):
        sql = 'SELECT * FROM players WHERE unionid = %s'
        res_by_unionid = self.db.get(sql, tmp_unionid)
        if res_by_unionid:
            return res_by_unionid
        else:
            return False

    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        access_token = yield AccessToken.get_access_token()
        code = self.get_argument("code")
        client = AsyncHTTPClient()
        url = "https://api.weixin.qq.com/sns/oauth2/access_token?" \
              "appid=%s&secret=%s&code=%s&grant_type=authorization_code" % (WECHAT_APPID, WECHAT_APPSECRET, code)
        resp = yield client.fetch(url)
        dict_data = json.loads(resp.body)
        print("access!!!!!!!!!!!!!!!!!", resp.body)
        if "errcode" in dict_data:
            self.write("error occur")
        else:
            # access_token = dict_data["access_token"]
            open_id = dict_data["openid"]
            url = "https://api.weixin.qq.com/cgi-bin/user/info" \
                  "?access_token=%s&openid=%s&lang=zh_CN" % (access_token, open_id)
            print("11111111111111111111111111")
            resp = yield client.fetch(url)
            # try:
            #     print(resp.body)
            # except Exception as e:
            #     pass
            user_data = json.loads(resp.body)
            if "errcode" in user_data:
                self.write("error occur at get info from wechat")
            else:
                unionid = user_data["unionid"]
                player_by_unionid = self.unionid_is_exist(unionid)
                if player_by_unionid:
                    self.write(player_by_unionid)
                else:
                    # self.__create_user()
                    self.write("don't exist")
    """
    用户最终访问的URL网址
    https://open.weixin.qq.com/connect/oauth2/authorize?appid=wxf5a0ff0a7fe1c69b&redirect_uri=http%3A//wechat.hnbdfyy.com.cn/wechat8000/profile&response_type=code&scope=snsapi_userinfo&state=1#wechat _redirect
    http://wechat.hnbdfyy.com.cn/wechat8000/profile
    """
