"""
    2048核心算法
"""

map = [[2, 0, 0, 2],
       [2, 4, 4, 2],
       [0, 4, 2, 0],
       [2, 0, 2, 0]]

list_merge = []


def zero_to_end():
    """
    零元素移动到末尾
    """
    for i in range(len(list_merge) - 1, -1, -1):
        if list_merge[i] == 0:
            list_merge.append(list_merge.pop(i))


def merge():
    """
    合并
    """
    zero_to_end()
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            list_merge[i], list_merge[i + 1] = list_merge[i] * 2, 0
    zero_to_end()


def move_left():
    """
    将二维列表中的元素向左移动
    """
    global list_merge
    for list_merge in map:
        merge()


def move_right():
    """
    向右移动
    """
    global list_merge
    for list_merge in map:
        list_merge.reverse()
        merge()
        list_merge.reverse()


def transpose():
    """
    方阵转置
    """
    for i in range(len(map)):
        for j in range(i + 1, len(map)):
            map[i][j], map[j][i] = map[j][i], map[i][j]


def move_up():
    """
    向上移动
    """
    transpose()
    move_left()
    transpose()


def move_down():
    """
    向下移动
    """
    transpose()
    move_right()
    transpose()


move_down()
print(map)
