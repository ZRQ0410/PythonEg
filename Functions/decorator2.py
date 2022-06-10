def print_func_name(func):
    def wrapper(*args, **kwargs):
        # 新功能
        print(func.__name__)
        # 旧功能
        return func(*args, **kwargs)
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