from pymysql import *
import random

class Mysql_Create_Data(object):

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

    def run_mysql(self,sqls):
        '''
        sqls指的是mysql语句组，要熟悉表结构；
        '''
        try:
            conn = connect(host=self.host,user=self.user,password=self.pwd,database=self.database,port=self.port,charset=self.charset)
            cursor1 = conn.cursor()
            
            for sql in sqls:
                cursor1.execute(sql)

            conn.commit()
            cursor1.close()
            conn.close()

        except Exception as res:
            print(res)

if __name__ == "__main__":
    host = '192.168.2.138'
    user = 'root'
    pwd = '111111'
    database = 'inserttable'
    port = 3306             #固定
    charset = 'utf8'        #固定

    excute_mysql = Mysql_Create_Data(host,user,pwd,database,port,charset)

    sqls = []
    for i in range(10000):
        age = random.randint(10,50)
        name = random.randint(1,1000)
        sql = "insert into student(name,gender,age) values('{0}',1,{1})".format(name,age)         #增
        sqls.append(sql)
        #sql = 'update students set name="12121" where name="阿三"' #改
        #sql = 'delete from students where name = "12121"'           #删
    
    excute_mysql.run_mysql(sqls)
