import sys

import allure

sys.path.append('..')
import pytest
import yaml

from api.wework import Wework

with open('../datas/test_wework.yaml',encoding='utf-8') as f:
    wework=yaml.safe_load(f)

class TestWework:

    @allure.story('添加通讯录')
    def test_add(self):
        with allure.step('增'):
            print(Wework().test_add('horrypot', '哈利波特', '17311111111'))

    @allure.story('查询通讯录')
    @pytest.mark.parametrize('a,b',wework)
    def test_getinfo(self,a,b):
        with allure.step('查'):
            print(Wework().test_getinfo("horrypot"))

    @allure.story('修改通讯录')
    def test_update(self):
        with allure.step('改'):
            print(Wework().test_update('horrypot', '哈利波特111', '18311111111'))

    @allure.story('删除通讯录')
    def test_delete(self):
        with allure.step('删'):
            print(Wework().test_delete('horrypot'))