"""
    闭包
"""


def func01():
    a, b = 1, 1

    # 内嵌函数
    def func02():
        nonlocal b  # 修改外部变量要申明nonlocal
        b = 2
        print(a, b)  # 内嵌函数引用外部函数的变量

    # 返回内嵌函数
    return func02


# 调用外部函数
result = func01()
# 调用内嵌函数
result()
