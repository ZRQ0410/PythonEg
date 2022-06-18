# business logic layer: 业务逻辑层

"""
    游戏核心逻辑控制器
"""
from binascii import b2a_hex
import random
import copy

from model import LocationModel


# 装饰器函数，确认是否可以向某个方向移动
def valid_move(func):
    def wrapper(self, *args, **kargs):
        temp = copy.deepcopy(self.map)
        func(self, *args, **kargs)
        if temp == self.map:
            self.valid_movement = False
            return
        self.valid_movement = True
    return wrapper


class GameCoreController:
    def __init__(self):
        self.__list_merge = None
        self.__map = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]
        self.__list_empty_location = []
        self.valid_movement = False

    @property
    def map(self):
        return self.__map

    @property
    def valid_movement(self):
        return self.__valid_movement

    @valid_movement.setter
    def valid_movement(self, b):
        self.__valid_movement = b

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
                self.__list_merge[i], self.__list_merge[i +
                                                        1] = self.__list_merge[i] * 2, 0
        self.__zero_to_end()

    def __transpose(self):
        """
            方阵转置
        """
        for i in range(len(self.__map)):
            for j in range(i + 1, len(self.__map)):
                self.__map[i][j], self.__map[j][i] = self.__map[j][i], self.__map[i][j]


# =============================================================================


# =============================================================================

    @valid_move
    def __move_left(self):
        """
            向左移动
        """
        for self.__list_merge in self.__map:
            self.__merge()

    @valid_move
    def __move_right(self):
        """
            向右移动
        """
        for self.__list_merge in self.__map:
            self.__list_merge.reverse()
            self.__merge()
            self.__list_merge.reverse()

    def __move_up(self):
        """
            向上移动(包含向左移动)
        """
        self.__transpose()
        self.__move_left()
        self.__transpose()

    def __move_down(self):
        """
            向下移动(包含向右移动)
        """
        self.__transpose()
        self.__move_right()
        self.__transpose()

    def move(self, dir):
        if dir == "w":
            self.__move_up()
        elif dir == "a":
            self.__move_left()
        elif dir == "d":
            self.__move_right()
        else:
            self.__move_down()

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
        self.__map[loc.r][loc.c] = self.__select_random_num()

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
