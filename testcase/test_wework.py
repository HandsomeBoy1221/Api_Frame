from test_wechat.api.wework import Wework


class TestWework:
    def test_add(self):
        print(Wework().test_add('horrypot', '哈利波特', '17311111111'))

    def test_getinfo(self):
        print(Wework().test_getinfo("horrypot"))

    def test_update(self):
        print(Wework().test_update('horrypot', '哈利波特111', '18311111111'))

    def test_delete(self):
        print(Wework().test_delete('horrypot'))