# 共享内存 shared memory 

value = mp.Value('d',1) # i整数，d小数，其他形式见表1
array = mp.Array('i',[1,2,3]) # 和numpy不同，只能是一维数组

# 只有这种形式才能在多核间通信
