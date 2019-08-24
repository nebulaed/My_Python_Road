# while 循环
#condition = 1
#while condition < 10:
#    print(condition)
#    condition = condition + 1

#while True:
#    print("I'm True")

# for 循环
example_list = [1,2,3,4,5,6,7,12,543,876,12,3,2,5]

for i in example_list:
    print(i)

print('outer of for')

for i in range(1,10): # 左闭右开
    print(i)

for i in range(1,10,2): # 步长是2
    print(i)
