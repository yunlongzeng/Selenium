import unittest
from ddt import ddt, data, file_data,unpack

def get_num():
    return  [['xiaoming', '121231212', '失败', '用户名或密码错误'], ['helloworld', '123456', '成功', 'helloworld']]

@ddt
class FooTestCase(unittest.TestCase):
    # @data(3, 4, 12, 23)
    # def test_larger_than_two(self, value):
    #     print('----------',value)

    # @file_data('test_json.json')
    # def test_case2(self,username,pwd,email):
    #     print('-----',username,'-----')
    #     print('-----',pwd,'-----')
    #     print('-----',email,'-----')

    @data(*get_num())
    @unpack
    def test_func(self,one,two,three,four):
        print('-----',one)

if __name__ == '__main__':
    unittest.main(verbosity=2)