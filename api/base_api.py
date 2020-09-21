import json

import requests


class BaseApi:
  params = {}

  def send(self, data):
    raw = json.dumps(data)
    for key, value in self.params.items():
      raw = raw.replace('${' + key + '}', value)
    data = json.loads(raw)
    return requests.request(**data).json()