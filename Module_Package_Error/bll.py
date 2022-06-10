# business logic layer: 业务逻辑层

class StudentManagerController:
    """
        学生管理控制器：主要负责业务逻辑处理
    """
    init_id = 1000

    @classmethod
    def __generate_id(cls, stu):
        stu.id = cls.init_id
        cls.init_id += 1

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self, stu):
        """
            添加学生信息
        :param stu: 需要添加的学生对象
        """
        StudentManagerController.__generate_id(stu)
        self.__stu_list.append(stu)

    def remove_student(self, stu_id):
        """
            移除学生信息
        :param stu_id: 需要移除的学生的编号
        :return: 是否移除成功
        """
        for i in self.__stu_list:
            if i.id == stu_id:
                self.__stu_list.remove(i)
                return True
        return False

    def update_student(self, new_stu):
        """
            修改学生信息
        :param new_stu: 需要修改信息的学生
        :return: 是否修改成功
        """
        for i in self.__stu_list:
            if i.id == new_stu.id:
                i.name = new_stu.name
                i.age = new_stu.age
                i.score = new_stu.score
                return True
        return False

    def order_by_score(self):
        """
            根据成绩升序排列
        """
        lst = self.__stu_list[:]  # 拷贝
        for i in range(len(lst) - 1):
            for j in range(len(lst) - 1 - i):
                if lst[j].score > lst[j + 1].score:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
        return lst
