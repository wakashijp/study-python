# randomモジュールの randint関数を読み込む
from random import randint
point = randint(0, 100)  # 0〜100の乱数を生成する。

# 判定
if point >= 80:
    result = "Aクラス"  # pointが80以上の時に実行されます。
elif point >= 60:
    result = "Bクラス"  # pointが60以上80未満の時に実行されます。
elif point >= 30:
    result = "Cクラス"  # pointが30以上60未満の時に実行されます。
else:
    result = "不適合"  # pointが30未満の時に実行されます。

# 結果の出力
print(f"{point}点：{result}")  # 全てのケースでif文を抜けた後で実行されます。
