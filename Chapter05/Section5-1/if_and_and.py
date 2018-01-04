# randomモジュールのrandint関数を読み込む
from random import randint

a = randint(0, 100)  # 0〜100の乱数を生成する。
b = randint(0, 100)  # 0〜100の乱数を生成する。

# 判定（3つの条件がTrueの時合格）
if a >= 40 and b >= 40 and (a + b) >= 120:  # 3つの条件をandで連結します。
    result = "合格"
else:
    result = "不合格"

# 結果の出力
text = f"a {a}、b {b}、合計{a + b}：{result}"
print(text)
