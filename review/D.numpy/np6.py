# numpy array合并

import numpy as np

A = np.array([1,1,1])
B = np.array([2,2,2])

C = np.vstack((A,B)) # vertical合并array
D = np.hstack((A,B)) # horizontal合并array

print (A.shape,C.shape) 
print (A.shape,D.shape)

# 注意：不能通过A.T来将行向量转成列向量，因为原向量是一维的，没有纵向，这与二维向量只有一行不同

# 或者直接reshape
print(A[:,np.newaxis]) # 给numpy增加了一个新的维度，原维度行变为列(被挤到第二个维度了)

A = A[:,np.newaxis]
B = B[:,np.newaxis]
E = np.concatenate((A,B,B,A),axis=0) # 采用concatenate可以选择在哪个维度进行合并
print(E)
