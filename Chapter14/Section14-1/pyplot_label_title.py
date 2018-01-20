import matplotlib.pyplot as plt

price = [200, 300, 400, 500, 600]
count = [31, 29, 25, 28, 26]
plt.plot(price, count)  # グラフを描く
plt.title("Count - Price")  # タイトル
plt.xlabel("Price")  # x軸のラベル
plt.ylabel("Count")  # y軸のラベル
plt.show()
