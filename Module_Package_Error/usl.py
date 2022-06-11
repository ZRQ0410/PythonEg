# user show layer: 用户显示层
from bll import StudentManagerController
from model import StudentModel
from errorHandler import ErrorHandler
import time


class StudentManagerView:
    """
        学生管理视图：主要负责界面逻辑
    """

    def __init__(self):
        self.__controller = StudentManagerController()
        self.end = True

    @staticmethod
    def __display_menu():
        print("""+--------------------------------+
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
        while True:
            age = input("学生年龄：")
            age = ErrorHandler.age_checker(age)
            if age != -999:
                break
        while True:
            score = input("学生成绩：")
            score = ErrorHandler.score_checker(score)
            if score != -999:
                break
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
        while True:
            stu_id = input("输入学生编号：")
            stu_id = ErrorHandler.id_checker(stu_id)
            if stu_id != -999:
                break
        time.sleep(0.2)
        if self.__controller.remove_student(stu_id):
            print("删除成功。")
        else:
            print("删除失败。")
        time.sleep(0.5)

    def __modify_students(self):
        stu = StudentModel()
        while True:
            stu.id = input("需要修改的学生编号：")
            stu.id = ErrorHandler.id_checker(stu.id)
            if stu.id != -999:
                break
        stu.name = input("需要修改的学生姓名：")
        while True:
            stu.age = input("需要修改的学生年龄：")
            stu.age = ErrorHandler.age_checker(stu.age)
            if stu.age != -999:
                break
        while True:
            stu.score = input("需要修改的学生分数：")
            stu.score = ErrorHandler.score_checker(stu.score)
            if stu.score != -999:
                break
        time.sleep(0.2)
        if self.__controller.update_student(stu):
            print("修改成功。")
        else:
            print("修改失败，无此编号。")
        time.sleep(0.5)

    def __output_students_order_by_score(self):
        lst = self.__controller.order_by_score()
        self.__output_students(lst)
        time.sleep(0.5)
