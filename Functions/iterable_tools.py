"""
    可迭代对象工具模块
"""


class IterableHelper:
    """
        可迭代对象助手
    """

    @staticmethod
    def find_all(iterable, func_cond):
        """
            在可迭代对象中查找满足条件的所有元素
        :param iterable: 可迭代对象类型，需要查找的数据
        :param func_cond: 函数类型，查找的条件
        :return: 生成器对象
        """
        for i in iterable:
            if func_cond(i):
                yield i

    @staticmethod
    def find_first(iterable, func_cond):
        """
            在可迭代对象中查找第一个满足条件的元素
        :param iterable: 可迭代对象类型，需要查找的数据
        :param func_cond: 函数类型，查找的条件
        :return: 第一个满足条件的元素
        """
        for i in iterable:
            if func_cond(i):
                return i

    @staticmethod
    def get_count(iterable, func_cond):
        """
            在可迭代对象中，获取满足条件的元素数量
        :param iterable: 可迭代对象类型，需要查找的数据
        :param func_cond: 函数类型，查找的条件
        :return: int类型，数量
        """
        count = 0
        for i in iterable:
            if func_cond(i):
                count += 1
        return count

    @staticmethod
    def select(iterable, func_handle):
        """
            通用筛选方法
        :param iterable: 可迭代对象类型，需要查找的数据
        :param func_handle: 筛选的逻辑
        :return: 生成器对象
        """
        for i in iterable:
            yield func_handle(i)

    @staticmethod
    def is_exist(iterable, func_cond):
        """
             判断可迭代对象中是否存在满足某个条件的对象
        :param iterable: 可迭代对象类型，需要查找的数据
        :param func_cond: 查找的条件
        :return: bool，True为存在，False为不存在
        """
        for i in iterable:
            if func_cond(i):
                return True
        return False

    @staticmethod
    def sum(iterable, func_handle):
        """
            根据指定逻辑累加可迭代对象中的元素
        :param iterable: 可迭代对象类型，需要累加的数据
        :param func_handle: 累加逻辑
        :return: 数值类型，累加结果
        """
        total = 0
        for i in iterable:
            total += func_handle(i)
        return total

    @staticmethod
    def get_max(iterable, func_handle):
        """
            根据指定逻辑筛选出值最大的元素
        :param iterable: 可迭代对象类型，需要筛选的数据
        :param func_handle: 筛选逻辑
        :return: 值最大的对象
        """
        max_value = iterable[0]
        for i in range(1, len(iterable)):
            if func_handle(iterable[i]) > func_handle(max_value):
                max_value = iterable[i]
        return max_value

    @staticmethod
    def delete(iterable, func_handle):
        """
            根据条件删除多个元素
        :param iterable: 可迭代对象类型，需要查找的数据
        :param func_handle: 删除元素的条件
        :return: 删除元素后的列表
        """
        for i in range(len(iterable)-1, -1, -1):
            if func_handle(iterable[i]):
                del iterable[i]
        return iterable
