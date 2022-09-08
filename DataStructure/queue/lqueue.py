"""
    queue 队列的链式存储

1. 基于链表构建队列模型
2. 链表的开头作为队头，结尾位置作为队尾
3. 单独定义队尾标记，避免每次插入数据都要遍历
4. 当队头和队尾重叠时，队列为空
"""


# 自定义队列异常
class QueueError(Exception):
    pass


#  节点类
class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LQueue:
    def __init__(self):
        # 定义队头和队尾
        self.front = self.rear = Node(None)

    def enqueue(self, val):
        self.rear.next = Node(val)
        self.rear = self.rear.next

    def dequeue(self):
        if self.front == self.rear:
            raise QueueError("Queue is empty")
        self.front = self.front.next
        return self.front.val  # front指向的节点已经出队

    def is_empty(self):
        return self.front == self.rear


if __name__ == "__main__":
    lq = LQueue()
    lq.enqueue(10)
    lq.enqueue(20)
    lq.enqueue(30)
    print(lq.dequeue())
