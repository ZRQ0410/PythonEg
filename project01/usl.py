# user show layer 游戏界面逻辑模块

from bll import GameCoreController
import os


class GameConsoleView:
    """
        控制台界面类
    """

    def __init__(self):
        self.__controller = GameCoreController()

    def __start(self):
        # 产生两个数字，绘制界面
        self.__controller.generate_new_num()
        self.__controller.generate_new_num()
        print("需上下左右移动，请输入wsad。无输入则退出。")
        # 绘制界面
        self.__show_map()

    def __move(self):
        valid_dir = ["w", "a", "s", "d"]
        direction = input("方向：")
        if direction in valid_dir:
            self.__controller.move(direction)
            if not self.__controller.valid_movement:
                print("不能向此方向移动。")
                return -999
        elif direction == "":
            print("已退出。")
            return 999
        else:
            print("输入错误。")
            return -999

    def __update(self):
        while True:
            if self.__controller.is_game_over():
                print("游戏结束。")
                break

            is_end = self.__move()
            if is_end == 999:
                break
            elif is_end == -999:
                continue
            else:
                print()
                self.__controller.generate_new_num()
                self.__show_map()

    def __show_map(self):
        # 清空屏幕: 要在终端才能运行，否则会报错
        # windows命令cls，linux命令clear
        # os.system("cls")
        for r in self.__controller.map:
            for c in r:
                print(c, end="\t")
            print()

    def main(self):
        self.__start()
        self.__update()
