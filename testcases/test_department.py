import sys
sys.path.append('..')

import allure
from api.department import Department


class TestDepartment:

    @allure.story('添加部门')
    def test_add(self):
        with allure.step('增'):
            print(Department().add("广州研发中心", "1", "1", "2"))

    @allure.story('修改部门')
    def test_update(self):
        with allure.step('改'):
            print(Department().update("2","广州研发中心222"))

    @allure.story('查询部门')
    def test_get(self):
        with allure.step('查'):
            print(Department().get("2"))

    @allure.story('删除部门')
    def test_delete(self):
        with allure.step('删'):
            print(Department().delete("2"))