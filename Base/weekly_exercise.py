print('\n1.')
# 1. 斐波那契数列：从第3项开始，每一项都等于前两项之和。
#     1, 1, 2, 3, 5, 8, 13, 21..
# 定义函数，根据长度获取斐波那契数列。
def fibonacci(i):
    if i <= 2:
        return 1
    return fibonacci(i - 2) + fibonacci(i - 1)

for i in range(1, 9):
    print(fibonacci(i), end=" ")


print('\n\n2.')
# 2. 定义函数，删除列表中所有重复的元素(重复元素只保留一个)。
# 输入：[4,35,7,64,7,35]
# 输出：[4, 35, 7, 64]
def single(lst):
    list01 = set(lst)
    return list01

lst = [4,35,7,64,7,35]
print(single(lst))


print('\n3.')
# 3. 定义函数，判断二维数字列表中是否存在某个数字
# 输入：二维列表、11
# 输出：True
def is_exist(lst, a):
    if a in lst:
        return True
    return False

lst = [2, 5, 4, 11, 16]
print(is_exist(lst, 11))


print('\n4.')
# 4. 定义函数，返回字符串中第一个不重复的字符。
# 输入：ABCACDBEFD
# 输出：E
def non_repetition(s):
    dict01 = {}
    for char in s:
        if char not in dict01:
            dict01[char] = 1
        else:
            dict01[char] += 1
    for k, v in dict01.items():
        if v == 1:
            return k

s = "ABCACDBEFD"
print(non_repetition(s))


print('\n5.')
# 5.质数：大于1的整数，除了1和它本身以外不能再被其他数字整除。
#     定义函数，获取指定范围内的所有质数。
# 输入：2,20
# 输出：[2, 3, 5, 7, 11, 13, 17, 19]
def is_prime(a, b):
    primes = []
    for k in range(a, b):
        if k > 1:
            for j in range(2, k):
                if k % j == 0:
                    break
            else:
                primes.append(k)
    return primes

print(is_prime(2, 20))