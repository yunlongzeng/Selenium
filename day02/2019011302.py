from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get('https://login.zhipin.com/?ka=header-login')

ele = driver.find_element_by_css_selector('form>div:nth-child(4) div.nc_scale')
action = ActionChains(driver)
action.click_and_hold(ele).move_by_offset(324,0).perform()

