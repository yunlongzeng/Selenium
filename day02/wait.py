from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://login.live.com/login.srf?wa=wsignin1.0&rpsnv=13&ct=1547383493&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d93a295e3-6c01-e6c6-560f-b26bcff2d142&id=292841&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015")

#隐式等待
# driver.implicitly_wait(10)
#显式等待
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "loginfmt")))
driver.find_element_by_name('loginfmt').send_keys("1231231")