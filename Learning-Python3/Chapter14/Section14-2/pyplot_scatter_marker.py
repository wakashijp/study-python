import matplotlib.pyplot as plt

X1 = [79, 49, 24, 61, 37, 47, 70, 53, 48, 20,  2, 64, 77, 78, 78,  8,  6, 14, 62, 43]
Y1 = [26, 31, 34, 36, 31, 35, 41, 49, 31, 37, 43, 24, 29, 37, 30, 46, 41, 40, 31, 39]
X2 = [97, 98, 33, 93, 59, 63, 30, 48, 88, 56, 91, 65, 69, 66, 67, 92, 96, 59, 49, 34]
Y2 = [62, 77, 60, 57, 46, 45, 49, 57, 60, 54, 53, 72, 46, 72, 59, 76, 67, 49, 42, 42]
plt.scatter(X1, Y1, marker="+", color="red")  # グラフを描く
plt.scatter(X2, Y2, marker="^", color="green")  # グラフを描く
plt.show()