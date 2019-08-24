# numpy基础运算2

import numpy as np
A = np.arange(2,14).reshape((3,4)) # [2 3 4 5 6 7 8 9 10 11 12 13]

print(np.argmin(A)) # 输出A中最小值的索引
print(np.argmax(A)) # 输出A中最大值的索引
print(np.mean(A)) # 输出A的平均值
print(A.mean()) # 同上行
print(np.median(A)) # 输出A的中位数
print(np.cumsum(A)) # 输出A每一位的累加，此处为[2 5 9 14 20 27 35 44 54 65 77 90]
print(np.diff(A)) # 输出每两个数间的差
print(np.nonzero(A)) # 输出A中非零数的行和列，行和列分开在两个数列中

print(np.sort(A)) # 逐行进行排序
print(np.transpose(A)) # 转置
print(A.T) # 效果同上行

print(np.clip(A,5,9)) # 所有大于9的数都变成9，所有小于5的数都变成5

# 这些操作基本上都可以指定行和列

print(np.mean(A,axis=1)) # 算出每一行的平均值，axis=0时为每一列的平均值
