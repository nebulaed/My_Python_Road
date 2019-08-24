# Pandas plot出图

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# plot data

# Series
data = pd.Series(np.random.randn(1000), index=np.arange(1000))
data = data.cumsum()
# data.plot()
# plt.show()

# DataFrame
data = pd.DataFrame(np.random.randn(1000,4),
        index=np.arange(1000),
        columns=list("ABCD"))
data = data.cumsum()
# print(data.head()) # print出前5个数据，默认参数为5，想要自己设定在()中填数字即可
# data.plot()
# plt.show()

# plot methods: 'bar','hist','box','kde','area','scatter','hexbin','pie'
ax = data.plot.scatter(x='A', y='B', color='DarkBlue', label='Class 1')
data.plot.scatter(x='A',y='C', color='DarkGreen', label='Class 2', ax=ax) # 第一个ax是参数名，第二个ax是图名，含义是把该plot放进与ax同一张图中
plt.show()
