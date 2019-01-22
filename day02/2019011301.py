#导入selenium包
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
# driver.get("https://www.baidu.com/")
driver.get("http://39.107.96.138:3000/signin")

#登录
driver.find_element_by_id("name").send_keys("user19")
driver.find_element_by_id("pass").send_keys("123456")
driver.find_element_by_class_name("span-primary").click()

#发布话题
driver.find_element_by_xpath('//*[@id="create_topic_btn"]/span').click()
driver.find_element_by_css_selector('#tab-value > option:nth-child(2)').click()

#快捷键操作
ele = driver.find_element_by_xpath('//*[@id="create_topic_form"]/fieldset/div/div/div[2]/div[6]')
action = ActionChains(driver)
action.move_to_element(ele).click().send_keys("hahahha")
action.key_down(Keys.CONTROL).send_keys('a')
action.key_up(Keys.CONTROL)
action.key_down(Keys.CONTROL).send_keys('b')
action.key_up(Keys.CONTROL).perform()

#上传照片
driver.find_element_by_id("title").send_keys('Ivon test selenium')
driver.find_element_by_xpath('//*[@id="create_topic_form"]/fieldset/div/div/div[1]/a[7]').click()
time.sleep(2)
driver.find_element_by_css_selector('.webuploader-element-invisible').send_keys(r"E:\vb\Selenium\day02\test.PNG")
