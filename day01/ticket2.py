import requests  
from PIL import Image  
from json import loads  

from requests.packages.urllib3.exceptions import InsecureRequestWarning  
# 禁用安全请求警告  
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)  

headers = {  
            "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36"  
        }  
session = requests.session()  

def getCheckImgIndex():  
        url = "https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand";  
        response = session.get(url=url,headers=headers,verify=False)  
        # 把验证码图片保存到本地  
        f=open('12306.jpg','wb') #也可以是其他任何文件名，图片保存在当前目录下
        f.write(response.content)
        f.close
        img=Image.open('12306.jpg')
        img.show()
        img.close()  #关闭后，不关闭显示图片

        #=======================================================================  
        # 根据打开的图片识别验证码输入图片索引序号，有可以是1张、2张、3张图片的序号，序号之间用逗号隔开
        #例如2，4，6,表示第1排第2，第2排第4,6张
        # ---------------------------------------  
        #         |         |         |  
        #    0    |    1    |    2    |     3  
        #         |         |         |  
        # ---------------------------------------  
        #         |         |         |  
        #    4    |    5    |    6    |     7  
        #         |         |         |  
        # ---------------------------------------  
        #=======================================================================  
        checkindex = input('请输入验证码位置，以","分割（例如2,4,6）:')  
        return checkindex  


#提交验证图片索引位置，并返回验证结果True/False
def postcheckImage(checkindex):  
        # 分割用户输入的验证码位置  
        indexs = checkindex.split(',')  
        # 由于12306官方验证码是验证正确验证码的坐标范围,我们取每个验证码中点的坐标(大约值)  
        imgcentor_position = ['35,35','105,35','175,35','245,35','35,105','105,105','175,105','245,105']  
        checkokList = []  #例如得到：['175,35', '35,105', '175,105']
        for index in indexs:  
            checkokList.append(imgcentor_position[int(index)])  
        # 正确验证码的坐标拼接成字符串，作为网络请求时的参数  
        checkokImgStr = ','.join(checkokList)  #生成的数据例如：175,35,35,105,175,105
        checkUrl = "https://kyfw.12306.cn/passport/captcha/captcha-check"  
        data = {  
            'login_site':'E',           #固定的  
            'rand':'sjrand',            #固定的  
            'answer':checkokImgStr    #验证码对应的中心坐标字符串序号，例如175,35,35,105,175,105  
        }  
        # 发送验证  
        response = session.post(url=checkUrl,data=data,headers=headers,verify=False)  
        # 返回json格式的字符串，用json模块解析 -->dict 
        checkResult = loads(response.content) 
        print(checkResult)
        checkcode = checkResult['result_code']  
        print(checkcode,type(checkcode)) #数字类型的字符串
        # 取出验证结果，4：成功  5：验证失败  7：过期  
        if checkcode == '4':  
            print('验证码提交成功！')  
            return True  
        else:  
            print('验证码提交失败！')  
            return False       

def login12306():
        #输入用户名
        username = input('用户名:')  
        # 输入密码
        password = input('密码:')  
        loginUrl = "https://kyfw.12306.cn/passport/web/login"  
        data = {  
            'username':username,  
            'password':password,  
            'appid':'otn'  #固定的标志
        }  
        response = session.post(url=loginUrl,data=data,headers=headers,verify=False)  
        result = loads(response.content)  
        print (result)
        isLoginOK = result['result_message']  
        # 结果的编码方式是Unicode编码，所以对比的时候字符串前面加u,或者mes.encode('utf-8') == '登录成功'进行判断，否则报错  
        if isLoginOK == '登录成功':  
            print ('登录成功，可以购票!')
        else:  
            print ('登录失败!' )      




if __name__ == '__main__':  
      imgindex=getCheckImgIndex()  
      check=postcheckImage(imgindex)  
      login12306() 
'''      
#输出结果如下
      请输入验证码位置，以","分割[例如2,5]:0,3
{'result_message': '验证码校验成功', 'result_code': '4'}
4 <class 'str'>
验证码提交成功！

用户名:xxxx(在此输入你的用户id)

密码:yyyy(在此输入的登录密码)
{'result_message': '登录成功', 'result_code': 0, 'uamtk': '0gFZ3cDiqqy2UuG0310dDMFyW0uMHHNnJ84KoAbcb2b0'}
登录成功，可以购票!
'''
--------------------- 
作者：isscollege 
来源：CSDN 
原文：https://blog.csdn.net/isscollege/article/details/80776022 
版权声明：本文为博主原创文章，转载请附上博文链接！