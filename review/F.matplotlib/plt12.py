# 3D 数据

import numpy as np 
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = Axes3D(fig) # 添加3D坐标轴
# X,Y value
X = np.arange(-4,4,0.25)
Y = np.arange(-4,4,0.25)
X,Y = np.meshgrid(X,Y)
R = np.sqrt(X**2+Y**2)
# height value 
Z = np.sin(R) # 该量即Z轴的坐标值

ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow')) # rstride和cstride表示了3D图形上线的横向和纵向跨度，
ax.contourf(X,Y,Z,zdir='z',offset=-2,cmap='rainbow') # offset=-2表示把等高线图放在坐标为-2的地方，zdir表示要画出哪个方向上的等高线图
ax.set_zlim(-2,2)

plt.show()
