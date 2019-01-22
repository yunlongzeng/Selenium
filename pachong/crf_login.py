import re
import requests
import http.cookiejar
from PIL import Image
import time
import json,urllib
 
class Crf_Login():
    

    def __init__(self,headers,url):
        self.headers = headers
        self.url = url
        # 建立一个会话，可以把同一用户的不同请求联系起来；直到会话结束都会自动处理cookies
        self.session = requests.Session()
        # 建立LWPCookieJar实例，可以存Set-Cookie3类型的文件。
        # 而MozillaCookieJar类是存为'/.txt'格式的文件
        self.session.cookies = http.cookiejar.LWPCookieJar("cookie")
        # 若本地有cookie则不用再post数据了
        try:
            self.session.cookies.load(ignore_discard=True)
        except IOError:
            print('Cookie未加载！')

    def get_xsrf(self):
        """
        获取参数_xsrf
        """       
        response = self.session.get(self.url, headers=self.headers)
        html = response.text
        get_xsrf_pattern = re.compile(r'<meta name="csrf-token" content="(.+?)">')
        self._xsrf = re.findall(get_xsrf_pattern, html)[0]
        # print(_xsrf)
        return self._xsrf
    
    def login(self):
        text_xsrf = self.get_xsrf()
        print(text_xsrf)
        self.data = {
                    '_csrf': text_xsrf,
                    'LoginForm[username]': "15618926689",
                    'LoginForm[password]': 'nokia111111',
                    'LoginForm[rememberMe]':'0',
                    'show_qr':'0',
                    'login-button':'登 录'
                    }
        
        data=urllib.parse.urlencode(self.data).encode('utf-8')
        result = self.session.post(self.url, data=data, headers=headers)
        # print(result.text)
        print(self.session.cookies)
        self.session.cookies.save(ignore_discard=True, ignore_expires=True)
    
    def run_rearch(self,url):      
        login_code = self.session.get(url, headers=self.headers, allow_redirects=False).status_code
        print(login_code)
        res = self.session.get(url, headers=self.headers)
        print(res.text)

    
    def is_login(self,check_url):
        # 通过查看用户个人信息来判断是否已经登录
        # 禁止重定向，否则登录失败重定向到首页也是响应200
        login_code = self.session.get(check_url, headers=headers, allow_redirects=False).status_code
        if login_code == 200:
            return True
        else:
            return False

 
if __name__ == '__main__':
    headers = {
            "Host" : "home.51cto.com",
            # "Connection":"keep-alive",
            # "Content-Length":"209",
            # "Cache-Control":"max-age=0",
            "Origin" : "http://home.51cto.com",
            # "Upgrade-Insecure-Requests":"1",
            "Content-Type":"application/x-www-form-urlencoded",
            "Referer" : "http://home.51cto.com/index/?reback=http%3A%2F%2Fedu.51cto.com%2Fcenter%2Fuser%2Findex%2Flogin-success%3Fsign%3D1bb6BgMIVQcCVVZVBAMHBlFQClRSAlZcVwEKVgxdQRJGR1d3FgojEgAjAwFBTwVSU0ZdHwZfX0BWcVAGW0FQFBNQIkFWUgpVF1cgFUYOXQxEW11fQAJ0DApTVhsQBnMWXwwUV1oJB1UE%26client%3Dweb",
            "User-Agent" : "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
            "Accept-Language" : "zh-CN,zh;q=0.9"
              }

# 建立LWPCookieJar实例，可以存Set-Cookie3类型的文件。
# 而MozillaCookieJar类是存为'/.txt'格式的文件
    url = r"http://home.51cto.com/index/?reback=http%3A%2F%2Fedu.51cto.com%2Fcenter%2Fuser%2Findex%2Flogin-success%3Fsign%3D1bb6BgMIVQcCVVZVBAMHBlFQClRSAlZcVwEKVgxdQRJGR1d3FgojEgAjAwFBTwVSU0ZdHwZfX0BWcVAGW0FQFBNQIkFWUgpVF1cgFUYOXQxEW11fQAJ0DApTVhsQBnMWXwwUV1oJB1UE%26client%3Dweb"
    check_url = "http://home.51cto.com/msg/inbox"
    search_url = "http://home.51cto.com/msg/inbox"

    login = Crf_Login(headers,url)
    if login.is_login(check_url):
        print('您已经登录')
        login.run_rearch(search_url)
    else:
        login.login()
        login.run_rearch(search_url)
    