from selenium.webdriver.common.by import By
from po.createTopicPageLocator import  CreateTopicPageLocator
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert

class CreateTopicPage(object):

    def __init__(self,driver):
        self.driver = driver
        self.bankuai_name = ""

    def choose_bankuai(self,bankuai_name):
        if bankuai_name == "share":
            self.bankuai_name = 'share'
            ele = self.driver.find_element(*CreateTopicPageLocator.BANKUAI_SHARE)
            ele.click()
        elif bankuai_name == "ask":
            self.bankuai_name = 'ask'
            ele = self.driver.find_element(*CreateTopicPageLocator.BANKUAI_ASK)
            ele.click()
        elif bankuai_name == "job":
            self.bankuai_name = 'job'
            ele = self.driver.find_element(*CreateTopicPageLocator.BANKUAI_JOB)
            ele.click()

    def input_title(self,title):
        ele = self.driver.find_element(*CreateTopicPageLocator.TITLE)
        ele.send_keys(title)

    def input_text(self,text):
        ele = self.driver.find_element(*CreateTopicPageLocator.TEXT)
        actions = ActionChains(self.driver)
        actions.move_to_element(ele).click().send_keys(text).perform()

    def click_submit_button(self):
        ele = self.driver.find_element(*CreateTopicPageLocator.SUBMIT_BUTTON)
        ele.click()

    def return_result(self,respect_result):
        driver = self.driver
        if respect_result == 'True':
            ele = driver.find_element(*CreateTopicPageLocator.TOPIC_TITLE)
        else:
            if self.bankuai_name == "":
                ele = Alert(driver)
                ele.accept()
                print(ele.text)
            else:
                ele = driver.find_element(*CreateTopicPageLocator.WRONG_MESSAGE_ELE)
        return ele.text
    