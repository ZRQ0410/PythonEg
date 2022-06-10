"""
    信息管理系统
    MVC架构:
    界面视图类(view): StudentManagerView
                 行为: __display_menu  __select_menu
                      入口逻辑 main  输入学生信息 __input_students
                      显示学生信息 __output_students
                      删除学生信息 __delete_students
                      修改学生信息 __modify_students
    数据模型类(model): StudentModel
                 数据: name, age, score, id(逻辑控制自增)
    逻辑控制类(controller): StudentManagerController
                 数据: 学生列表__stu_list
                 行为: 获取列表 stu_list  添加学生 add_student
                      删除学生 remove_student  修改学生 update_student
                      根据学生排序 oder_by_score
"""

import time


class StudentModel:
    """
        学生数据模型类
    """

    def __init__(self, name="", age=0, score=0, id=0):
        """
            创建学生对象
        """
        self.name = name
        self.age = age
        self.score = score
        self.id = id

        @property
        def name(self):
            return self.__name

        @name.setter
        def name(self, val):
            self.__name = val

        @property
        def age(self):
            return self.__age

        @age.setter
        def age(self, val):
            self.__age = val

        @property
        def score(self):
            return self.__score

        @score.setter
        def score(self, val):
            self.__score = val

        @property
        def id(self):
            return self.__id

        @id.setter
        def score(self, val):
            self.__id = val


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
        :param stu: 需要添加的学生对象(可以没有编号)
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
        for i in range(len(lst) - 1):  # 冒泡排序
            for j in range(len(lst) - 1 - i):
                if lst[j].score > lst[j + 1].score:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
        return lst


class StudentManagerView:
    """
        学生管理视图：主要负责界面逻辑
    """

    def __init__(self):
        self.__controller = StudentManagerController()
        self.end = True

    @staticmethod
    def __display_menu():
        print("""
+--------------------------------+
| 1) 添加学生信息                |
| 2) 显示学生信息                |
| 3) 删除学生信息                |
| 4) 修改学生成绩                |
| 5) 按学生成绩低到高显示学生信息|
| 6) 退出                        |
+--------------------------------+""")

    def __select_menu(self):
        choice = input("请输入选项：")
        if choice in ['1', '2', '3', '4', '5', '6']:
            if choice == '1':
                self.__input_students()
            elif choice == '2':
                self.__output_students(self.__controller.stu_list)
            elif choice == '3':
                self.__delete_students()
            elif choice == '4':
                self.__modify_students()
            elif choice == '5':
                self.__output_students_order_by_score()
            else:
                print("已退出。")
                self.end = False
        else:
            print("请输入正确序号！")
            time.sleep(0.3)

    def main(self):
        while self.end:
            self.__display_menu()
            self.__select_menu()

    def __input_students(self):
        name = input("学生姓名：")
        age = int(input("学生年龄："))
        score = int(input("学生成绩："))
        stu = StudentModel(name, age, score)
        self.__controller.add_student(stu)
        time.sleep(0.2)
        print("添加成功。")
        time.sleep(0.5)

    @staticmethod
    def __output_students(lst):
        print("%5s\t%5s\t%5s\t%5s" % ("编号", "姓名", "年龄", "分数"))
        for i in lst:
            print("%5d\t%5s\t%5d\t%5d" % (i.id, i.name, i.age, i.score))
        time.sleep(0.5)

    def __delete_students(self):
        stu_id = int(input("输入学生编号："))
        time.sleep(0.2)
        if self.__controller.remove_student(stu_id):
            print("删除成功。")
        else:
            print("删除失败。")
        time.sleep(0.5)

    def __modify_students(self):
        stu = StudentModel()
        stu.id = int(input("需要修改的学生编号："))
        stu.name = input("需要修改的学生姓名：")
        stu.age = int(input("需要修改的学生年龄："))
        stu.score = int(input("需要修改的学生分数："))
        time.sleep(0.2)
        if self.__controller.update_student(stu):
            print("修改成功。")
        else:
            print("修改失败。")
        time.sleep(0.5)

    def __output_students_order_by_score(self):
        lst = self.__controller.order_by_score()
        self.__output_students(lst)
        time.sleep(0.5)


view = StudentManagerView()
view.main()
