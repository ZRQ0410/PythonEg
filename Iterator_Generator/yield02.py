class MyRange:
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        num = -1
        while num < self.count - 1:
            num += 1
            yield num


for i in MyRange(5):
    print(i)
