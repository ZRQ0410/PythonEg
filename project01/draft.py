class Testing:

    def check(func):
        def wrapper(self):
            print(2222222)
            move(self)

    @check
    def move(self):
        print(111)
