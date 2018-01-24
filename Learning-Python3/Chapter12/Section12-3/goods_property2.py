class Goods:
    # 初期化メソッド
    def __init__(self, name, price):
        self.__data = {"name": name, "price": price}

    # nameプロパティのゲッター
    def get_name(self):
        return self.__data["name"]

    # nameプロパティのセッター
    def set_name(self, value):
        self.__data["name"] = value

    # priceのプロパティのゲッター
    def get_price(self):
        price = self.__data["price"]
        price_str = f"{price:,}円"
        return price_str

    # プロパティの設定
    name = property(get_name, set_name)  # nameプロパティのゲッター／セッターを指定します
    price = property(get_price)  # priceプロパティのゲッターを指定します。
