# zip
a = [1,2,3]
b = [4,5,6]
print(zip(a,b))
print(list(zip(a,b)))
for i,j in zip(a,b):
    print(i/2,j*2)
print(list(zip(a,a,b)))

# lambda
def fun1(x,y):
    return (x+y)
print('fun1(2,3)=',fun1(2,3))

fun2 = lambda x,y: x+y
print('fun2(2,3)=',fun2(2,3))

# map
print('list(map(fun1,[1],[2]))=',list(map(fun1,[1],[2])))
print('list(map(fun1,[1,3],[2,5]))=',list(map(fun1,[1,3],[2,5])))
