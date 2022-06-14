"""
    处理列表
"""
list01 = [43, 4, 5, 5, 6, 7, 87]


# 条件1：所有偶数
def cond01(num):
    return num % 2 == 0


# 条件2：>10且<50
def cond02(num):
    return 10 < num < 50


def find(cond):
    for i in list01:
        if cond(i):
            yield i


for i in find(cond02):
    print(i)
