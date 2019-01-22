
from selenium.webdriver.common.by import By
from po.registPageLocator import RegistPageLocator

class RegistPage(object):

    def __init__(self,driver):
        self.driver = driver

    def input_username(self,username):
        ele = self.driver.find_element(*RegistPageLocator.USERNAME)
        ele.clear()
        ele.send_keys(username)

    def input_password(self,password):
        ele = self.driver.find_element(*RegistPageLocator.PASSWORD)
        ele.clear()
        ele.send_keys(password)

    def input_re_password(self,re_password):
        ele = self.driver.find_element(*RegistPageLocator.RE_PASSWORD)
        ele.clear()
        ele.send_keys(re_password)

    def input_email(self,email):
        ele = self.driver.find_element(*RegistPageLocator.EMAIL_BOX)
        ele.clear()
        ele.send_keys(email)

    def click_regist_button(self):
        ele = self.driver.find_element(*RegistPageLocator.REGIST_BUTTON)
        ele.click()
    

    def get_regist_result(self,expect_status):
        if expect_status == True:
            login_success_message_text = self.driver.find_element(*RegistPageLocator.SUCCESS_TEXT).text
            return login_success_message_text
        else:
            login_fail_message_text = self.driver.find_element(*RegistPageLocator.FAIL_TEXT).text
            return login_fail_message_text