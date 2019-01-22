import unittest,os,random
from selenium import webdriver
from time import localtime, strftime
import common.util as Util
from po.registPage import RegistPage
from ddt import ddt, file_data,unpack,data
from common.read_file import Read_Excel

excel_data = Read_Excel('data/user.xls',1)

@ddt
class Regist_New_User(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
    
    def setUp(self):
        self.driver.get('http://39.107.96.138:3000/signup')

    def tearDown(self):
        self.driver.delete_all_cookies()
        time_png = strftime("%Y_%m_%d_%H_%M_%S", localtime())
        name = __name__ + time_png
        screenShotFile = os.path.join(Util.getScreenShotsPath(),name+'.png')
        self.driver.save_screenshot(screenShotFile)

    # @file_data('../../data/registdata.json')  #读取json数据
    @data(*excel_data.get_excel_data())
    @unpack
    def test_regist(self,user_name,pwd,re_pwd,email_address,status,message):
        # logger.debug('test_regist_success')
        # user_name = "user" + str(random.randint(200,200000))
        # pwd = '123456'
        # re_pwd = '123456'
        # email_address = str(random.randint(200,200000)) + '@qq.com'
        new_regist = RegistPage(self.driver)

        #输入用户名
        new_regist.input_username(user_name)
        #输入密码
        new_regist.input_password(pwd)
        #再次输入密码
        new_regist.input_re_password(re_pwd)
        #输入email
        new_regist.input_email(email_address)
        #点击注册按钮
        new_regist.click_regist_button()

        #验证结果
        txt = new_regist.get_regist_result(status)
        self.assertEqual(txt,message,'提示信息错误')

    # def test_regist_repass_false(self):
    #     user_name = "user100"
    #     pwd = '123456'
    #     re_pwd = '1234567'
    #     email_address = '11112211@qq.com'
    #     new_regist = RegistPage(self.driver)
        
    #     #输入用户名
    #     new_regist.input_username(user_name)
    #     #输入密码
    #     new_regist.input_password(pwd)
    #     #再次输入密码
    #     new_regist.input_re_password(re_pwd)
    #     #输入email
    #     new_regist.input_email(email_address)
    #     #点击注册按钮
    #     new_regist.click_regist_button()

    #     #验证结果
    #     txt = new_regist.get_regist_result(False)
    #     self.assertIn('两次密码输入不一致。',txt , '提示信息错误')


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
