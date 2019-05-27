# coding=utf-8
import line_profiler
import sys

def bbb():
    for i in range(0, 3):
        print(i**2)
    print('end')

profile = line_profiler.LineProfiler(bbb)  # 把函数传递到性能分析器
profile.enable()  # 开始分析
bbb()
profile.disable()  # 停止分析
profile.print_stats(sys.stdout)  # 打印出性能分析结果