# 全局&局部变量
APPLE = 100
# b = None # 老版python需要在外面声明
def fun():
    a = APPLE
    global b
    b=APPLE/a
    return a+100

print(APPLE)
print(fun())
print(b)
