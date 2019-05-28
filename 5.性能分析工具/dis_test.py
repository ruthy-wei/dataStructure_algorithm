#coding=utf-8
import dis
def fun1():
    l=[]
    for i in range(100):
        l.append(i)
def fun2():
    l=[i for i in range(100)]

dis.dis(fun1)
dis.dis(fun2)