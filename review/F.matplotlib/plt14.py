# Subplot 分格显示

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# method 1：subplot2grid
'''
plt.figure()
ax1 = plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1) 
# 整体plot有3行3列，从第1行第1列开始，ax1占1行3列
ax1.plot([1,2],[1,2]) # plot的内容为从(1,1)到(2,2)的一条线段
ax1.set_title('ax1_title')
# 之前是plt.xlabel这样去设置label，但ax1不是plot而是grid
# plt.xlim相应的就是ax1.set_xlim

ax2 = plt.subplot2grid((3,3),(1,0),colspan=2,) # (1,0)从第2行第1列开始，占2列

ax3 = plt.subplot2grid((3,3),(1,2),rowspan=2,) # (1,2)从第2行第3列开始，向下占2行位置

ax4 = plt.subplot2grid((3,3),(2,0))

ax5 = plt.subplot2grid((3,3),(2,1))

plt.tight_layout()
plt.show()
'''

# method 2: gridspec
'''
plt.figure()
gs = gridspec.GridSpec(3,3)
ax1 = plt.subplot(gs[0,:]) # 第1行占所有列
ax2 = plt.subplot(gs[1,:2]) # 第2行占了第1列到第2列(左闭右开)
ax3 = plt.subplot(gs[1:,2]) # 第2行到最后一行占了第3列
ax4 = plt.subplot(gs[-1,0]) # 倒数第1行占了第1列
ax5 = plt.subplot(gs[-1,-2]) # 倒数第1行占了倒数第2列

plt.tight_layout()
plt.show()
'''
# method 3: easy to define structure -- subplots

f,((ax11,ax12),(ax21,ax22)) = plt.subplots(2,2,sharex=True,sharey=True) # sharex=True表示共享x轴，sharey同理
ax11.scatter([1,2],[1,2])

plt.tight_layout()
plt.show()
