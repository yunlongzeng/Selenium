from selenium import webdriver

driver = webdriver.Chrome()

driver.get(r"E:\vb\Selenium\day02.\test.html")

#切换frame
ele = driver.find_element_by_tag_name('iframe')
driver.switch_to_frame(ele)
driver.switch_to_frame('iframeLoginIfm')

driver.find_element_by_css_selector('#pwdTab').click()
driver.find_element_by_css_selector("#pwdUserNameIpt").send_keys("15618926689")