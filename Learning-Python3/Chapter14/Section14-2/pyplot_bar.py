import matplotlib.pyplot as plt

labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
x_pos = range(0, 10)
V = [91, 45, 17, 88, 47, 87, 49, 56, 67, 77]
plt.bar(x_pos, V, tick_label=labels)  # 縦棒グラフを描く
plt.show()
