def func01():
    print(1)
    return 'ok'

def func02(a, b, c=0):
    print(2, a, b, c)

def print_func_name(func):
    def wrapper(*args, **kwargs):
        # 新功能
        print(func.__name__)
        # 旧功能
        return func(*args, **kwargs)
    return wrapper

func01 = print_func_name(func01)
print(func01())  # 执行的是内部函数

func02 = print_func_name(func02)
func02(100, 200, c=300)