"""
    包
"""

# import package01.m01 as m
# m.func01()

# from package01.package02.m02 import func02
# func02()

from package01.package02.m02 import *
func02()

def func():
    """ 这是文档字符串 """
    return True
print(func.__doc__)
print(func.__name__)
print(__file__)
