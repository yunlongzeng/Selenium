from MysqlHelper import *
from hashlib import sha1

class Login_Check(object):
     
    def __init__(self,host,user,pwd,database,port,charset):
        '''
        host填写主机ip地址，user指账户名，pwd指服务器密码，database指数据库名，port一般是3306，charset一般是utf8
        '''
        self.host = host
        self.user = user
        self.pwd = pwd
        self.database = database
        self.port = port
        self.charset = charset

    def get_sha1_password(self,password):
        #获取输入密码的sha1值
        s1 = sha1()
        s1.update(password.encode("utf-8"))
        password = s1.hexdigest()
        return password

    def get_sha1_mysql(self,sql,param):
        #连接数据库，查询数据库sha1加密密码
        mysqltest = MysqlHelper(host=self.host,user=self.user,password=self.pwd,database=self.database,port=self.port,charset=self.charset)       
        ret = mysqltest.all(sql,param)
        return ret

    def exist_check(self,sql,password,param):
        #判断数据库的用户名是否存在，存在的话密码是否相等
        sha1_password = self.get_sha1_password(password)
        # print(sha1_password)
        sha1_mysql = self.get_sha1_mysql(sql,param)
        # print(sha1_mysql)
        if len(sha1_mysql) == 0:
            print("用户名不存在！")
        elif sha1_mysql[0][0] == sha1_password:
            print("密码正确！")
        else:
            print("密码错误！")

if __name__ == "__main__":
    host = '192.168.2.138'
    user = 'root'
    pwd = '111111'
    database = 'inserttable'
    port = 3306             #固定
    charset = 'utf8'        #固定
    
    #获取user输入信息
    user_name = input("请输入学生姓名：")
    password = input("请输入密码：")

    login_check = Login_Check(host,user,pwd,database,port,charset)
    sql = 'select password from users where name=%s'
    param = [user_name]
    login_check.exist_check(sql,password,param)


