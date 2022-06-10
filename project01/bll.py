# business logic layer: 业务逻辑层

"""
    游戏核心逻辑控制器
"""
import random

from project01.model import LocationModel


class GameCoreController:
    def __init__(self):
        self.__list_merge = None
        self.__map = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]
        self.__list_empty_location = []

    @property
    def map(self):
        return self.__map

    def __zero_to_end(self):
        """
            零元素移动到末尾，默认为向左移动的情况
        """
        for i in range(len(self.__list_merge) - 1, -1, -1):
            if self.__list_merge[i] == 0:
                self.__list_merge.append(self.__list_merge.pop(i))

    def __merge(self):
        """
            合并，默认为向左移动的情况
        """
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i], self.__list_merge[i + 1] = self.__list_merge[i] * 2, 0
        self.__zero_to_end()

    def move_left(self):
        """
            将二维列表中的元素向左移动
        """
        for self.__list_merge in self.__map:
            self.__merge()

    def move_right(self):
        """
            向右移动
        """
        for self.__list_merge in self.__map:
            self.__list_merge.reverse()
            self.__merge()
            self.__list_merge.reverse()

    def __transpose(self):
        """
            方阵转置
        """
        for i in range(len(self.__map)):
            for j in range(i + 1, len(self.__map)):
                self.__map[i][j], self.__map[j][i] = self.__map[j][i], self.__map[i][j]

    def move_up(self):
        """
            向上移动
        """
        self.__transpose()
        self.move_left()
        self.__transpose()

    def move_down(self):
        """
            向下移动
        """
        self.__transpose()
        self.move_right()
        self.__transpose()

    def __calculate_empty_location(self):
        self.__list_empty_location.clear()
        for r in range(len(self.__map)):
            for c in range(len(self.__map[r])):
                if self.__map[r][c] == 0:
                    self.__list_empty_location.append(LocationModel(r, c))

    def __select_random_num(self):
        return 4 if random.randint(1, 10) == 1 else 2

    def generate_new_num(self):
        """
            在空位置随机产生2(90%)或4(10%)
        """
        self.__calculate_empty_location()
        if len(self.__list_empty_location) == 0:
            return
        loc = random.choice(self.__list_empty_location)
        self.map[loc.r][loc.c] = self.__select_random_num()

    # 判断游戏是否结束
    def is_game_over(self):
        if len(self.__list_empty_location) > 0:
            return False
        for r in range(len(self.__map)):
            for c in range(len(self.__map) - 1):
                if self.__map[r][c] == self.map[r][c + 1]:
                    return False
        for c in range(len(self.__map)):
            for r in range(len(self.__map) - 1):
                if self.__map[r][c] == self.map[r + 1][c]:
                    return False
        return True


# 主模块才执行
if __name__ == "__main__":
    controller = GameCoreController()
    # controller.generate_new_num()
    # controller.generate_new_num()

    print(controller.is_game_over())
