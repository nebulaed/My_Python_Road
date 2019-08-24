# Bar 柱状图

import matplotlib.pyplot as plt
import numpy as np

n = 12
X = np.arange(n)
Y1 = (1-X/float(n))*np.random.uniform(0.5,1.0,n)
Y2 = (1-X/float(n))*np.random.uniform(0.5,1.0,n)

plt.bar(X,+Y1,facecolor='#9999ff',edgecolor='white') # +表示向上,facecolor是填充颜色
plt.bar(X,-Y2,facecolor='#ff9999',edgecolor='white') # -表示向下

# 加标注
for x,y in zip(X,Y1): # 要zip起来才会每次循环输出两个值
    # ha: horizonal alignment
    plt.text(x,y+0.05,'%.2f' % y, fontdict={'size':16,'color':'k'}, ha='center', va='bottom') # ha表示横向对齐方式，va表示纵向对齐方式

for x,y in zip(X,Y2):
    # ha: horizonal alignment
    plt.text(x,-y-0.05,'-%.2f' % y, fontdict={'size':16,'color':'k'}, ha='center', va='top')

plt.xlim(-.5,n)
plt.xticks(())
plt.ylim(-1.25,1.25)
plt.yticks(())

plt.show()
