# Animation 动画

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig,ax = plt.subplots()

x = np.arange(0,2*np.pi,0.01)
line, = ax.plot(x,np.sin(x))

def animate(i):
    line.set_ydata(np.sin(x+i/10))
    return line, # 打个,因为返回的line是个列表，这只是个表头

def init():
    line.set_ydata(np.sin(x))
    return line,

ani = animation.FuncAnimation(fig=fig,func=animate,frames=100,init_func=init,interval=20,blit=True)
# frames=100表示插入100帧,blit=True表示不动处不更新画面，func为更新函数，init_func为初始化函数
plt.show()
