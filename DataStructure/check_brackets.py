"""
获取一段文字，判断文字中括号是否匹配正确，如果正确则打印正确，不正确则指出出错的地方。
"""

from stack.sstack import StackError
from stack.sstack import SStack

# s = input()
s = "The core (of) extensible programming [is] defining functions. Python allows {mandatory [and]} optional (arguments, {keyword} arguments), and even arbitrary argument lists."

brackets = '()[]{}'
open_brackets = '([{'
opposite = {')': '(', ']': '[', '}': '{'}
sk = SStack()
# valid = True
# for i in s:
#     if i in open_brackets:
#         sk.push(i)
#     elif i in opposite:
#         # 少左括号时
#         try:
#             tmp = sk.pop()
#         except StackError:
#             print("括号错误")
#             valid = False
#             break
#         # 右括号匹配左括号
#         if tmp != opposite[i]:
#             print("括号错误")
#             valid = False
#             break
# # 多左括号时
# if sk.is_empty() and valid:
#     print("括号正确")
# else:
#     print("括号错误")


# 生成器，遍历字符串，不断提供括号及其位置
def check(s):
    # i表示字符串索引位置
    i, s_len = 0, len(s)

    # 遍历字符串
    while True:
        # 跳过其他字符
        while i < s_len and s[i] not in brackets:
            i += 1
        # 到字符串结尾时
        if i >= s_len:
            return
        # 找到括号时
        else:
            yield s[i], i
            i += 1


for i, j in check(s):
    print(i, j)
