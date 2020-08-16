import json
import re

import pytest
import requests


def test_create_data():
    data = [("horrypot" + str(x),
             "哈利波特",
             "138%08d" % x) for x in range(20)]
    return data

class TestDemo:

    @pytest.fixture(scope="session")
    def token(self):
        request_parma={
            "corpid" : "wwb24e6fe4d7d1c71a",
            "corpsecret" : "yIhI9TMNunyO38XkFESwsKUb1tfcBWtw01LZmOz7Xvc"
        }
        r=requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken",params=request_parma)
        return r.json()['access_token']

    def test_add(self,token,userid,name,mobile,department=None):
        if department == None:
            department=[1]
        request_parma={
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        r=requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}",
                        json=request_parma)
        return r.json()

    def test_getinfo(self,token,userid):
        r=requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid={userid}")
        return r.json()

    def test_update(self,token,userid,name,mobile):
        request_parma={
            "userid": userid,
            "name": name,
            "mobile": mobile
        }
        r=requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={token}",json=request_parma)
        return r.json()

    def test_delete(self,token,userid):
        r=requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid={userid}")
        return r.json()

    @pytest.mark.parametrize('userid,name,phone',test_create_data())
    def test_wework(self,token,userid,name,phone):
        # name="哈利波特"
        # phone="17300000000"
        # userid="horrypot"
        try:
            assert 'created' in self.test_add(token,userid,name,phone)['errmsg']
        except AssertionError as e:
            if "mobile existed" in e.__str__():
                re_userid = re.findall(":(.*)'$", e.__str__())[0]
                self.test_delete(token, re_userid)
                assert 'created' in self.test_add(token, userid, name, phone)['errmsg']
        assert name in self.test_getinfo(token, userid)['name']
        assert 'updated' in self.test_update(token,userid,"哈利波特12305",phone)['errmsg']
        assert '哈利波特12305' in self.test_getinfo(token, userid)['name']
        assert 'deleted' in self.test_delete(token,userid)['errmsg']
        assert 60111 == self.test_getinfo(token, userid)["errcode"]