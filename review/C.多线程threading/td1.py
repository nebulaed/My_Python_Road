# 添加线程 Thread

import threading

def thread_job():
    print('This is an added Thread, number is %s' % threading.current_thread())

def main():
    added_thread = threading.Thread(target=thread_job,)
    #print(threading.active_count()) # 检查现在有多少激活的线程
    #print(threading.enumerate()) # 检查当前激活线程
    #print(threading.current_thread()) # 现在在运行程序的是哪一个线程
    added_thread.start()

if __name__ == '__main__':
    main()
