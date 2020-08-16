import requests

class Util:
    def get_token(self):
        request_parma={
            "corpid" : "xxxxxxxx",
            "corpsecret" : "xxxxxxxx"
        }
        r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",params=request_parma)
        return r.json()['access_token']