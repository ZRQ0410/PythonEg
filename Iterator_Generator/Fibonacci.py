"""
Fibonacci using generator
"""


def fib(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a+b
        yield a


for i in fib(10):
    print(i, end=" ")
