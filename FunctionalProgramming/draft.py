import time

def print_excute_time(func):
    def wrapper(*args):
        time01 = time.time()
        result = func(*args)
        time02 = time.time()
        return result, "{}s".format(time02 - time01)
    return wrapper

@print_excute_time
def func01():
    sum_value = 0
    for i in range(100):
        sum_value += i
    return sum_value

@print_excute_time
def func02(n):
    sum_value = 0
    for i in range(n):
        sum_value += i
    return sum_value


print(func01())
print(func02(100000))