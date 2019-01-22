from testcases.unit_test_create import TestStringMethods

import unittest

def suite01():
    suite = unittest.TestSuite()
    suite.addTest(TestStringMethods('test1_login'))
    suite.addTest(TestStringMethods('test2_create'))
    return suite

def suite02():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader().discover('testcases',pattern='unit*.py')
    suite.addTests(loader)
    return suite

def suite03():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    suite.addTests(loader)
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite03())
