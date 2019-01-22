from time import gmtime, strftime
import unittest
from selenium import webdriver
from po.loginPage import LoginPage
import common.util as Util 
import os
import time
from ddt import ddt,data, file_data,unpack
from common.read_file import Read_Excel

logger = Util.getLogger(__name__)
excel_data = Read_Excel('data/user.xls',0)
logger = Util.getLogger(__name__)

@ddt
class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logger.info('case2.....')
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
    
    def setUp(self):
        driver = self.driver
        driver.get('http://39.107.96.138:3000/signin')

    def tearDown(self):
        self.driver.delete_all_cookies()
        time_png = strftime("%Y_%m_%d_%H_%M_%S", gmtime())
        name = __name__ + time_png
        screenShotFile = os.path.join(Util.getScreenShotsPath(),name+'.png')
        
        self.driver.save_screenshot(screenShotFile)
        
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    @data(*excel_data.get_excel_data())
    @unpack
    def test_login(self,username,password,status,message):
        driver = self.driver
        lg = LoginPage(driver)

        lg.input_username(username)
        lg.input_password(password)
        lg.click_login_btn()
        text = lg.get_login_result(status)
        print(text)
        print(message)
        self.assertEqual(text,message,'提示信息错误')
