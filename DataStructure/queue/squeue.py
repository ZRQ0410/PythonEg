"""
    queue 队列的顺序存储

1. 基于列表的数据存储
2. 通过封装规定数据操作
3. 定义列表尾部为队尾，头部为队头
"""


# 自定义队列异常
class QueueError(Exception):
    pass


class SQueue:
    def __init__(self):
        self._elems = []

    # 从尾部入队
    def enqueue(self, val):
        self._elems.append(val)

    # 从头部出队
    def dequeue(self):
        if not self._elems:
            raise QueueError("Queue is empty")
        return self._elems.pop(0)

    # 判断队列为空
    def is_empty(self):
        return self._elems == []


if __name__ == "__main__":
    sq = SQueue()
    # sq.enqueue(10)
    # sq.enqueue(20)
    # sq.enqueue(30)
    # while not sq.is_empty():
    #     print(sq.dequeue())

    import sys
    sys.path.append(
        "c:\\Users\\12927\\Desktop\\PythonNote\\CourseEg\\DataStructure")

    ######## 将队列翻转 ########
    for i in range(10):
        sq.enqueue(i)
    # 翻转队列顺序
    from stack.sstack import *
    st = SStack()
    while not sq.is_empty():
        st.push(sq.dequeue())
    while not st.is_empty():
        sq.enqueue(st.pop())

    while not sq.is_empty():
        print(sq.dequeue())
