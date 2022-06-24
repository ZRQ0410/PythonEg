from enum import Enum, unique


class LocationModel:
    """
        位置模型
    """

    def __init__(self, r, c):
        self.row = r
        self.col = c


# unique:防止两个name有相同的value
@unique
class DirectionModel(Enum):
    UP = "w"
    DOWN = "s"
    LEFT = "a"
    RIGHT = "d"
