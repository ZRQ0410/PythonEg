"""
    装饰器: 对功能增加权限验证(增加新功能，不改变原有代码(开闭原则))
"""


# 装饰器的功能
def verify(func):
    def wrapper(*args, **kargs):  # kargs针对关键字实参
        print("权限验证")
        func(*args, **kargs)  # 放入实参
    return wrapper


@verify  # 拦截调用，增加新功能
def enter_background(id, pwd):
    print("进入后台", id, pwd)


@verify
def delete_order(id):
    print("删除订单", id)


"""
@verify的含义:
# enter_background = 新功能(验证) + 旧功能(进入后台)
enter_background = verify(enter_background)
delete_order = verify(delete_order)
"""

enter_background("abc", pwd=1234)
delete_order(101)
