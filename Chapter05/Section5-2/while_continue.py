# randomモジュールからrandint関数を読み込む
from random import randint

numbers = []  # 空のリスト

# numbersの値が10個になるまで繰り返す
while len(numbers) < 10:
    n = randint(0, 100)  # 0〜100の乱数を生成する
    if n in numbers:
        # n がnumbersに含まれていたらスキップする
        continue  # 既に含まれている値は追加せずに処理をスキップします

    # numbersに n を追加する
    numbers.append(n)  # 初めての数値ならばnumbersリストに追加します

print(numbers)
