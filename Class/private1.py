"""
    __init__中调用setter
"""
class Wife:
    def __init__(self, name, age):
        self.name = name
        # _Wife__age
        self.set_age(age)

    def get_age(self):
        return self.__age
    
    def set_age(self, val):
        if 21<= val <=31:
            self.__age = val
        else:
            raise ValueError("invalid")

w01 = Wife('aa', 25)
print(w01.__dict__)
print(w01.get_age())
# w01.set_age(80) # error: invalid