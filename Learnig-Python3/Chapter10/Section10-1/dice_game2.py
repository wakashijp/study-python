from random import randint


# サイコロを定義する
def dice():
    num = randint(1, 6)
    return num


# 2個のサイコロを振るゲーム
def dicegame():
    dice1 = dice()  # 1個目のサイコロを振る
    dice2 = dice()  # 2個目のサイコロを振る
    sum_number = dice1 + dice2  # 2個のサイコロの目の合計
    if sum_number % 2 == 0:
        print(f"{dice1}と{dice2}で合計{sum_number}、偶数")
    else:
        print(f"{dice1}と{dice2}で合計{sum_number}、奇数")


# dicegame()を5回行う
for i in range(5):
    dicegame()

print("ゲーム終了")
