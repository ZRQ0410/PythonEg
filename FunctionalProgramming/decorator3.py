import time


def print_excute_time(func):
    def wrapper(*args):
        time01 = time.time()
        result = func(*args)
        time02 = time.time()
        return result, "执行了{}s".format(time02 - time01)
    return wrapper


@print_excute_time
def func01():
    time.sleep(2)
    print("func01执行完毕")
    return 999


@print_excute_time
def func02():
    time.sleep(1)
    print("func02执行完毕")


print(func01())
print(func02())
