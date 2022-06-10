import re

# compile对象
regex = re.compile('(ab)cd(?P<pig>ef)')

# match对象
obj = regex.search("abcdefhijk")
print(obj)

# 对象属性
print("正则表达式", obj.re)
print("目标字符串", obj.string)
print("起始位置", obj.pos)
print("结束位置", obj.endpos)
print("最后一组名称", obj.lastgroup)
print("最后一组序号", obj.lastindex)
print()

# 对象方法
print("匹配内容的位置", obj.span(), obj.start(), obj.end())
print("子组内容", obj.groups())
print("捕获组内容", obj.groupdict())
print("对应内容", obj.group(), obj.group('pig'))