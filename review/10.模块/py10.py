# import模块
from time import time,localtime
# from time import * # 从time模块中import所有函数，可直接使用函数，但易引起不同模块中的同名函数重复
#import time
#print(time.localtime())

print(time())
print(localtime())

# 自己的模块
def printdata(data):
    print(data)
