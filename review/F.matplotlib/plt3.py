# 设置坐标轴1

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,2,50)
y1 = 2*x+1
y2 = x**2

plt.figure()
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--')

plt.xlim((-1,2)) # 设置x坐标轴范围
plt.ylim((-2,3)) # 设置y坐标轴范围
plt.xlabel('I am x')
plt.ylabel('I am y')

new_ticks = np.linspace(-1,2,5) 
print(new_ticks)
plt.xticks(new_ticks) # 替换掉原来坐标轴上的标识
plt.yticks([-2,-1.8,-1,1.22,3,],
        [r'$really\ good$',r'$bad$',r'$normal$',r'$good$',r'$really\ good$']) # 为采用tex形式展示，加上正则表达式

plt.show()

