import pytest

#pytest练习
#执行的命令：
import yaml


class TestData:

    @pytest.mark.parametrize(('a','b'),yaml.safe_load(open("./data.yaml")))
    def test_data(self,a,b):
        print(a + b)


    #raise
    def fun_raise(self):
        raise SystemExit(1)

    def test_raise(self):

        with pytest.raises(SystemExit):
            self.fun_raise()
            pytest.fail("系统退出")

    @pytest.mark.xfail(raises="SystemExit")
    def test_faile(self):
        self.fun_raise()

    def test_assert(self):
        set1 = set("1308")
        set2 = set("8035")
        assert 0