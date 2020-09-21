import yaml

from api.base_api import BaseApi
from api.util import Util


class Department(BaseApi):
    def __init__(self):
        self.token = Util().get_token()
        self.params["token"] = self.token
        with open("../steps/department.yaml", encoding="utf-8") as f:
            self.data = yaml.load(f)

    def add(self,name,parentid,order,id):
        self.params["name"] = name
        self.params["parentid"] = parentid
        self.params["order"] = order
        self.params["id"] = id
        return self.send(self.data['add'])

    def update(self,id,name):
        self.params["name"] = name
        self.params["id"] = id
        return self.send(self.data['update'])

    def get(self,id):
        self.params["id"] = id
        return self.send(self.data['get'])

    def delete(self,id):
        self.params["id"] = id
        return self.send(self.data['delete'])