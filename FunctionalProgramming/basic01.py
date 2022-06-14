"""
    函数式编程
"""


def func01():
    print("this is func01")


def func02():
    print("this is func02")


# 函数作为参数
def func03(func):
    print("this is func03")
    # 执行传入的函数
    func()


func03(func01)
