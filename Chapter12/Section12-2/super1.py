# スーパークラス
class Person:
    def __init__(self, name, age):  # このままではスーパークラスの初期化メソッドは実行されません
        self.name = name
        self.age = age


# サブクラス
class Player(Person):
    def __init__(self, number, position):
        self.number = number
        self.position = position
