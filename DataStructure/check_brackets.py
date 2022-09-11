"""
获取一段文字，判断文字中括号是否匹配正确，如果正确则打印正确，不正确则指出出错的地方。
"""

from stack.sstack import SStack

# s = input()
s = "The core (of) extensible programming [is] defining functions. Python allows {mandatory [and]} optional (arguments, {keyword} arguments), and even arbitrary argument lists."

brackets = '()[]{}'
open_brackets = '([{'
opposite = {')': '(', ']': '[', '}': '{'}
sk = SStack()


# 生成器，遍历字符串，不断提供括号及其位置
def find_bracket(s):
    # i表示字符串索引位置
    i, s_len = 0, len(s)

    # 遍历字符串
    while True:
        # 跳过其他字符
        while i < s_len and s[i] not in brackets:
            i += 1
        # 如果是字符串结尾，结束
        if i >= s_len:
            return
        # 找到括号时，判断是否匹配，返回括号所在位置
        else:
            yield s[i], i  # 返回元祖
            i += 1


# 判断括号是否匹配
def check_bracket():
    for br, pos in find_bracket(s):
        # 找到左括号
        if br in open_brackets:
            sk.push((br, pos))
        # 找到右括号
        else:
            # 右括号无匹配或不匹配时
            if sk.is_empty() or sk.pop()[0] != opposite[br]:
                print("Mismatch at %d for %s" % (pos, br))
                break
    # 执行完for后（未执行break）
    else:
        # 如果stack非空：左括号多了
        if sk.is_empty():
            print("All parenthese are matched")
        else:
            err = sk.pop()
            print("Mismatch at %d for %s" % (err[1], err[0]))


check_bracket()
