# Carクラス
class Car:
    # クラス変数
    maker = "PEACE"  # 自動車メーカー
    count = 0  # 台数

    # クラスメソッド
    @classmethod
    def countup(cls):
        cls.count += 1
        print(f"出荷台数：{cls.count}")

    # 初期化メソッド
    def __init__(self, color="white"):
        Car.countup()  # カウントアップする - クラスメソッドを実行しています
        self.mynumber = Car.count  # 自分の番号 - クラス変数を参照しています
        self.color = color  # 引数で受け取った値を代入
        self.mileage = 0  # 0からスタート

    # インスタンスメソッド
    def drive(self, km):
        self.mileage += km
        msg = f"{km}kmドライブしました。総距離は{self.mileage}kmです。"
        print(msg)
