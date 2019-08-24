# 进程池 Pool

import multiprocessing as mp

def job(x):
    return x*x

def multicore():
    pool = mp.Pool()
    # pool = mp.Pool(processes=4) # 只用4个核
    res = pool.map(job,range(10))
    print(res)
    res = pool.apply_async(job,(2,)) # apply_async()只能传递一个值，因此只会放入一个核进行运算，但要注意传入值可迭代，后面要加逗号
    print(res.get()) # 用get()获取apply_async()返回值
    multi_res = [pool.apply_async(job,(i,)) for i in range(10)]
    print([res.get() for res in multi_res]) # 为使apply_async达到map同样的效果，必须改造成该形式

if __name__ == '__main__':
    multicore()
