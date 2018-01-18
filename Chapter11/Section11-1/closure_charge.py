# クロージャの定義
def charge(price):
    # 関数の実態
    def calc(num):
        return price * num
    return calc


# クロージャ（関数オブジェクト）を2個作る
child = charge(400)  # 子供料金 400円
adult = charge(1200)  # 大人料金 1200円

# 料金を計算する
price1 = child(3)  # 子供3人 - charge(400)で作られた関数を使って計算します
price2 = adult(2)  # 大人2人 - charge(1200)で作られた関数を使って計算します

print(price1)
print(price2)
