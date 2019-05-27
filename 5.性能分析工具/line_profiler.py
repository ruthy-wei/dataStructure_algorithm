import time

@profile
def fun():
    a = 0
    b = 0
    for i in range(100000):
        a = a + i * i
    for i in range(3):
        b += 1
        time.sleep(0.1)
    return a + b
fun()
"""
test:line_profile
1.在需要测试的函数加上@profile装饰，这里我们把测试代码写在line_profile.py文件上.
2.运行命令行：kernprof -l -v line_profile.py

test:memory_profiler
1.在需要测试的函数加上@profile装饰
2.执行命令： python -m memory_profiler line_profile.py
"""