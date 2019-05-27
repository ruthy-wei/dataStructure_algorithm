import timeit
def method():
    list=[]
    sum=0
    for i in range(100000):
        sum=sum*i
        list.append(sum)
ta=timeit.timeit(stmt=method,number=10)
tr=timeit.repeat(stmt=method,repeat=3,number=10)
print(ta)
print(tr)