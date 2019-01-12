from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
# driver.implicitly_wait(10)  #隐式等待
driver.get("https://weibo.com/")
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "weibo_top_public"))  #显示等待
    )
finally:
    driver.find_element_by_css_selector(".gn_search_v2>input").send_keys("Web自动化")
    
driver.find_element_by_css_selector(".gn_search_v2>a").click()
driver.find_element_by_link_text("高级搜索").click()
driver.find_element_by_xpath('//*[@id="radio03"]').click()
driver.find_element_by_link_text("搜索微博").click()
eles = driver.find_elements_by_css_selector("#pl_feedlist_index > div:nth-child(2) > .card-wrap")

i = 1
for ele in eles:
    title = ele.find_element_by_css_selector(".txt").text
    title = "%s%s%s%s"%("title",i," = ",title)
    print(title)
    i += 1