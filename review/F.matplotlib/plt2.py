# figure 图像
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3,3,50)
y1 = 2*x+1
y2 = x**2

plt.figure()
plt.plot(x,y1)

plt.figure(num=3,figsize=(8,5)) # num=3表示设定figure序号为3，figsize=(8,5)表示设定其窗口长宽为8×5
plt.plot(x,y2)
plt.plot(x,y1,color='red',linewidth=1.0,linestyle='--') # 设定线的颜色，线宽，线型

plt.show()


