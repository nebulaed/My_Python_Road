# Contours 等高线图

import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    # the height function
    return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y) # 把x,y mesh出来，变成网格图，等高线图在其上绘制

# use plt.contourf to filling contours
# X,Y and value for (X,Y) point
plt.contourf(X,Y,f(X,Y),8,alpha=0.75,cmap=plt.cm.hot) # cmap把f(X,Y)对应成颜色，颜色还有cold


# use plt.contour to add contour lines
C = plt.contour(X,Y,f(X,Y),8,colors='black',linewidth=.5) # 8表示等高线把图分为10部分，0是把图分成2部分

# adding label
plt.clabel(C,inline=True,fontsize=20) # 给线加上标注

plt.xticks(())
plt.yticks(())

plt.show()
