# encoding:UTF-8
def yield_test(n):
    for i in range(n):
        yield call(i) #等同于return call(i)，可以继续执行
        print("i=", i)
    print("Done.")

def call(i):
    return i * 2

for i in yield_test(5):
    print(i, ",")