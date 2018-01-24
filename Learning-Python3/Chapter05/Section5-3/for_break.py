numlist = [3, 4.2, 10, "x", 1, 9]  # 文字列が含まれている
sum_value = 0
for num in numlist:
    # numが数値ではない時ブレイクする
    if not isinstance(num, (int, float)):  # intかfloatではない時
        print(num, "数値ではありません。")
        break  # ブレイクする
    sum_value += num
    print(num, "/", sum_value)
