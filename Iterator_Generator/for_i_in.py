# list01 = [34, 4, 5, 46, 57, 87]
#
# # 获取迭代器对象
# iterator = list01.__iter__()
# while True:
#     try:
#         # 获取下一个元素
#         i = iterator.__next__()
#         print(i)
#     # 没有元素则捕获异常
#     except StopIteration:
#         break

"""
    自定义一个迭代器
"""

class SkillIterator:
    def __init__(self, skills):
        self.__skills = skills
        self.__index = -1

    def __next__(self):
        self.__index += 1
        if self.__index > len(self.__skills) - 1:
            raise StopIteration
        return self.__skills[self.__index]


class SkillManager:
    def __init__(self):
        self.__skills = []

    def add_skill(self, skill):
        self.__skills.append(skill)

    def __iter__(self):
        return SkillIterator(self.__skills)

manager = SkillManager()
manager.add_skill("skill01")
manager.add_skill("skill02")
manager.add_skill("skill03")

iterator = manager.__iter__()

# while True:
#     try:
#         print(iterator.__next__())
#     except StopIteration:
#         break
for i in manager:
    print(i)
