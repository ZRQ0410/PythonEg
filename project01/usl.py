# user show layer 游戏界面逻辑模块
import os

from bll import GameCoreController


class GameConsoleView:
    """
        控制台界面类
    """

    def __init__(self):
        self.__controller = GameCoreController()

    def __start(self):
        self.__controller.generate_new_num()
        self.__controller.generate_new_num()
        print("需上下左右移动，请输入wsad。无输入则退出。")
        self.__show_map()

    def __move(self):
        direction = input("方向：")
        if direction == "w":
            self.__controller.move_up()
        elif direction == "s":
            self.__controller.move_down()
        elif direction == "a":
            self.__controller.move_left()
        elif direction == "d":
            self.__controller.move_right()
        elif direction == "":
            print("已退出。")
            return 999
        else:
            print("输入错误。")
            return -999

    def __update(self):
        while True:
            is_end = self.__move()
            if is_end == 999:
                break
            elif is_end == 999:
                continue
            else:
                print()
                self.__controller.generate_new_num()
                self.__show_map()

            if self.__controller.is_game_over():
                print("游戏结束。")
                break

    def __show_map(self):
        # os.system("clear")  # 清空屏幕。要在终端才能运行，否则会报错
        for r in self.__controller.map:
            for c in r:
                print(c, end="\t")
            print()

    def main(self):
        self.__start()
        self.__update()
