# Legend 图例

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1,2,50)
y1 = 2*x+1
y2 = x**2

plt.figure()

plt.xlim((-1,2)) # 设置x坐标轴范围
plt.ylim((-2,3)) # 设置y坐标轴范围
plt.xlabel('I am x')
plt.ylabel('I am y')

new_ticks = np.linspace(-1,2,5)
print(new_ticks)
plt.xticks(new_ticks) # 替换掉原来坐标轴上的标识
plt.yticks([-2,-1.8,-1,1.22,3,],
        [r'$really\ good$',r'$bad$',r'$normal$',r'$good$',r'$really\ good$']) # 为采用tex形式展示，加上正则表达式

plt.plot(x,y2,label='up') # label即线的名字
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label='down')
# plt.legend() # 给图片打上图例，不放参数即用默认图例
# plt.legend(handles=[],labels=,loc='best') # loc='best'就是由系统自动找一个最好的位置给它
# handles的作用如下
l1, = plt.plot(x,y2,color='blue',label='up')
l2, = plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--',label='down') # 注意变量名后要有逗号

plt.legend(handles=[l1,l2,], labels=['aaa','bbb'],loc='best') # 如果只想打印aaa的图例，可以把labels里，后面的'bbb'去掉，逗号要保留

plt.show()

