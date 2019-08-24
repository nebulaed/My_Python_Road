# 线程锁 Lock
'''
import threading

def job1():
    global A
    for i in range(10):
        A += 1
        print('job1',A)

def job2():
    global A
    for i in range(10):
        A += 10
        print ('job2',A)

if __name__ == '__main__':
    A = 0
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
'''
# 上面是没有线程锁Lock的，故job1和job2会交替输出

import threading

def job1():
    global A
    lock.acquire()
    for i in range(10):
        A += 1
        print('job1',A)
    lock.release() # release()要和lock()配对使用

def job2():
    global A
    lock.acquire()
    for i in range(10):
        A += 10
        print ('job2',A)
    lock.release()

if __name__ == '__main__':
    lock = threading.Lock()
    A = 0
    t1 = threading.Thread(target=job1)
    t2 = threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

