# Pandas合并merge

# 用merge的好处是相同的key可以合并内容
import pandas as pd
import numpy as np
# merging two df by key/keys. (may be used in database)
# simple example
left = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']}) 
right = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']})

print(left,'\n')
print(right,'\n')

res = pd.merge(left,right,on='key')
print(res,'\n')

# consider two keys
left = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
    'key2': ['K0','K1','K0','K1'],
    'A': ['A0', 'A1', 'A2', 'A3'],
    'B': ['B0', 'B1', 'B2', 'B3']})
right = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
    'key2':['K0','K0','K0','K0'],
    'C': ['C0', 'C1', 'C2', 'C3'],
    'D': ['D0', 'D1', 'D2', 'D3']})

print(left,'\n')
print(right,'\n')

res = pd.merge(left,right,on=['key1','key2']) # 根据key1,key2进行合并，默认合并方式为inner

print(res,'\n')

# how = ['left','right','outer','inner']
res2 = pd.merge(left,right,on=['key1','key2'],how='outer')

print(res2,'\n')
# 若采用'left','right'则分别根据left,right进行填充

# indicator
df1 = pd.DataFrame({'col1':[0,1], 'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
print(df1,'\n')
print(df2,'\n')

res3 = pd.merge(df1,df2,on='col1',how='outer',indicator=True) # 增加一个标签直观地显示merge合成是如何合成的
# indicator=True会在答案给出每一行merge时是如何merge的，数据是来自左还是右
print(res3,'\n')

# give the indicator a custom name
res4 = pd.merge(df1,df2,on='col1',how='outer',indicator='indicator_column')
print(res4,'\n')

# merged by index
left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']},
    index=['K0', 'K1', 'K2'])
right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
    'D': ['D0', 'D2', 'D3']},
    index=['K0', 'K2', 'K3'])

print(left,'\n')
print(right,'\n')

# left_index and right_index
res = pd.merge(left,right, left_index=True, right_index=True, how='outer')
print (res,'\n')

# handle overlapping
boys = pd.DataFrame({'k':['K0','K1','K2'], 'age': [1,2,3]})
print(boys,'\n')
girls = pd.DataFrame({'k':['K0','K1','K2'], 'age': [4,5,6]})
print(girls,'\n')

res = pd.merge(boys, girls, on='k', suffixes=['_boy','_girl'], how='inner') # suffixes为后缀
print(res,'\n')

# join的使用方法和merge相近
