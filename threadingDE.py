import _thread
import threading
import logging
from time import sleep,ctime

#线程
logging.basicConfig(level=logging.INFO)
loops = [2,4]
def loop(nloop,nsec):
    #nloop==》进程标识， nsec是秒数，lock是锁
    logging.info("select loop" + str(nloop) + " at "+ctime())
    sleep(nsec)
    logging.info("end loop" +str(nloop) + " at "+ ctime())

def loop1():
    logging.info("select loop1 at " + ctime())
    sleep(2)
    logging.info("end loop1 at " + ctime())

def main():
    logging.info("start all at " + ctime())
    nloops = range(len(loops))

    threads =[]
    for i in nloops:
        t = threading.Thread(target=loop,args=(i,loops[i]))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()

    # locks=[]  #锁
    # nloops = range(len(loops))
    # for i in nloops:
    #     lock = _thread.allocate_lock() #申请一个锁
    #     lock.acquire()
    #     locks.append(lock)
    # for i in nloops:
    #     _thread.start_new_thread(loop,(i,loops[i],locks[i]))
    # for i in nloops:
    #     while locks[i].locked(): pass

    # _thread.start_new_thread(loop0,())
    # _thread.start_new_thread(loop1,())
    # sleep(6)  #单独使用_thread时，主线程需要等待子线程结束的时间
    # loop()
    # loop1()
    logging.info("end all at " + ctime())

if __name__ =='__main__':
    main()
