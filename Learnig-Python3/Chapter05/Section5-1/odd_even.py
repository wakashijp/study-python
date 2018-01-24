# randomモジュールのrandint関数を読み込む
from random import randint

num = randint(0, 100)  # 0〜100の乱数を生成する。

# 奇数か偶数か判定する。
if num % 2:  # 2で割り切れる偶数は余り0でFalse、奇数は余り1でTrueです。
    result = "奇数"
else:
    result = "偶数"

# 結果の出力
print(num, result)
