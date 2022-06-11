"""
    迭代器
"""


# 创建一个迭代器对象: Iterator
class MyRangeIterator:
    def __init__(self, count):
        self.count = count
        self.index = -1

    def __next__(self):
        self.index += 1
        if self.index > self.count - 1:
            raise StopIteration
        return self.index


# 创建一个可迭代对象: Iterable
class MyRange:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        return MyRangeIterator(self.count)  # 返回迭代器对象


# 循环一次 调用一次 销毁一次 故即使是MyRange(9999999)也不会占用过多内存
for i in MyRange(5):
    print(i)
