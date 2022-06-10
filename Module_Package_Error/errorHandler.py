class ErrorHandler:
    @staticmethod
    def age_checker(data):
        try:
            age = int(data)
        except:
            print("请输入数字。")
            return -999
        if 0 < age <= 100:
            return age
        print("请输入正确年龄。")
        return -999

    @staticmethod
    def score_checker(data):
        try:
            score = int(data)
        except:
            print("请输入数字。")
            return -999
        if 0 <= score <= 100:
            return score
        print("请输入正确分数。")
        return -999

    @staticmethod
    def id_checker(data):
        try:
            id = int(data)
        except:
            print("请输入数字。")
            return -999
        if id >= 1000:
            return id
        print("请输入正确编号。")
        return -999