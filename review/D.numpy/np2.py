# numpy创建array

import numpy as np

a = np.array([2,23,4],dtype=np.int)
print(a.dtype) # 输出a的类型

b = np.zeros((3,4))
print(b)

c = np.arange(12).reshape((3,4)) # 生成一个3行4列，从0到11的数列
print(c)

d = np.linspace(1,10,20) # 生成一个19段(20个节点)，从1到10的数列，想更改数组形状仍可使用reshape
print(d)

e = np.empty((3,4)) # 一堆几乎为0的数
print(e)
