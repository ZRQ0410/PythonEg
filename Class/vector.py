"""
    二维向量处理 + static method
"""


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def right():
        return Vector2(0, 1)

    @staticmethod
    def up():
        return Vector2(-1, 0)

    @staticmethod
    def left():
        return Vector2(0, -1)

    @staticmethod
    def down():
        return Vector2(1, 0)


class DoubleListHelper:
    @staticmethod
    def get_elements(list_target, vect_pos, vect_dir, count):
        """
            在二维列表中获取指定位置、方向、数量的元素
        :param list_target: 二维列表
        :param vect_pos: 指定位置
        :param vect_dir: 指定方向
        :param count: 指定数量
        :return: 列表
        """
        list_result = []
        for i in range(count):
            vect_pos.x += vect_dir.x
            vect_pos.y += vect_dir.y
            element = list_target[vect_pos.x][vect_pos.y]
            list_result.append(element)
        return list_result


# Testing
list01 = [
    ["00", "01", "02", "03", "04"],
    ["10", "11", "12", "13", "14"],
    ["20", "21", "22", "23", "24"],
    ["30", "31", "32", "33", "34"]
]

print(DoubleListHelper.get_elements(list01, Vector2(3, 0), Vector2.right(), 3))
print(DoubleListHelper.get_elements(list01, Vector2(3, 2), Vector2.up(), 3))
print(DoubleListHelper.get_elements(list01, Vector2(3, 4), Vector2.left(), 4))
