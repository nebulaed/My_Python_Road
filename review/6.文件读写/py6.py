# 读写文件1
'''
text = "This is my first test.\nThis is next line.\nThis is last line."
print(text)
my_file = open('my file.txt','w') #'w'表示以写的形式打开文件，'r'表示以只读形式打开文件
my_file.write(text)
my_file.close()
'''

# 读写文件2
'''
append_text='\nThis is appended file.'
my_file=open('my file.txt','a') # append表示在后面附加内容
my_file.write(append_text)
my_file.close()
'''

# 读写文件3
file = open('my file.txt','r')
# content = file.readline()
# second_read_time = file.readline()
# python_list = [1,2,3,4,5,'dahi','fuiq']
# print(content,second_read_time)
content = file.readlines()
print(content)
