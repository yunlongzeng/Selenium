import unittest
from selenium import webdriver
from po.createtopicpage import CreateTopicPage
from po.loginPage import LoginPage
from time import localtime, strftime
import common.util as Util 
import os
from ddt import ddt, file_data,unpack,data
from common.read_file import Read_Excel

excel_data = Read_Excel('data/user.xls',2)

@ddt
class Create_Topic(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get('http://39.107.96.138:3000/signin')
        #登录
        lg = LoginPage(cls.driver)
        lg.input_username("user19")
        lg.input_password('123456')
        lg.click_login_btn()

    def setUp(self):
        self.driver.get('http://39.107.96.138:3000/topic/create')

    def tearDown(self):
        time_png = strftime("%Y_%m_%d_%H_%M_%S", localtime())
        name = __name__ + time_png
        screenShotFile = os.path.join(Util.getScreenShotsPath(),name+'.png')
        self.driver.save_screenshot(screenShotFile)

    @data(*excel_data.get_excel_data())
    @unpack
    def test_create_topic(self,bankuai,title,content,expect_result,message):
        create = CreateTopicPage(self.driver)
        create.choose_bankuai(bankuai)
        create.input_title(title)
        create.input_text(content)
        create.click_submit_button()  
        text = create.return_result(expect_result)
        self.assertEqual(text,message,"错误提示信息")
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
