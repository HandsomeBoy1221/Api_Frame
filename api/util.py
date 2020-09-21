import requests

class Util:
    def get_token(self):
        request_parma={
            "corpid" : "xxxxxxxxxx",
            "corpsecret" : "xxxxxxxxxx"
        }
        r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",params=request_parma)
        return r.json()['access_token']