import unittest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import gmtime, strftime

class TestStringMethods(unittest.TestCase):

    '''
    API实例
    '''
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    @classmethod
    def setUpClass(cls):
        '''
        所有用例执行的前置操作
        '''
        print("---------------setupclass-----------------")
        cls.driver = webdriver.Chrome()

    def setUp(self):
        pass

    def tearDown(self):
        time_png = strftime("%Y_%m_%d_%H_%M", gmtime())
        driver = self.driver
        driver.save_screenshot(time_png + '.png')

    def test1_login(self):
        driver = self.driver
        driver.get("http://39.107.96.138:3000/signin")
        driver.find_element_by_id("name").send_keys("user19")
        driver.find_element_by_id('pass').send_keys("123456")
        driver.find_element_by_class_name("span-primary").click()

        current_url = driver.current_url
        self.assertEqual(current_url,"http://39.107.96.138:3000/")

        user_name = driver.find_element_by_css_selector('.user_name>.dark').text
        self.assertEqual(user_name,"user19")

    # @unittest.skip("create skipping")
    def test2_create(self):
        driver = self.driver
        driver.find_element_by_css_selector('.span-success').click()
        driver.find_element_by_css_selector('#tab-value > option:nth-child(2)').click()
        driver.find_element_by_id("title").send_keys('Ivon test selenium')
        print("111")
        ele = driver.find_element_by_css_selector(".CodeMirror-scroll")
        actions =ActionChains(driver)
        print("222")
        actions.move_to_element(ele).click().send_keys("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh").perform()
        print("333")
        driver.find_element_by_css_selector('.editor_buttons > input').click()

    @classmethod
    def tearDownClass(cls):
        '''
        所有用例执行后的操作
        '''
        print("---------------tear down class--------------")
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)