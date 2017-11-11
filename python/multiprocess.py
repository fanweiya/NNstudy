import multiprocessing as mp
# import threading as td
#
# def job():
#     print('aaaaa')
#
# t1=td.Thread(target=job,args=(a,b))
# p1=mp.Process(target=job,args=(a,b))

# def job(x):
#     return x*x
#
# def multicore():
#     pool = mp.Pool(processes=2)
#     res = pool.map(job, range(10))
#     print(res)
#     res = pool.apply_async(job, (2,))
#     print(res.get())
#     multi_res =[pool.apply_async(job, (i,)) for i in range(10)]
#     print([res.get() for res in multi_res])
#
# if __name__ == '__main__':
#     multicore()

value=mp.Value('d',1)

array=mp.Array('i',[1,2,3])

print(value)
print(array)

