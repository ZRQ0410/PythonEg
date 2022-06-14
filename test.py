def fib(n):
    a = 0
    b = 1
    count = 0
    while count < n:
        a, b = b, a+b
        count += 1
        yield a


for i in fib(5):
    print(i)
