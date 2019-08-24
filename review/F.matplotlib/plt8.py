# Scatter 散点图

import matplotlib.pyplot as plt
import numpy as np

n = 1024
X = np.random.normal(0,1,n)
Y = np.random.normal(0,1,n)
T = np.arctan2(Y,X) # for color value,colormap根据data生成很好看

plt.scatter(X,Y,s=300,c=T,alpha=0.5)# size=75,color色谱,alpha透明度

plt.xlim((-1.5,1.5))
plt.ylim((-1.5,1.5))
plt.xticks(()) # 删除x坐标轴上的标签
plt.yticks(()) # 删除y坐标轴上的默认标签``
plt.show()
