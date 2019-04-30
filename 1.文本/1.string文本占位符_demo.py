'''本节主要讲述字符串的替换问题，常用的为Template Interpolation Format三种格式化占位符，
   https://blog.csdn.net/yiifaa/article/details/78024206
'''
#capwords()
import string
s='The quick brown fox jumped over the lazy dog.'
print(s)
print(string.capwords(s))

#Template
ss = string.Template('There  ${moneyType} is  ${money}')
print(ss.substitute(moneyType = 'Dollar',money=12))#替换全部元素
print(ss.safe_substitute(moneyType = 'Dollar'))#替换部分元素

values={'var':'foo'}
t=string.Template("""
Variable        : $var hi
Escape          : $$
Variable in text: ${var}iable
""")
print('**Template:',t.substitute(values))

#Interpolation
s="""
Variable        : %(var)s
Escape          : %%
Variable in text: %(var)siable
"""
print('**Interpolation:',s % values)

#Format
s="""
Variable        : {var}
Escape          : {{}}
Variable in text: {var}iable
"""
print('**Format:',s.format(**values))
#
