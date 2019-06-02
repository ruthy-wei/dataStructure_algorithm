#coding=utf-8
import dis
def fun1():
    l=[]
    for i in range(1000000):
        l.append(i*i*i)
# @profile
def fun2():
    l=[i*i*i for i in range(1000000)]
# @profile
def fun3():
    l=list((i*i*i for i in range(1000000)))
dis.dis(fun1)
dis.dis(fun2)
dis.dis(fun3)
