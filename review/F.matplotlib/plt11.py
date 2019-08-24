# Image 图片

import matplotlib.pyplot as plt
import numpy as np

# image data
a = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3,3)

'''
for the value of "interpolation", check this:
http://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
'''

plt.imshow(a, interpolation='nearest', cmap=plt.cm.bone, origin='lower') # origin定义位置，lower和upper分别对应不同位置呈现，cmap中的plt.cm.bone可用'bone'取代
plt.colorbar(shrink=0.9) # 用默认参数就可以，即括号中空，shrink=0.9表示长度为plot的90%

plt.xticks(())
plt.yticks(())

plt.show()
