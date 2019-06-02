#栈实现后缀表达式
"""
输入第一行为：字符数   5
第二行为 数字   2 2 + 3 *
输出：           12
"""
opp=['+','-','*','/']
n=int(input())
data=list(input().split())
a = []
for value in data:
    if value.isdigit():
        a.append(value)
    elif value in opp:
        first=str(a.pop())
        second=str(a.pop())
        result=eval(first+value+second)
        if value == '/' and int(result) < 0 and int(second) % int(first) != 0:
            result = str(int(result) + 1)
        a.append(result)
print(a[0])