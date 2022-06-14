"""
    处理列表
"""
list01 = [43, 4, 5, 5, 6, 7, 87]


# 条件1：所有偶数
def cond01(num):
    return num % 2 == 0


# 条件2：<10的数
def cond02(num):
    return num < 10


def find(cond):
    for i in list01:
        if cond(i):
            yield i


for i in find(cond01):
    print(i, end=" ")
print()


# 打印<10的前3个数
generator = find(cond02)
# 将惰性操作变为立即操作
list_result = list(generator)  # 生成器 -> 列表
for i in list_result[:3]:
    print(i, end=" ")
