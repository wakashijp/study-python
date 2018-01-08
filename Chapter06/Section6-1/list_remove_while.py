colors = ["blue", "red", "yellow", "red", "green"]
print("削除前", colors)
target = "red"

# 削除する値が含まれている間は繰り返し削除する
while target in colors:  # targetが含まれている間は繰り返し削除します
    colors.remove(target)

print("削除後", colors)
