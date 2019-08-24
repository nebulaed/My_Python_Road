# join 功能
'''
import threading
import time

def thread_job():
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finish\n')

def main():
    added_thread = threading.Thread(target=thread_job, name='T1')
    added_thread.start()
    print('all done\n')

if __name__ == '__main__':
    main()
'''
# 以上是没有用join功能的情况，主程序不会等待其他线程的任务完成后再执行后面的任务，故会使得all done出现在T1 finish前面

import threading
import time

def thread_job():
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.1)
    print('T1 finish\n')

def T2_job():
    print('T2 start\n')
    print('T2 finish\n')

def main():
    added_thread = threading.Thread(target=thread_job, name='T1')
    thread2 = threading.Thread(target=T2_job, name='T2')    
    added_thread.start()
    thread2.start()
    added_thread.join() # 使用join功能后面的语句都是要等T1运行完后再运行，一般要让运行时间最长的线程用join功能，保证主线程最后结束
    print('all done\n')

if __name__ == '__main__':
    main()

