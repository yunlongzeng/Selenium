from pymysql import *

class MysqlHelper():
    def __init__(self,host,user,password,database,port,charset='utf8'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset

    def open(self):
        self.conn = connect(host=self.host,user=self.user,password=self.password,database=self.database,port=self.port,charset=self.charset)
        self.cur = self.conn.cursor()

    def close(self):
        self.cur.close()
        self.conn.close()

    def carryout(self,sql,param):
        try:
            self.open()
            self.cur.execute(sql,param)
            self.conn.commit()
            self.close()
            print("OK")
        except Exception as e:
            print(e)

    def all(self,sql,param=[]):
        try:
            self.open()
            self.cur.execute(sql,param)
            result = self.cur.fetchall()
            self.close()
            return result
        except Exception as e:
            print(e)