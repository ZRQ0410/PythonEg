"""
    功能标志位
"""
import re

s = """Hello
北京
"""

# 只匹配ASCII码
regex = re.compile(r'\w+', flags=re.A)
l = regex.findall(s)
print(l)

# 忽略大小写
regex = re.compile('[a-z]+', flags=re.I)
l = regex.findall(s)
print(l)

# 使.可以匹配换行
regex = re.compile('.+', flags=re.S)
l = regex.findall(s)
print(l)

# 使^$可以匹配每一行的开头结尾位置
regex = re.compile('^北京', flags=re.M)
l = regex.findall(s)
print(l)