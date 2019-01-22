from selenium.webdriver.common.by import By

class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    GO_BUTTON = (By.ID, 'submit')
    INPUT_BOX = (By.ID,'name')
    PASSWORD_BOX = (By.ID,'pass')
    LOGIN_BUTTON = (By.CLASS_NAME,'span-primary')
    REGISTER_NAME = (By.ID,'loginname')
    REPASS_BOX = (By.ID,'re_pass')
    EMAIL_BOX = (By.ID,'email')
    REGISTER_BUTTON = (By.CLASS_NAME,'span-primary')

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass