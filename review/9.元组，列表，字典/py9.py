# 元组 列表
# tuple list
'''
a_tuple =(12,3,5,15,6) # 元组是有序的
another_tuple = 2,4,6,7,8

a_list = [12,3,67,7,82] # 列表是有序的

for content in a_list:
    print(content)

for content in a_tuple:
    print(content)

for index in range(len(a_list)):
    print('index=',index,',number in list=',a_list[index])
'''

# list 列表
'''
a = [1,2,3,4,2,3,1,1]

a.append(0)
print(a)
a.insert(1,9) # 在第[1]位插入9
print(a)
a.remove(2)
print(a)
print(a[0])
print('a[-1]=',a[-1]) # -1序号代表倒数第一位
print(a.index(2)) # 输出2的序号
print(a.count(3)) # 输出列表中3的个数

a.sort(reverse=True) # 从大到小排序
print(a)
'''

# 多维列表
'''
multi_dim_a = [[1,2,3],
        [2,3,4],
        [3,4,5]]

print (multi_dim_a[2][2])
'''

# dictionary 字典
a_list=[1,2,3,5,4,5,4]
d = {'apple':1,'pear':2,'orange':3}
d2 = {1:'a','c':'b'}
print(d['apple'])
print(a_list[0])

d['b'] = 0
print(d) # python新版本中字典是有序的，以前是无序的
del d['pear'] # 删除字典元素
print(d)

d3 = {'apple':[1,2,3],'pear':{1:3,3:'a'},'orange':2}
print(d3['pear'][3])
