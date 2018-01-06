# randomモジュールからrandint関数を読み込む
from random import randint

miss = 0  # 間違えた数
correct = 0  # 正解数

print("問題！3回間違えたら終了。qで止める")

while miss < 3:
    a = randint(1, 100)
    b = randint(1, 100)
    ans = a + b
    # 問題を出題し、キーボードからの入力待ちにする
    question = f"{a} + {b}は？"
    value = input(question)
    # qと入力されたら中断する
    if value == "q":
        break
    # 解答が正解かどうか判断する
    if value == str(ans):
        correct += 1
        print("正解です！")
    else:
        miss += 1  # 間違いをカウントアップします
        print("間違い！", "x" * miss)  # 間違いの数だけ x を表示する

print("-" * 20)
print("正解：", correct)
print("間違い：", miss)
