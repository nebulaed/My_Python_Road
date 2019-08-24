# 图中图

import matplotlib.pyplot as plt

fig = plt.figure()
x = [1,2,3,4,5,6,7]
y = [1,3,4,2,5,8,6]

left,bottom,width,height=0.1,0.1,0.8,0.8 # 从横轴的10%开始，纵轴的10%开始，长度和高度都是80%
ax1 = fig.add_axes([left,bottom,width,height])
ax1.plot(x,y,'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title')

left,bottom,width,height=0.2,0.6,0.25,0.25 # 从横轴的20%开始，纵轴的60%开始，长度和高度都是25%
ax1 = fig.add_axes([left,bottom,width,height])
ax1.plot(y,x,'b')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('title inside 1')

# 用第2种方法画出图中图
plt.axes([.6,.2,0.25,0.25]) # 从横轴的60%开始，纵轴的20%开始，长度和高度都是25%
plt.plot(y[::-1],x,'g') #y[::-1]表示从后往前逆序步长为1
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside 2')

plt.show()
