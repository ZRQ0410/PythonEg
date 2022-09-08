"""
    linked list
    功能：单链表的构建和功能操作
"""


# 创建节点类
class Node:
    """
    实例对象中包含数据部分和指向下一个节点的部分
    """

    def __init__(self, val, next=None):
        self.val = val  # 存储数据
        self.next = next  # 下一个节点


class LinkedList:
    """
    单链表类，生成对象可进行增删改查操作
    """

    def __init__(self):
        """
        初始化链表，标记一个链表的开端，以便获取后续节点
        """
        self.head = Node(None)  # 表头

    # 通过list_为链表初始化一组节点
    def init_list(self, list_):
        p = self.head  # 移动变量
        for item in list_:
            p.next = Node(item)
            p = p.next

    # 遍历打印链表
    def show(self):
        p = self.head
        # for i in range(self.length()):
        #     print(p.val)
        #     p = p.next
        while p.next is not None:
            p = p.next
            print(p.val, end=" ")
        print()

    # 判断列表是否为空
    def is_empty(self):
        if self.head.next is None:
            return True
        return False

    # 清空链表
    def clear(self):
        self.head.next = None

    # 返回链表长度
    def length(self):
        p = self.head.next
        num = 0
        while p is not None:
            num += 1
            p = p.next
        return num

    # 尾部插入(非空时)
    def append(self, val):
        p = self.head.next
        while p.next is not None:
            p = p.next
        p.next = Node(val)

    # 插入到开头（非空时）
    def head_insert(self, val):
        temp = self.head.next
        self.head.next = Node(val, temp)

    # 插入到某位置（非空时）
    def insert(self, index, val):
        p = self.head
        for i in range(index):
            if p.next is None:
                # 超出最大范围结束循环
                break
            p = p.next
        temp = p.next
        p.next = Node(val, temp)

    # 根据值删除节点
    def remove(self, val):
        p = self.head
        while p.next and p.next.val != val:
            p = p.next
        if p.next is None:
            raise ValueError("value not in linked list")
        else:
            p.next = p.next.next

    # 传入节点位置，获取节点值
    def get_val(self, index):
        if self.is_empty():
            raise IndexError("linked list index out of range")
        p = self.head.next
        for i in range(index):
            if p.next is None:
                raise IndexError("linked list index out of range")
            p = p.next
        return p.val


# testing
if __name__ == "__main__":
    ll = LinkedList()
    ll.init_list([2, 5, 3, 8, 6])
    ll.head_insert(11)
    ll.insert(2, 20)
    ll.remove(100)
    print(ll.get_val(2))
    ll.show()
