import pytest

#pytest练习
#执行的命令：
import yaml


class TestData:

    @pytest.mark.parametrize(('a','b'),yaml.safe_load(open("./data.yaml")))
    def test_data(self,a,b):
        print(a + b)