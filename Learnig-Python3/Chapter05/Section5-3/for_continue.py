numlist = [3, 4.2, 10, "x", 1, 9]  # 文字列が含まれている
sum_value = 0

for num in numlist:
    # numが数値ではない時には処理をスキップする
    if not isinstance(num, (int, float)):
        print(num, "数値ではありません。")
        continue
    sum_value += num
    print(num, "/", sum_value)
