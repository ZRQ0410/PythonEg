class AgeRangeError(Exception):
    def __init__(self, name="", error_id=0, error_code=""):
        super().__init__("出错啦")
        self.name = name
        self.error_id = error_id
        self.error_code = error_code


class Wife:
    def __init__(self, name="", age=0):
        self.name = name
        # self.age = age
        self.set_age(age)

    def get_age(self):
        return self.__age

    def set_age(self, value):
        if 20 <= value <= 30:
            self.__age = value
        else:
            raise AgeRangeError(
                "年龄超过范围错误", 1324, "if 20 <= value <= 30:")  # 报错


a = Wife('a', 40)  # run without debugging -- see error message
# try:
#     a = Wife('a', 40)
# except AgeRangeError as e:
#     print(e.args)
#     print(e.name)
