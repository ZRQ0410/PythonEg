"""
    闭包--外部嵌套作用域(对于内部函数而言)
"""


def func01():
    # a是func01的局部作用域，是func02的外部嵌套作用域
    a = 1
    b = 1

    def func02():
        # a是func02的局部变量，不能修改func01的a
        a = 2

    def func03():
        nonlocal b
        b = 2

    func02()
    print("a is", a)
    func03()
    print("b is", b)


func01()
