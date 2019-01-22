from urllib.request import urlopen 
import urllib,json
from http import cookiejar
import http.cookiejar as cookielib

class Login_Url():
	def __init__(self,url,data,cookie_file):
		self.url = url
		self.data = data
		# 1). 设置保存cookie的文件名
		self.cookieFilename = cookie_file
		#self.ck_opener = ""
		
	def get_new_cookie(self):
		#print("00")
		# 通过CookieJar()类构建一个cookieJar()对象，用来保存cookie的值
		# 2). 声明一个MozillaCookie,用来保存cookie并且可以写入文进阿
		cookiejar_1 = cookiejar.MozillaCookieJar(filename=self.cookieFilename)
		postdata=urllib.parse.urlencode(self.data).encode('utf-8')
		req = urllib.request.Request(self.url,data = postdata) 
		response = urlopen(req) 
		handler = urllib.request.HTTPCookieProcessor(cookiejar_1)  #理论上可以不传参数，但是后面无法使用 cookiejar
		self.ck_opener = urllib.request.build_opener(handler)
		resp = self.ck_opener.open(req) 
			
		for i in cookiejar_1:
			print(i)   
		# ignore_discard, 即使cookie信息将要被丢弃。 也要把它保存到文件中;
		# ignore_expires, 如果在文件中的cookie已经存在， 就覆盖原文件写入;
		cookiejar_1.save(ignore_discard=True, ignore_expires=True)

	def read_cookie(self):
		#print("0")
		# 2).声明一个MozillaCookie,用来保存cookie并且可以写入文件， 用来读取文件中的cookie信息
		cookie = cookiejar.MozillaCookieJar()
		# 3). 从文件中读取cookie内容
		#print("1")
		cookie.load(filename=self.cookieFilename)
		# 4). 利用urllib.request的HTTPCookieProcessor创建一个cookie处理器
		#print("2")
		handler = urllib.request.HTTPCookieProcessor(cookie)
		#print("3")
		# 5). 通过CookieHandler创建opener
		# 默认使用的openr就是urlopen;
		self.ck_opener = urllib.request.build_opener(handler)
		#print("4")

	def get_data(self,s_url):
		try:
			self.read_cookie()
			#print("b")
		except:
			#print("a")
			self.get_new_cookie()
		
		#print("c")
		#6). 打开url页面
		response = self.ck_opener.open(s_url)
		#7). 打印信息
		print(response.read().decode('utf-8'))
		#print("d")
		
if __name__ == "__main__":
	url = "http://39.107.96.138:3000/signin"
	data = {
		"name":"user19",
		"pass":"123456",
		}		
	cookieFilename = 'cookie.txt'
	s_url = "http://39.107.96.138:3000/my/messages"
	
	login = Login_Url(url,data,cookieFilename)
	login.get_data(s_url)
# https://blog.csdn.net/zcx1203/article/details/83098632

