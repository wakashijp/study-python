fruits = []  # 空で試してみる
# 例外処理に組み込む
try:
    dessert = fruits.pop()
    print("デザートは" + dessert)
    print(fruits)
except IndexError:
    print("エラーになりました。")
