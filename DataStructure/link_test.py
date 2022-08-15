from linkedlist import *
import time

# 数据量较大时：
# 列表遍历快
l = range(200000)
tm = time.time()
for i in l:
    print(i)
a = time.time() - tm


# 链表遍历慢
link = LinkedList()
link.init_list(l)
tm = time.time()
link.show()
b = time.time() - tm

print("\n列表遍历用时{}s，链表遍历用时{}s".format(a, b))
