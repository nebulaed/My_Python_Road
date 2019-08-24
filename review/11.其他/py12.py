# continue & break
'''
a = True
while a:
    b = input('type something')
    if b == '1':
        a = False
    else:
        pass
    print('still in while')
'''
# 两者的区别在于前者检测到1仍会执行这一次循环后面的语句，而后者不会
while True:
    c = input('type something')
    if c == '1':
        break
    else:
        pass
    print('still in while')
