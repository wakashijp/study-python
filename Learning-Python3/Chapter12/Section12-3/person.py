class Person:
    def __init__(self, name):
        self.__name = name  # 非公開インスタンス変数
    
    def who(self):
        print(self.__name + "です")
