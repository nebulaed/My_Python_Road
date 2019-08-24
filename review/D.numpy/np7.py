# numpy array分割

import numpy as np

A = np.arange(12).reshape((3,4))

print(np.split(A,2,axis=1)) # 分割成了两个array，不可以将array分割成不等的几块，只能进行均等的分割

print(np.array_split(A,3,axis=1)) # 可以进行不均等的分割

print(np.vsplit(A,3)) # 简洁的纵向分割，把纵向看成一条线，用刀把线分割开，分割线为横向水平
print(np.hsplit(A,2)) # 简洁的横向分割


