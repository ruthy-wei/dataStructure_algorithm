#coding=utf-8
import threading
from time import ctime,sleep


def music(func):
    for i in range(2):
        print ("I was listening to %s. %s" %(func,ctime()))
        sleep(4)

def movie(func):
    for i in range(2):
        print ("I was at the %s! %s" %(func,ctime()))
        sleep(5)

threads = []
t1 = threading.Thread(target=music,args=(u'爱情买卖',))
threads.append(t1)
t2 = threading.Thread(target=movie,args=(u'阿凡达',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        #setDaemon(True)将线程声明为守护线程，必须在start() 方法调用之前设置，如果不设置为守护线程程序会被无限挂起。
        # 子线程启动后，父线程也继续执行下去，当父线程执行完最后一条语句print "all over %s" %ctime()后，
        # 没有等待子线程，直接就退出了，同时子线程也一同结束。
        t.setDaemon(True)
        t.start()
    t.join()#join（）的作用是，在子线程完成运行之前，这个子线程的父线程将一直被阻塞。
    print("all over %s" %ctime())

"""
result:
I was listening to 爱情买卖. Mon May 27 15:13:35 2019
I was at the 阿凡达! Mon May 27 15:13:35 2019
I was listening to 爱情买卖. Mon May 27 15:13:36 2019
I was at the 阿凡达! Mon May 27 15:13:40 2019
all over Mon May 27 15:13:45 2019
"""