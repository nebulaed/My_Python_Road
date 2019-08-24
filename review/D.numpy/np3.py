# numpy基础运算1

import numpy as np
a = np.array([10,20,30,40])
b = np.arange(4)

c=a-b # a里面逐个元素减去b里面逐个元素
d=a+b # 同理
e=a**2 # 同理输出a里面逐个元素的平方

f=10*np.sin(a) # 调用np中的sin函数
print (b<3) # print出b中小于3的，结果是[True,True,True,False]

g=a*b # 逐个相乘(点乘)
g_dot=np.dot(a,b) # 矩阵相乘(叉乘)
g_dot_2=a.dot(b) # 与上一行效果相同     

h = np.random.random((2,4)) # 生成一个2行4列的随机数字矩阵

print(h)
print(np.sum(h)) # 整个矩阵中的数字求和
# print(np.sum(h), axis=1) # axis=1表示对每行求和，axis=0表示对每列求和，以下各函数用法同理
print(np.min(h)) # 输出最小值
print(np.max(h)) # 输出最大值
