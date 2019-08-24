# Pandas处理丢失数据

import pandas as pd
import numpy as np

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)),index=dates, columns=['A','B','C','D'])

df.iloc[0,1]=np.nan
df.iloc[1,2]=np.nan

print(df.dropna(axis=0,how='any')) # axis=0表示对列进行操作，丢掉有nan的行, how='any'表示只要有一个nan就丢掉，how='all'表示只有全部为Nan才丢掉
print(df.fillna(value=0)) # 把nan填充为0

print(df.isnull()) # 检查矩阵所有地方是否有nan

print(np.any(df.isnull())==True) # 检查矩阵中是否有至少一个nan，有则返回True，这里可以删掉==True，因为返回的值本身就是True or False



