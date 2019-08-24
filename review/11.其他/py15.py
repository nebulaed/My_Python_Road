import copy
a = [1,2,3]
b = a
print('id(a)=',id(a))
print('id(b)=',id(b))
b[0]=11
print(a)
b[1]=22
print(b)
print('id(a)==id(b)?',id(a)==id(b))
c = copy.copy(a)
print('id(a)==id(c)?',id(a)==id(c))
c[1]=222222;
print('a=',a)
print('c=',c)
a = [1,2,[3,4]]
d = copy.copy(a) # copy.copy只能使得浅层的id不跟随前变量，而deepcopy能使其深层id也不跟随前变量
print(id(a)==id(b))
print('id(a[2])==id(d[2])?',id(a[2])==id(d[2]))
a[0]=11
print('d=',d)
a[2][0]=333
print('d=',d)
e = copy.deepcopy(a)
print('id(a[2])==id(e[2])?',id(a[2])==id(e[2]))
