# set找不同
char_list=['a','b','c','c','d','d','d']

print(set(char_list)) # 重复部分会被自动删除
print(type(set(char_list)))
print(type({1:2}))

setence = 'Welcome Back to This Tutorial'
print(set(setence))
# 不能用set将不同类型的变量进行合并

unique_char = set(char_list)
unique_char.add('a') # add不能加一个列表，只能加入一个变量
print(unique_char)
# unique_char.clear() # 删除内部所有东西
unique_char.remove('a') # 删除set中的a，若set中无a会报错
unique_char.discard('b') # 删除set中的b，与remove的不同是当set中没有b时不会报错
print(unique_char)

set1 = {'a','b','c','d'}
set2 = {'a','e','i'}
print(set1.difference(set2)) # set1中与set2不同部分
print(set1.intersection(set2)) # 两集合的交集
