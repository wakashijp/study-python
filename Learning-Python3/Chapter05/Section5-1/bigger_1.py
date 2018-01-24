# randomモジュールからrandint関数を読み込む
from random import randint

a = randint(0, 100)  # 0〜100の乱数を生成する。
b = randint(0, 100)  # 0〜100の乱数を生成する。

# 大きな方の値を代入する。
if a > b:
    bigger = a
else:
    bigger = b

# 結果の出力
text = f"{a}と{b}では、{bigger}が大きい"
print(text)
