# 数列の値を作るジェネレータ
def num_generator():
    n = 0
    while True:
        num_ = n * n + 2 * n + 3  # 数列式
        yield num_  # ジェネレータが次に返す値
        n += 1


# 何かを行う関数
def do_something(num):
    return num % 2, num % 3


# ジェネレータが返す値を使って処理を行う
gen = num_generator()  # genジェネレータを作ります
for i in range(1, 10):
    number = next(gen)  # ジェネレータから次の値を取り出す
    result = do_something(number)  # ジェネレータから取り出した値で実行する
    print(result)
