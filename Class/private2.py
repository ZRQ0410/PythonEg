"""
    使用property读取、写入方法, 封装变量
"""
class Wife:
    def __init__(self, name, age, weight):
        self.name = name
        # 类变量age, weight
        self.age = age
        self.weight = weight

    def get_age(self):
        return self.__age

    def set_age(self, val):
        if 21 <= val <= 31:
            self.__age = val
        else:
            raise ValueError("invalid")

    def set_weight(self, val):
        self.__weight = val

    age = property(get_age, set_age)
    weight = property(None, set_weight)

w01 = Wife('aa', 25, 100)
w01.age = 30
print(w01.age)
print(w01.__dict__)

# print(w01.weight) # error: unreadable