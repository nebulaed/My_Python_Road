# try错误处理
try:
    file = open('eeee','r+')
except Exception as e:
    print(e) # 若出现错误则打印错误信息
    response = input('do you want to create a new file')
    if response == 'y':
        file = open('eeee','w')
    else:
        pass
else: # 若try成功了的话
    file.write('ssss')
    file.close()
