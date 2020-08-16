import requests
import yaml

from test_wechat.api.baseapi import BaseApi
from test_wechat.api.util import Util


class Wework(BaseApi):
    def __init__(self):
        self.token = Util().get_token()
        self.params["token"] = self.token
        with open("../api/wework.yaml", encoding="utf-8") as f:
            self.data = yaml.load(f)

    def test_add(self,userid,name,mobile,department=None):
        if department == None:
            department="1"
        self.params["userid"] = userid
        self.params["mobile"] = mobile
        self.params["name"] = name
        self.params["department"] = department
        return self.send(self.data['add'])

    def test_getinfo(self,userid):
        self.params["userid"] = userid
        return self.send(self.data['getinfo'])

    def test_update(self,userid,name,mobile):
        self.params["userid"] = userid
        self.params["mobile"] = mobile
        self.params["name"] = name
        return self.send(self.data['update'])

    def test_delete(self,userid):
        self.params["userid"] = userid
        return self.send(self.data['delete'])