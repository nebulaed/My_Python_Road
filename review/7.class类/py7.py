# class 类
'''
class Calculator:
    name = 'Good calculator'
    price = 18
    def add(self,x,y): # 类内函数要加self
        print(self.name)
        result = x + y
        print(result)
    def minus(self,x,y):
        result = x - y
        print(result)
    def times(self,x,y):
        # result = x * y 
        print(x*y)
    def divide(self,x,y):
        # result = x/y
        print(x/y)
calcul = Calculator()
print(calcul.name)
print(calcul.price)
calcul.add(10,11)
calcul.minus(10,11)
calcul.divide(13,2)
'''
# class类init功能

class Calculator:
    name = 'Good calculator'
    price = 18
    def __init__(self,name,price,hight,width,weight):
        self.name = name
        self.price = price
        self.h = hight
        self.wi = width
        self.we = weight
        self.add(1,2)
    def add(self,x,y):
        print(x+y)
    def minus(self,x,y):
        print(x-y)
    def times(self,x,y):
        print(x*y)
    def divide(self,x,y):
        print(x/y)
c = Calculator('Bad calculator',12,30,15,19)
print(c.name)
c.add(8,20)
