#导入selenium包
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="./chromedriver.exe")
driver.get("https://www.baidu.com/")
# driver.get("http://39.107.96.138:3000/signin")

#登录
# driver.find_element_by_id("name").send_keys("user19")
# driver.find_element_by_id("pass").send_keys("123456")
# driver.find_element_by_class_name("span-primary").click()

#点击页面上方功能模块按钮
# eles = driver.find_elements_by_css_selector("body > div.navbar > div > div > ul > li")
# for ele in eles:
#     print(ele.text)
# for i in range(1,len(eles)+1):
#     ele = driver.find_element_by_css_selector("body > div.navbar > div > div > ul > li:nth-child(" + str(i) + ") > a")
#     ele.click()

#发布话题
# driver.find_element_by_xpath('//*[@id="create_topic_btn"]/span').click()
# driver.find_element_by_css_selector('#tab-value > option:nth-child(2)').click()
# driver.find_element_by_id("title").send_keys('Ivon test selenium')
# #actionchains 相关操作，主要是模拟手点操作
# ele_info = driver.find_element_by_class_name("CodeMirror-scroll")
# ActionChains(driver).move_to_element(ele_info).click().send_keys("哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈").perform()
#提交
# driver.find_element_by_xpath('//*[@id="create_topic_form"]/fieldset/div/div/div[4]/input').click()


#元素定位8种方式
# se_input = driver.find_element_by_id("kw") # 1.id定位，id是当前页面唯一属性，定位精准
# se_input = driver.find_element_by_name("wd") # 2.name定位，一定要确保第一个元素是要找的元素
# se_input = driver.find_element_by_tag_name("input") # 3.tag name定位,此方法不适用，因为tag name很难是唯一的
# se_input = driver.find_element_by_class_name("s_ipt") # 4.class name定位
# link = driver.find_element_by_link_text("新闻") # 5.link text定位
# link =driver.find_element_by_partial_link_text("新") # 6.partial link text定位，与link text相似，不同就是link text需要输入全部text
# se_input = driver.find_element_by_xpath('//*[@id="kw"]') #7.xpath定位
# se_input = driver.find_element_by_css_selector('#kw') #8.css定位

# link.click()
# se_input.send_keys("你好")
# driver.quit()  #退出驱动及与之关联的窗口
#driver.close() #退出当前浏览器窗口

#百度上传照片
# driver.find_element_by_xpath('//*[@class="soutu-btn"]').click()
# driver.find_element_by_xpath('//*[@id="form"]/div/div[2]/div[2]/input').send_keys(r'E:\Python\前端开发\html\images\001.jpg')

#使用键盘输入
se_input = driver.find_element_by_css_selector('#kw')
se_input.send_keys("你好")
driver.find_element_by_id('su').send_keys(Keys.ENTER)