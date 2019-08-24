# pickle保存数据
import pickle

a_dict = {'da':111,2:[23,1,4],'23':{1:2,'d':'sad'}}

# 写入
'''
file = open('pickle_example.pickle','wb')
pickle.dump(a_dict,file)
file.close()
'''

# 读取

# 方式1
#file = open('pickle_example.pickle','rb')
#a_dict1 = pickle.load(file)
#file.close()
#print(a_dict1)

# 方式2

with open('pickle_example.pickle','rb') as file:
    a_dict1 = pickle.load(file)
# 这种方式不用的担心忘记close
print(a_dict1)
