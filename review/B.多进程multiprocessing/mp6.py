# 进程锁 Lock
'''
import multiprocessing as mp
import time 

def job(v,num):
    for _ in range(10):
        time.sleep(0.1)
        v.value += num # 共享内存必须用.value形式
        print(v.value)

def multicore():
    v = mp.Value('i',0)
    p1 = mp.Process(target=job, args=(v,1))
    p2 = mp.Process(target=job, args=(v,3))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ =='__main__':
    multicore()
'''
# 以上状态即不用进程锁时，会导致该数一会儿加1一会儿加3，两个进程相互抢夺资源

import multiprocessing as mp
import time 

def job(v,num,l):
    l.acquire()
    for _ in range(10):
        time.sleep(0.1)
        v.value += num # 共享内存必须用.value形式
        print(v.value)
    l.release()

def multicore():
    l = mp.Lock()
    v = mp.Value('i',0)
    p1 = mp.Process(target=job, args=(v,1,l))
    p2 = mp.Process(target=job, args=(v,3,l))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__ =='__main__':
    multicore()

# 现在用了进程锁后，会先把+1全部执行完再执行+3。
# 在涉及到共享内存时，为了避免数据发生错误，加锁保持单线程是最好的办法
