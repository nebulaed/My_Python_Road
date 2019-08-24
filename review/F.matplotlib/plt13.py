# Subplot 多合一显示
'''
import matplotlib.pyplot as plt

plt.figure()

plt.subplot(2,2,1) # 2行2列的图中的第1个
plt.plot([0,1],[0,1]) # (0,0)到(1,1)的一条直线

plt.subplot(2,2,2) # 2行2列的图中的第2个
plt.plot([0,1],[0,2]) # (0,0)到(1,2)的一条直线

plt.subplot(223) # ...第3个
plt.plot([0,1],[0,3]) # (0,0)到(1,3)的一条直线

plt.subplot(224) # ...第4个
plt.plot([0,1],[0,4]) # (0,0)到(1,4)的一条直线

plt.show()
'''

import matplotlib.pyplot as plt

plt.figure()

plt.subplot(2,1,1) # 2行1列的图中的第1个，即占用第一行的所有位置
plt.plot([0,1],[0,1]) # (0,0)到(1,1)的一条直线

plt.subplot(2,3,4) # 2行3列的图中的第1个
plt.plot([0,1],[0,2]) # (0,0)到(1,2)的一条直线

plt.subplot(235) # ...第2个
plt.plot([0,1],[0,3]) # (0,0)到(1,3)的一条直线

plt.subplot(236) # ...第3个
plt.plot([0,1],[0,4]) # (0,0)到(1,4)的一条直线

plt.show()