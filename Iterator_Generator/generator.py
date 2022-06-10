"""
    生成器
"""

"""
    # 生成器: 可迭代对象(可以参与for) + 迭代器(产生数据)
    class Generator:
        def __init__(self):
            return self
            
        def __next__(self):
            ...
"""


def my_range(count):
    num = -1
    while num < count - 1:
        num += 1
        yield num


# for i in my_range(5):
#     print(i)

generator = my_range(5)
print(generator)  # <generator object my_range at 0x7f2a3d1f1660>
iterator = generator.__iter__()
while True:
    try:
        print(iterator.__next__())
    except StopIteration:
        break
