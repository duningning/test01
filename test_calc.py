import pytest

from pythoncode.calculator import Calculator

def test_a():
    print("test case a")

class TestCalc:
    def setup_class(self):
        print("计算开始")
        self.calc=Calculator()
    def teardown_class(self):
        print("计算结束")
    @pytest.mark.parametrize('a,b,expect',[[1,1,2],[100,100,200],[0.1,0.1,0.2]],ids=['+1','+2','+3' ])#参数化，ids内的用例数量要与参数组数量一样
    def test_add(self,a,b,expect):
        #calc = Calculator()#1、重复的步骤可以提取出来放在setup中
        result = self.calc.add(a,b)
        assert result == expect
    # def test_add1(self):
    #     #calc = Calculator()
    #     result = self.calc.add(100,100)
    #     assert result == 200
    # def test_add2(self):
    #     #calc = Calculator()
    #     result = self.calc.add(0.1,0.1)
    #     assert result == 0.2
    @pytest.mark.parametrize('a,b,expect',[[1,1,0],[2,3,-1],[4,3,1]],ids=['-1','-2','-3'])
    def test_sub(self,a,b,expect):
        result =self.calc.sub(a,b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect',[[1,2,2],[2,3,6],[4,3,12]],ids=['*1','*2','*3'])
    def test_mul(self,a,b,expect):
        result =self.calc.mul(a,b)
        assert result == expect

    @pytest.mark.parametrize('a,b,expect',[[2,1,2],[6,3,2],[4,2,2]],ids=['/1','/2','/3'])
    def test_div(self,a,b,expect):
        result =self.calc.div(a,b)
        assert result == expect

