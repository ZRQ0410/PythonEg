"""
    处理、筛选Wife对象
"""
from iterable_tools import IterableHelper


class Wife:
    def __init__(self, name="", face_score=0, age=0, height=0):
        self.name = name
        self.face_score = face_score
        self.age = age
        self.height = height

    def __str__(self):
        return "{}, {}, {}, {}".format(self.name, self.face_score, self.age, self.height)


list_wife = [
    Wife("aaa", 96, 22, 166),
    Wife("bb", 100, 23, 173),
    Wife("ccc", 96, 22, 161),
    Wife("dd", 86, 27, 166),
    Wife("ee", 99, 31, 176),
    Wife("fff", 93, 24, 163),
    Wife("gg", 88, 26, 170)
]


# 颜值 > 90
def cond01(item):
    return item.face_score > 90


# 身高 < 170
def cond02(item):
    return item.height < 170


def cond03(item):
    return item.name == "ee"


def cond04(item):
    return item.face_score > 95


def cond05(item):
    return len(item.name) > 2


def cond06(item):
    return item.age < 25


for i in IterableHelper.find_all(list_wife, cond01):
    print(i)
print(IterableHelper.find_first(list_wife, cond03))


def handle01(item):
    return item.name


def handle02(item):
    return (item.name, item.face_score)

# for i in IterableHelper.select(list_wife, handle02):
#     print(i)


# 也可以用lambda替换cond函数
# print(IterableHelper.is_exist(list_wife, lambda item: item.height > 170))
#
# print(IterableHelper.sum(list_wife, lambda item: item.height))
#
# print(IterableHelper.get_max(list_wife, lambda item: item.face_score))

# for i in IterableHelper.delete(list_wife, lambda item: item.age < 25):
#     print(i)

# for i in map(lambda item: item.name, list_wife):
#     print(i)
print(IterableHelper.get_count(list_wife, lambda item: item.age < 25))
print(max(list_wife, key=lambda item: item.face_score))
