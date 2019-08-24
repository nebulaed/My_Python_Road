# Pandas设置值

import pandas as pd
import numpy as np

dates=pd.date_range('20130101',periods=6)
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])

df.iloc[2,2]=1111
df.loc['20130101','B']=2222
df.A[df.A>4]=0
print(df,'\n') # 只更改A列
df=pd.DataFrame(np.arange(24).reshape((6,4)),index=dates,columns=['A','B','C','D'])
df[df.A>4]=0
print(df,'\n') # 更改所有列
df['F']=np.nan # 给df增加F行，且该行内均为空值
df['E']=pd.Series([1,2,3,4,5,6],index=pd.date_range('20130101',periods=6))
print (df,'\n') # 给df增加E行，且该行内为1,2,3,4,5,6
