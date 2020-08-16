from test_wechat.api.department import Department


class TestDepartment:
    def test_add(self):
        print(Department().add("广州研发中心", "1", "1", "2"))

    def test_update(self):
        print(Department().update("2","广州研发中心222"))

    def test_get(self):
        print(Department().get("2"))

    def test_delete(self):
        print(Department().delete("2"))