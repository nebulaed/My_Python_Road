# numpy copy & deep copy

import numpy as np

a = np.arange(4)
b = a
c = a
d = b
a[0] = 11

print(b is a) # True
print(c is a) # True
print(d is a) # True
    
d[1:3]=[22,33]

a is d # True
b is d # True
c is d # True

# 想要b和a脱离关系，需要用以下方法

b = a.copy() # deep copy，只copy值，b不是a
a[3] = 44

print(b is a) # False


