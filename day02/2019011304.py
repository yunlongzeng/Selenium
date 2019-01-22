from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.12306.cn/index/index.html")

date = "2019-02-11"
js = 'document.querySelector("#train_date").value = "{}"'.format(date)

driver.execute_script(js)

