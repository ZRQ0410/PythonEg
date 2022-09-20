# 冒泡排序（从小到大）
def bubbleSort(list_):
    # 表示比较多少轮
    for i in range(len(list_)-1):
        # 比较第0~N-1个, 0~N-2, 0~N-3 ...
        for j in range(len(list_)-1-i):
            if list_[j] > list_[j+1]:  # 若要从大到小排序改为<即可
                list_[j], list_[j+1] = list_[j+1], list_[j]


# 选择排序
def selectionSort(list_):
    for i in range(len(list_)-1):
        min_pos = i
        for j in range(i+1, len(list_)):
            if list_[j] < list_[min_pos]:
                min_pos = j
        if min_pos != i:
            list_[i], list_[min_pos] = list_[min_pos], list_[i]


# 插入排序
def insertSort(list_):
    for i in range(1, len(list_)):
        tmp = list_[i]
        for j in range(i-1, -1, -1):
            if tmp < list_[j]:
                list_[j+1] = list_[j]
                if j == 0:
                    list_[0] = tmp
            else:
                list_[j+1] = tmp
                break


def sub_sort(list_, low, high):
    # 选定基准
    x = list_[low]
    # low向后，high向前
    while low < high:
        # 如果后面的数比x小，往前放
        while list_[high] >= x and high > low:
            high -= 1
        list_[low] = list_[high]
        # 如果前面的数比x大或一样大，往后放
        while list_[low] <= x and low < high:
            low += 1
        list_[high] = list_[low]
    # 当low和high相等时
    list_[low] = x
    return low


# 快速排序
def quickSort(list_, low, high):
    if low < high:
        key = sub_sort(list_, low, high)
        quickSort(list_, low, key-1)
        quickSort(list_, key+1, high)


# Eg. 4 1 3 2 1
l = [4, 9, 3, 1, 2, 5, 8, 4]
quickSort(l, 0, len(l)-1)
print(l)
