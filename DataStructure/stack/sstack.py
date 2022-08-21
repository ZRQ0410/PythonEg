"""
    stack 栈模型的顺序存储

1. 顺序存储 -> 列表，但需要只允许在一端操作数据
2. 利用列表将其封装，提供接口方法
"""


# 自定义异常
class StackError(Exception):
    pass


# 顺序栈类
class SStack:
    def __init__(self):
        # 空列表作为栈的存储空间
        # 列表最后一个元素作为栈顶
        self._elems = []

    def is_empty(self):
        return self._elems == []

    # 入栈
    def push(self, val):
        self._elems.append(val)

    # 出栈
    def pop(self):
        if self.is_empty():
            raise StackError("Stack is empty")
        # 弹出并返回
        return self._elems.pop()

    # 查看栈顶元素
    def top(self):
        if self.is_empty():
            raise StackError("Stack is empty")
        return self._elems[-1]


if __name__ == "__main__":
    st = SStack()
    st.push(10)
    st.push(20)
    st.push(30)
    while not st.is_empty():
        print(st.pop())
