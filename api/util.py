import requests

class Util:
    def get_token(self):
        request_parma={
            "corpid" : "wwb24e6fe4d7d1c71a",
            "corpsecret" : "yIhI9TMNunyO38XkFESwsKUb1tfcBWtw01LZmOz7Xvc"
        }
        r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",params=request_parma)
        return r.json()['access_token']