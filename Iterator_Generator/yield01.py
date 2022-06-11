class SkillManager:
    def __init__(self):
        self.__skills = []

    def add_skill(self, skill):
        self.__skills.append(skill)

    def __iter__(self):

        # 1. 将yield以前的代码，定义在__next__方法中
        # 2. 抛出异常的代码在最后一部分中
        # 3. 将yield后的数据，作为__next__的返回值
        print("准备")
        yield self.__skills[0]
        print("准备")
        yield self.__skills[1]
        print("准备")
        yield self.__skills[2]

        # for i in self.__skills:
        #     yield i


manager = SkillManager()
manager.add_skill("skill01")
manager.add_skill("skill02")
manager.add_skill("skill03")

iterator = manager.__iter__()

while True:
    try:
        print(iterator.__next__())
    except StopIteration:
        break
