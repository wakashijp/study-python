# randomモジュールからrandint関数を読み込む
from random import randint

numbers = []  # 空のリスト

# numbersの値が10個になるまで繰り返す
while len(numbers) < 10:
    n = randint(-10, 90)  # -10〜90の乱数を生成する
    if n < 0:
        # nがマイナスならばブレイクする
        print("中断されました")
        break  # elseブロックを実行せずに終了します

    if n in numbers:
        # nがnumbersに含まれていたらスキップする
        continue

    # numbersにnを追加する
    numbers.append(n)
else:
    print(numbers)  # 繰り返しが終わったら実行します
