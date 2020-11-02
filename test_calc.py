import pytest
import yaml

from pythoncode.calculator import Calculator


# 解析测试数据
def get_datas():
    with open("./datas/calc.yml") as f:
        datas = yaml.safe_load(f)  # 读取一次就没有数据了，所以只需要读取一次就够了
    add_datas = datas['add']['datas']
    add_ids = datas['add']['ids']
    print(add_ids)
    print(add_datas)
    return [add_datas, add_ids]


# 解析测试步骤
def get_steps(calc, a, b, expect):
    with open("./steps/steps.yml") as f:
        steps = yaml.safe_load(f)
        for step in steps:
            if 'add' == step:
                print('add')
                result = calc.add(a, b)
            # elif 'sub'==steps:
            #     print("sub")
            #     result =calc.sub(a,b)
            assert expect == result


# 使用Fixture代替 class TestCalc中的setup和tear_down
# @pytest.fixture(scope="class")
# def get_cacl():
#     print("计算开始")
#     cacl = Calculator()
#     yield cacl
#     print("计算结束")
# 放入conftest文档中去


class TestCalc:
    # def setup_class(self):#已被上面的fixture代替
    #     print("计算开始")
    #     self.calc=Calculator()
    # def teardown_class(self):
    #     print("计算结束")
    # @pytest.mark.parametrize('a,b,expect',[[1,1,2],[100,100,200],[0.1,0.1,0.2]],ids=['+1','+2','+3' ])#参数化，ids内的用例数量要与参数组数量一样
    @pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
    def test_add(self, get_cacl, a, b, expect):
        # calc = Calculator()#1、重复的步骤可以提取出来放在setup中
        # result = self.calc.add(a,b)
        result = get_cacl.add(a, b)  # 使用新定义的get_cacl改造
        assert result == expect

    #    def test_add1(self):
    #     #calc = Calculator()
    #     assert result == 200
    # def test_add2(self):
    #     #calc = Calculator()
    #     result = self.calc.add(0.1,0.1)
    #     assert result == 0.2
    @pytest.mark.parametrize('a,b,expect', [[1, 1, 0], [2, 3, -1], [4, 3, 1]], ids=['-1', '-2', '-3'])
    def test_sub(self, get_cacl, a, b, expect):
        # result =self.calc.sub(a,b)
        result = get_cacl.sub(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [[1, 2, 2], [2, 3, 6], [4, 3, 12]], ids=['*1', '*2', '*3'])
    def test_mul(self, get_cacl, a, b, expect):
        # result =self.calc.mul(a,b)
        result = get_cacl.mul(a, b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect', [[2, 1, 2], [6, 3, 2], [4, 2, 2]], ids=['/1', '/2', '/3'])
    def test_div(self, get_cacl, a, b, expect):
        # result =self.calc.div(a,b)
        result = get_cacl.div(a, b)
        assert result == expect

    def test_div(self):  # 捕获异常
        with pytest.raises(ZeroDivisionError):  # 指定特定的异常
            result = self.calc.div(1, 0)

    # 测试步骤
    def test_add_steps(self):
        get_steps(self.calc, 1, 2, 3)

        # assert 2 == self.calc.add(1,1)
        # assert 1 == self.calc.sub(2,1)
        # assert 6 == self.calc.mul(2,3)
        # assert 7 == self.calc.div(14,2)
