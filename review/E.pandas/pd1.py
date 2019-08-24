# pandas基本介绍

import pandas as pd
import numpy as np
s = pd.Series([1,3,6,np.nan,44,1])
print (s) # 一般dtype为float64

dates = pd.date_range('20160101',periods=6) # 从2016-01-01到2016-01-06的六天
print(dates)

df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d']) # print出以下的东西
print (df)
"""
                   a         b         c         d
    2016-01-01 -0.253065 -2.071051 -0.640515  0.613663
    2016-01-02 -1.147178  1.532470  0.989255 -0.499761
    2016-01-03  1.221656 -2.390171  1.862914  0.778070
    2016-01-04  1.473877 -0.046419  0.610046  0.204672
    2016-01-05 -1.584752 -0.700592  1.487264 -1.778293
    2016-01-06  0.633675 -1.414157 -0.277066 -0.442545
"""
df1 = pd.DataFrame(np.arange(12).reshape((3,4)))
print (df1) # 自动生成行号和列号

df2 = pd.DataFrame({'A' : 1.,                     'B' : pd.Timestamp('20130102'),                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),                     'D' : np.array([3] * 4,dtype='int32'),                     'E' : pd.Categorical(["test","train","test","train"]),                     'F' : 'foo'})

print(df2.dtypes) # 打印出每一列的数据形式

print(df2.index) # 打印出每一列的标序

print(df2.columns) # 打印出每一行的名字


print(df2.values) # 把每一行的值输出出来

print(df2.describe()) # 只能运算数字形式，输出其各项数据，如数据数目，平均值，方差，最小值，最大值

print(df2.T) # 转置

print(df2.sort_index(axis=1,ascending=False)) # 1对列号进行倒序排序

print(df2.sort_index(axis=0,ascending=False)) # 0对行号进行倒序排序

print (df2.sort_values(by='E')) # 对各行按照E列中的东西进行排序

