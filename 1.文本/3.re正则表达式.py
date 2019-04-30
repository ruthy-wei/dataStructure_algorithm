# -*- coding: UTF-8 -*-
'''
1. re.match,re.search,re.finditer 的返回值均为m=<re.Match object; span=(0, 1), match='她'>类型，
    若想获得匹配值的位置：m.span()；
    若想获得匹配值的内容，m.group()；
    特殊：re.finditer返回的为迭代器需要循环输出
2. re.sub返回替换后的内容
3. re.findall 返回匹配值的列表
'''
import re
pattern='她|他|它|你'
text='她一直认为他是个好人'

#re.match 尝试从字符串的起始位置匹配一个模式，
# 如果不是起始位置匹配成功的话，match()就返回none。
print("="*15,'match',"="*15)
print(re.match(pattern,text))
matchObj = re.match(pattern,text)
if matchObj:
   print("match 仅匹配开始字符--> matchObj.group() : ", matchObj.group())
else:
   print("No match!!")



#re.search 扫描整个字符串并返回第一个成功的匹配。
print("="*15,'search',"="*15)
print(re.search(pattern,text))
searchObj = re.search(pattern,text)
if searchObj:
   print("search --> matchObj.group() : ", searchObj.group())
else:
   print("No match!!")

#re.sub用于替换字符串中的匹配项。
print("="*15,'sub',"="*15)
sub_after = re.sub(pattern, '小红', text, count=0, flags=0)
print(sub_after)

#repl替换值:函数
print("="*15,'?P<groupName>',"="*15)
def double(x):
    value = int(x.group('value'))
    return str(value * 2)
s = 'A23G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))
#?P组名必须是合格的python标识符

#compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，
# 供 match() 和 search() 这两个函数使用。
print("="*15,'compile',"="*15)
pattern1=re.compile(r'\d+')
m=pattern1.match('one12twothree34four')
print(m)

#在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，
# 如果没有找到匹配的，则返回空列表。
print("="*15,'findall',"="*15)
pattern3 = re.compile(r'\d+')  # 查找数字
result1 = pattern3.findall('run88oob123google456', 0, 10)
print('findall:',result1)

#和 findall 类似，在字符串中找到正则表达式
# 所匹配的所有子串，并把它们作为一个迭代器返回。
print("="*15,'finditer',"="*15)
it = re.finditer(r"\d+","12a32bc43jf3")
for match in it:
    print (match.group())
print("="*15,'splite',"="*15)
#split 方法按照能够匹配的子串将字符串分割后返回列表
print(re.split('\W+', 'runoob, runoob, runoob.'))

