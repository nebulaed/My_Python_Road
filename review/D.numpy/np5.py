# numpy索引

import numpy as np 

A = np.arange(3,15).reshape((3,4))
print (A[2]) # 输出第3行
print (A[2][1]) # 输出第3行第2列，可用冒号来表示所有的变量
# numpy支持A[2,1]与A[2][1]，python自己的数组、元组、字符串等均不支持A[2,1]
print (A[2][1:2]) # :左闭右开

for row in A:
    print (row) # print出每一行的数

for column in A.T: # print出每一列的数，numpy中没有直接实现该功能的方法故必须使用技巧转置
    print(column)

print(A)
print(A.flatten())
for item in A.flat: # A.flatten()就是把矩阵平铺成行向量,A.flat是一个函数，可以把矩阵平铺成一堆值
    print (item) # 把其中的每一项print出来
