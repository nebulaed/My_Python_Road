# Pandas选择数据

import pandas as pd
import numpy as np

dates = pd.date_range('20130101',periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])

print(df['A'],df.A) # 前后两者效果一样
print(df[0:3],df['20130102':'20130104']) # 第一个是2013-01-01到2013-01-03的数字，第二个是2013-01-02到2013-01-04的数据

# select by label: loc

print(df.loc['20130102']) # 由标签进行选择

print(df.loc[:,['A','B']]) # 打印A列、B列所有行的数据

print(df.loc['20130102',['A','B']]) # 打印A列、B列 20130102行的数据

# select by position: iloc
print (df.iloc[3]) # 打印第4行的数据

print(df.iloc[3,1]) # 打印第4行第2列的数据

print(df.iloc[3:5,1:3]) # 切片操作

print(df.iloc[[1,3,5],1:3]) # 逐个不连续地筛选

# mixed selection: ix
print (df.ix[:3,['A','C']]) # 同时利用标签和位置进行筛选
# 在python3.7中ix已被弃用，现在loc已经可以实现标签、位置双筛选

# Boolean indexing
print(df[df.A >8]) # 在A这一列中筛选大于8的部分，将符合条件的行的所有列显示出来

