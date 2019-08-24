# Pandas合并concat

import pandas as pd
import numpy as np

# concatenating
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*2, columns=['a','b','c','d'])

res = pd.concat([df1,df2,df3],axis=0,ignore_index=True) # axis=0表示纵向合并
# 若没有ignore_index=True，打印出来会是行标会是0,1,2,0,1,2,0,1,2，现在是进行了重新排序，变成了0,1,2,3,4,5,6,7,8
print(res,'\n')

# join, ['inner','outer']

df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'], index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d','e'], index=[2,3,4])

print(df1,'\n')
print(df2,'\n')
res1 = pd.concat([df1,df2]) # 默认填充方式为'outer'，若两个合并的DataFrame中有一个有另外一个没有的部分会填充NaN
print (res1,'\n')
res2 = pd.concat([df1,df2], join='inner', ignore_index=True) # 砍掉并非两者都有的部分，同时利用ignore_index处理序号 
print(res2,'\n')

# join_axes
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'], index=[1,2,3])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['b','c','d','e'], index=[2,3,4])
res3 = pd.concat([df1,df2], axis=1, join_axes=[df1.index]) # 按照df1的行号进行合并，若df2中没有df1中有的行，合并后会填充NaN，若没有给定join_axes则双方没有对方的部分都填充NaN
print(res3,'\n')

# append
df1 = pd.DataFrame(np.ones((3,4))*0, columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
df3 = pd.DataFrame(np.ones((3,4))*1, columns=['a','b','c','d'])
res4 = df1.append(df2,ignore_index=True)
res5 = df1.append([df2,df3], ignore_index=True)
s1 = pd.Series([1,2,3,4], index=['a','b','c','d'])
res6 = df1.append(s1,ignore_index=True)
print(res4,'\n')
print(res5,'\n')
print(res6,'\n')
