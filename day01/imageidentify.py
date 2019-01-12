import requests,sys,base64
import ssl,time,re
from selenium import webdriver
from PIL import Image  

ssl._create_default_https_context = ssl._create_unverified_context
#获取图片保存至本地
driver = webdriver.Chrome()
driver.get("https://kyfw.12306.cn/otn/login/init")
time.sleep(2)
# driver.find_element_by_xpath('//*[@id="loginForm"]/div/ul[2]/li[4]/div/div/div[3]/img').screenshot("./12306.png")
driver.save_screenshot("./full_screenshot.png")
#裁剪文字图片
im = Image.open("./full_screenshot.png")
x = 500
y = 340
w = 100
h = 40
region = im.crop((x, y, x+w, y+h))
region.save("./12306.png")
#裁剪图像图片
im_2 = Image.open("./full_screenshot.png")
x_2 = 350
y_2 = 380
w_2 = 380
h_2 = 200
region_2 = im_2.crop((x_2, y_2, x_2+w_2, y_2+h_2))
region_2.save("./image.png")
# html = driver.page_source
# 创建正则表达式规则对象，匹配每页里的段子内容，re.S 表示匹配全部字符串内容
# pattern = re.compile('<img class="touclick-image" alt="" src="(.+?)"', re.S)
# 将正则匹配对象应用到html源码字符串里，返回这个页面里的所有段子的列表
# content_list = pattern.findall(html)
# session = requests.session()
# response = session.get(url=content_list[0],verify=False)  
# 把验证码图片保存到本地  
# f=open('./12306.png','wb') #也可以是其他任何文件名，图片保存在当前目录下
# f.write(response.content)
# f.close
# print(content_list)

#获取文字识别token
# client_id 为官网获取的AK， client_secret 为官网获取的SK
client_id = "nEA17QNtUIr3DptjaX892fg7"
client_secret = "6zklMaTeEPeGUuenE2eDdEo5BGOhqBWI"
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={0}&client_secret={1}'.format(client_id,client_secret)
# print(host)
request = requests.get(host)
r = request.json()
# print(r)
access_token = r["access_token"]
print(access_token)

#获取图像识别token
# client_id 为官网获取的AK， client_secret 为官网获取的SK
client_id_2 = "Lefovyj34BsK5GnGAABVKaBW"
client_secret_2 = "3ki7VdtKuF5LNLW5HofurAGrOdkik3Fd"
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={0}&client_secret={1}'.format(client_id_2,client_secret_2)
# print(host)
request_2 = requests.get(host)
r = request_2.json()
# print(r)
access_token_2 = r["access_token"]
print(access_token_2)


# 处理文字图片
url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/general?access_token=' + access_token
# 二进制方式打开图文件
f = open(r'./12306.png', 'rb')
# 参数image：图像base64编码
img = base64.b64encode(f.read())
params = {"image": img}
image_response = requests.post(url,data = params)
image_info = image_response.json()
print(image_info)

# 处理主体图像图片
url_2 = 'https://aip.baidubce.com/rest/2.0/image-classify/v2/advanced_general?access_token=' + access_token_2
# 二进制方式打开图文件
f_2 = open(r'./image.png', 'rb')
# 参数image：图像base64编码
img_2 = base64.b64encode(f_2.read())
params_2 = {"image": img_2}
image_response_2 = requests.post(url_2,data = params_2)
image_info_2 = image_response_2.json()
print(image_info_2)