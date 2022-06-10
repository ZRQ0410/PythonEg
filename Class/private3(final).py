"""
    使用property, 封装变量
"""
class Wife:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.__score = 200

    # __age: getter & setter
    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, val):
        if 21 <= val <= 31:
            self.__age = val
        else:
            raise ValueError("invalid")

    # __score: read only
    @property
    def score(self):
        return self.__score

    # __weight: write only
    def set_weight(self, val):
        self.__weight = val
    weight = property(None, set_weight)


w01 = Wife('aa', 24, 100)
print(w01.age)
print(w01.score)
