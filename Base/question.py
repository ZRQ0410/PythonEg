# 解释器会将函数定义到方法区（存储一份），连同默认参数一起创建
# 所以不指定参数时，使用的就是那一份列表（同一份列表继续用）
# 总结：默认参数，不要使用可变对象
def fun01(x, list_target=[]):
    for i in range(x):
        list_target.append(i)
    print(list_target)


fun01(3)
fun01(4)
