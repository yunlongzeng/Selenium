import unittest
from selenium import webdriver
import page

class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()              

    def test_login(self):
        """
        登录操作，验证url及用户名出现
        """
        #打开登录网页
        self.driver.get("http://39.107.96.138:3000/signin")
        #Load the main page. In this case the home page of cnode.
        #实例化一个Mainpage对象
        main_page = page.MainPage(self.driver)
        username = "user19"
        pwd = '123456'
        #输入用户名
        main_page.input_username(username)
        #输入密码
        main_page.input_password(pwd)
        #点击登录按钮
        main_page.click_login_button()

        #Checks if the word "Node" is in title
        assert main_page.is_title_matches(), "cNode title doesn't match."

        #验证页面是否显示username
        search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
        assert search_results_page.is_results_found(username), "No results found."

    def test_register_user(self):
        driver = self.driver
        driver.get('http://39.107.96.138:3000/signup')
        
        #实例化一个Mainpage对象
        main_page = page.MainPage(self.driver)
        username = "user19"
        pwd = '123456'
        email = '11111222@qq.com'
        #输入注册用户名
        main_page.input_register_name(username)
        #输入密码
        main_page.input_password(pwd)
        #输入确认密码
        main_page.input_repass_name(pwd)
        #输入邮箱
        main_page.input_email(email)
        #点击注册按钮
        main_page.click_register_button()

        #验证页面是否显示"欢迎加入 Nodeclub！我们已给您的注册邮箱发送了一封邮件，请点击里面的链接来激活您的帐号"
        search_results_page = page.SearchResultsPage(self.driver)
        text = '我们已给您的注册邮箱发送了一封邮件'
        #Verifies that the results page is not empty
        assert search_results_page.is_results_found(text), "No results found."
        self.driver.delete_all_cookies()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)