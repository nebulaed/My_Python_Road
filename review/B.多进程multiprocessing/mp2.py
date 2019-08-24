# 存储进程输出 Queue

import multiprocessing as mp

def job(q):
    res = 0
    for i in range(1000):
        res += i+i**2+i**3
    
    q.put(res) # queue

if __name__ == '__main__':
    q = mp.Queue()
    p1 = mp.Process(target = job, args = (q,)) # args 的参数只有一个值时，后面需要加一个逗号，表示args是可迭代的，后面可能还有别的参数，不加逗号会出错
    p2 = mp.Process(target = job, args = (q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print(res1+res2)
