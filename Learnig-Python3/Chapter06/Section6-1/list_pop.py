fruits = ["apple", "orange", "banana", "peach"]
# fruitsが空でないかチェックする
if fruits:  # リストが空の時はFalseになります
    dessert = fruits.pop()  # fruitsのリストから最後の要素を取り出しています
    print("デザートは" + dessert)

print(fruits)
