from selenium.webdriver.common.by import By
class CreateTopicPageLocator(object):
    BANKUAI_SHARE=(By.CSS_SELECTOR,'#tab-value>option:nth-child(2)')
    BANKUAI_ASK=(By.CSS_SELECTOR,'#tab-value>option:nth-child(3)')
    BANKUAI_JOB=(By.CSS_SELECTOR,'#tab-value>option:nth-child(4)')
    TITLE=(By.ID,"title")
    TEXT = (By.CSS_SELECTOR,'.CodeMirror-code>pre')
    SUBMIT_BUTTON = (By.CSS_SELECTOR,'.editor_buttons>input')
    TOPIC_TITLE = (By.CSS_SELECTOR,'.topic_full_title')
    WRONG_MESSAGE_ELE = (By.CSS_SELECTOR,'.alert>strong')