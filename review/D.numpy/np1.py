# numpy属性
import numpy as np

array = np.array([[1,2,3],
[2,3,4]])

print(array)
print('number of dim:',array.ndim) # 该数组是几维
print('shape:',array.shape) # 行数多少，列数多少
print('size:',array.size) # 总共有多少元素
