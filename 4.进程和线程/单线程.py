#coding=utf-8
import threading
from time import ctime,sleep

def music(func):
    for i in range(2):
        print(("I was listening to %s. %s" %(func,ctime())))
        sleep(1)

def movie(func):
    for i in range(2):
        print(("I was at the %s! %s" %(func,ctime())))
        sleep(5)



if __name__ == '__main__':
    music('爱情买卖')
    movie('阿凡达')
    print(("all over %s" %ctime()))

"""
result：
I was listening to 爱情买卖. Mon May 27 15:11:24 2019
I was listening to 爱情买卖. Mon May 27 15:11:25 2019
I was at the 阿凡达! Mon May 27 15:11:26 2019
I was at the 阿凡达! Mon May 27 15:11:31 2019
all over Mon May 27 15:11:36 2019
"""