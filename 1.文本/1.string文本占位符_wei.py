name1="菜鸟教程"
print("format占位符：网站名：{name}, 地址 {url}".format(name=name1, url="www.runoob.com"))

# 通过字典设置参数
site = {"name": "百度", "url": "www.baidu.com"}
print("format通过字典设置参数占位符：网站名：{name}, 地址 {url}".format(**site))

# 使用元组传参
infos = '钢铁侠', 66, '小辣椒'
print('我是{}，身价{}亿。'.format(*infos))

# 通过列表索引设置参数
my_list = ['谷歌', 'www.google.com']
print("format通过列表索引设置参数占位符：网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的

#通过% 为文本占位
print("占位符：网站名：%s, 地址 %s" % ("菜鸟教程","www.runoob.com"))


