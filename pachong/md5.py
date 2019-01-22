import hashlib
m = hashlib.md5()  #创建hash对象
print(m)  
m.update("nokia111111".encode("utf-8")) #更新哈希对象以字符串参数
print(m.hexdigest())  #返回十六进制数字字符串