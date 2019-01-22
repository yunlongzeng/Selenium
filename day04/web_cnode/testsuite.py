import unittest
# from test.cases.case2 import LoginTest
# from test.cases.case3 import Regist_New_User
from testcases.cases.case2_login import LoginTest
from testcases.cases.case3_regist import Regist_New_User
from testcases.cases.case4_create_topic import Create_Topic


def get_suite():
    testsuite = unittest.TestSuite()

    # loader = unittest.TestLoader().discover(start_dir='test',pattern='case*.py')
    # testsuite.addTests(loader)

    #注册
    loader1 = unittest.TestLoader().loadTestsFromTestCase(Regist_New_User)
    #登录
    loader2 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    #发帖
    loader3 = unittest.TestLoader().loadTestsFromTestCase(Create_Topic)

    # testsuite.addTests(loader1)
    # testsuite.addTests(loader2)
    testsuite.addTests(loader3)

    return testsuite

if __name__ == "__main__":
    suite = get_suite()

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)