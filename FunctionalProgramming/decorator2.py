def print_func_name(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)  # 新功能
        return func(*args, **kwargs)  # 调用func(原函数)并返回func的返回值
    return wrapper


@print_func_name  # func01 = print_func_name(func01)
def func01():
    print(1)
    return 'ok'


@print_func_name
def func02(a, b, c=0):
    print(2, a, b, c)


print(func01())

func02(100, 200, c=300)
