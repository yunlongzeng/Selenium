from elements import BasePageElement
from locators import MainPageLocators

# class SearchTextElement(BasePageElement):
#     """This class gets the search text from the specified locator"""

#     #The locator for search box where search string is entered
#     locator = 'q'


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. cnode"""
    #Declares a variable that will contain the retrieved text
    # search_text_element = SearchTextElement()

    def input_username(self,username):
        '''
        输入用户名
        '''
        element = self.driver.find_element(*MainPageLocators.INPUT_BOX)
        element.send_keys(username)
    
    def input_password(self,pwd):
        '''
        输入密码
        '''
        element = self.driver.find_element(*MainPageLocators.PASSWORD_BOX)
        element.send_keys(pwd)

    def click_login_button(self):
        '''
        点击登录按钮
        '''
        element = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        element.click()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Node" appears in page title"""
        return "Node" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

    def input_register_name(self,username):
        #  '''
        # 输入注册用户名
        # '''
        element = self.driver.find_element(*MainPageLocators.REGISTER_NAME)
        element.send_keys(username)

    def input_repass_name(self,pwd):
        #  '''
        # 输入注册用户名
        # '''
        element = self.driver.find_element(*MainPageLocators.REPASS_BOX)
        element.send_keys(pwd)
    
    def input_email(self,email):
        '''
        输入邮箱
        '''
        element = self.driver.find_element(*MainPageLocators.EMAIL_BOX)
        element.send_keys(email)

    
    def click_register_button(self):
        '''
        点击注册按钮
        '''
        element = self.driver.find_element(*MainPageLocators.REGISTER_BUTTON)
        element.click()


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self,appear_elements):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        # print(self.driver.page_source)
        return appear_elements in self.driver.page_source