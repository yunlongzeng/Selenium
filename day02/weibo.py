from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import xlwt

driver = webdriver.Chrome()
driver.implicitly_wait(10)  #隐式等待
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


wb = xlwt.Workbook()
ws = wb.add_sheet('Web 自动化')
ws.write(0,0,"作者")
ws.write(0,1,"主题")
ws.write(0,2,"日期")
ws.write(0,3,"收藏")
ws.write(0,4,"转发")
ws.write(0,5,"评论")
ws.write(0,6,"点赞")

i = 1

for x in range(5):
    eles = driver.find_elements_by_css_selector("#pl_feedlist_index > div:nth-child(2) > .card-wrap")
    for ele in eles:
        author = ele.find_element_by_css_selector(".name").text
        title = ele.find_element_by_css_selector(".txt").text
        date = ele.find_element_by_xpath('.//*[@class="from"]/a[1]').text
        shoucang = ele.find_element_by_xpath('.//*[@class="card-act"]/ul/li[1]').text.split("收藏")[1] or 0  #没有的话输出0
        zhuanfa = ele.find_element_by_xpath('.//*[@class="card-act"]/ul/li[2]').text.split("转发")[1] or 0  #没有的话输出0
        pinglun = ele.find_element_by_xpath('.//*[@class="card-act"]/ul/li[3]').text.split("评论")[1] or 0  #没有的话输出0
        zan = ele.find_element_by_xpath('.//*[@class="card-act"]/ul/li[4]').text or 0  #没有的话输出0
    
        ws.write(i,0,author)
        ws.write(i,1,title)
        ws.write(i,2,date)
        ws.write(i,3,shoucang)
        ws.write(i,4,zhuanfa)
        ws.write(i,5,pinglun)
        ws.write(i,6,zan)
        i += 1
    driver.find_element_by_xpath('//*[contains(@class,"next")]').click()
wb.save('微博.xls')