from selenium import webdriver
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()

driver.get('http://39.107.96.138:3000/signin')
driver.find_element_by_id('name').send_keys('user1')
driver.find_element_by_id('pass').send_keys('123456')
driver.find_element_by_css_selector('.span-primary').click()

driver.get('http://39.107.96.138:3000/user/user1')

driver.find_element_by_class_name('topic_title').click()

driver.find_element_by_css_selector('i.fa.fa-lg.fa-trash').click()

print( Alert(driver).text)
#取消
# Alert(driver).dismiss() 
# 确定
Alert(driver).accept() 