# def 函数
'''
def function():
    print('This is a function')
    a = 1+2
    print(a)
function()
'''

# 函数参数
'''
def fun(a,b):
    c = a*b
    print('the c is',c)
fun(9,4)
fun(a=3,b=5)
'''

# 函数默认参数
def sale_car(price,colour,brand,is_second_hand,length=200,hight=100): # 预赋值变量必须在未赋值变量后
    print('price:',price,
            'colour:',colour,
            'brand:',brand,
            'is_second_hand',is_second_hand,
            'length:',length,
            'hight:',hight)

sale_car(1000,'red','carmy',True)

