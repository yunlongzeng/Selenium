# from selenium import webdriver
from urllib.request import urlopen
import urllib
import ssl,time,json
from urllib.parse import quote
# import requests

ssl._create_default_https_context = ssl._create_unverified_context


def login():
    driver = webdriver.Chrome()
    #打开12306登录网址
    driver.get("https://kyfw.12306.cn/otn/login/init")
    #输入登录名及密码
    driver.find_element_by_id("username").send_keys("15618926689")
    driver.find_element_by_id("password").send_keys("nokia111111")
    while driver.current_url == "https://kyfw.12306.cn/otn/login/init" or driver.current_url == "https://kyfw.12306.cn/otn/login/init#":
        time.sleep(0.1)
    print("验证完成！")
    #获取cookie
    cookie = [item["name"] + "=" + item["value"] for item in driver.get_cookies()] 
    cookiestr = ';'.join(item for item in cookie) 
    print(cookiestr)
    return cookiestr

def search_ticket():
    #查询火车票信息
    #获取查询的url
    start_station = "上海"    #出发城市
    start_station = quote(start_station,encoding = 'UTF-8') + ",SHH"
    des_station = "长沙"      #到达城市
    des_station = quote(des_station,encoding = 'UTF-8') + ",CSQ"
    start_date = "2019-01-16"    #出发时间
    search_url = r"https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs={0}&ts={1}&date={2}&flag=N,N,Y".format(start_station,des_station,start_date)
    print(search_url)
    ua_headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        # "cookie":cookie
    }
    req = urllib.request.Request(search_url,headers = ua_headers)
    response = urlopen(req)
    # read()方法就是读取文件里的全部内容，返回字符串s
    html = response.read().decode("UTF-8")   
    # raw_trains = html.json()['data']['result']
    # 返回 HTTP的响应码，成功返回200，4服务器页面出错，5服务器问题
    print("返回的状态码："+str(response.getcode()))
    print(html)

def search_ticket1():
    #查询火车票信息
    #获取查询的url
    start_station = "上海"    #出发城市
    start_station = quote(start_station,encoding = 'UTF-8') + ",SHH"
    des_station = "长沙"      #到达城市
    des_station = quote(des_station,encoding = 'UTF-8') + ",CSQ"
    start_date = "2019-01-16"    #出发时间
    search_url = r"https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs={0}&ts={1}&date={2}&flag=N,N,Y".format(start_station,des_station,start_date)
    print(search_url)
    ua_headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
        # "cookie":cookie
    }
    r = requests.get(search_url, verify=False)
    # read()方法就是读取文件里的全部内容，返回字符串s  
    print(r.content)

def search_ticket2():
    search_url = r"https://blog.csdn.net/memory_qianxiao/article/details/81944732"
    print(search_url)

    req = urllib.request.Request(search_url)
    response = urlopen(req)
    # read()方法就是读取文件里的全部内容，返回字符串s
    html = response.read().decode("UTF-8")   
   
     # read()方法就是读取文件里的全部内容，返回字符串s  
    # raw_trains = r.json()['data']['result']
    print(html)

if __name__ == "__main__":
    search_ticket()
