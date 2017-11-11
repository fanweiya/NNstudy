import threading
import time
from queue import Queue
# def t1_job():
#     print('this is an added thread,numbe is %s'%threading.current_thread())
#     print('t1 start\n')
#     for i in range(100):
#         time.sleep(0.1)
#     print('t1 end\n')
# def t2_job():
#     print('t2 start\n')
#     print('t2 end\n')
# def main():
#     print(threading.active_count())
#     print(threading.enumerate())
#     print(threading.current_thread())
#     thread_1 =threading.Thread(target=t1_job())
#     thread_2 = threading.Thread(target=t2_job())
#     thread_1.start()
#     thread_2.start()
#     thread_2.join()
#     thread_1.join()
#     print('all done\n')
# if __name__ == '__main__':
#     main()

# def job(l,q):
#     for i in range (len(l)):
#         l[i] = l[i]**2
#     q.put(l)
#
# def multithreading():
#     q =Queue()
#     threads = []
#     data = [[1,2,3],[3,4,5],[4,4,4],[5,5,5]]
#     for i in range(4):
#         t = threading.Thread(target=job,args=(data[i],q))
#         t.start()
#         threads.append(t)
#     for thread in threads:
#         thread.join()
#     results = []
#     for _ in range(4):
#         results.append(q.get())
#     print(results)
#
# if __name__=='__main__':
#     multithreading()

def job1():
    global A,lock
    lock.acquire()
    for i in range(10):
        A+=1
        print('job1',A)
    lock.release()

def job2():
    global A,lock
    lock.acquire()
    for i in range(10):
        A+=10
        print('job2',A)
    lock.release()

if __name__== '__main__':
    lock=threading.Lock()
    A=0
    t1=threading.Thread(target=job1)
    t2=threading.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()