"""
    二分查找

前提：数据必须有序
"""


# list_ 为有序数列，key为要查找的关键值，返回key在数列中的索引号
def bisearch(list_, key):
    low, high = 0, len(list_)-1
    while low < high:
        mid = (low+high) // 2
        if key > list_[mid]:
            low = mid+1
        elif key < list_[1]:
            high = mid-1
        else:
            return mid


l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("key index:", bisearch(l, 8))
