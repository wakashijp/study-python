import numpy as np
sigma = 3.5  # 分散
mu = 65  # 平均
# 点数のサンプルデータ（正規分布の乱数で作成する）
data = sigma * np.random.randn(200) + mu  # 点数200個入った配列
x = float(input("得点は？："))  # キーボードから入力する
t_score = 10 * (x - data.mean()) / data.std() + 50  # 偏差値
print("平均点：", round(data.mean(), 1))
print("標準偏差：", round(data.std(), 1))
print("偏差値：", round(t_score, 1))
