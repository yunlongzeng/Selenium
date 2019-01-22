
from selenium.webdriver.common.by import By
class RegistPageLocator(object):
    USERNAME=(By.ID,'loginname')
    PASSWORD=(By.ID,"pass")
    RE_PASSWORD = (By.ID,'re_pass')
    EMAIL_BOX = (By.ID,'email')
    REGIST_BUTTON = (By.CSS_SELECTOR,'.span-primary')

    SUCCESS_TEXT = (By.CSS_SELECTOR,'.inner>div>strong')
    FAIL_TEXT = (By.CSS_SELECTOR,'.inner > div >strong')
