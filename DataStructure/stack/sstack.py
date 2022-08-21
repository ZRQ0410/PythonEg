"""
    stack 栈模型的顺序存储

1. 顺序存储 -> 列表，但需要只允许在一端操作数据
2. 利用列表将其封装，提供接口方法
"""


# 顺序栈类
class SStack:
    def __init__(self):
        # 空列表作为栈的存储空间
        # 列表最后一个元素作为栈顶
        self._elems = []


if __name__ == "__main__":
    st = SStack()
