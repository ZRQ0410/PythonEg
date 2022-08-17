"""
    l1, l2均为顺序链表，合并后的链表仍为顺序
"""

from linkedlist import *
l1 = LinkedList()
l2 = LinkedList()

l1.init_list([1, 5, 7, 8, 10, 12, 13, 19])  # 顺序
l2.init_list([2, 3, 4, 9, 16, 17, 20])  # 顺序
# l2.init_list([0, 5, 5, 6, 20, 21, 22])


def merge(l1, l2):
    # 将l2合并到l1中
    p = l1.head
    q = l2.head.next
    while p.next is not None:
        if p.next.val < q.val:
            p = p.next
        else:
            tmp = p.next
            p.next = q
            q = tmp
            p = p.next
    p.next = q


l1.show()
l2.show()
# combine(l1, l2)
# l1.show()
merge(l1, l2)
l1.show()
