numlist = [3, 4.2, 10, 1, 9]
sum_value = 0
for num in numlist:
    # numが数値でない時は処理をブレイクする
    if not isinstance(num, (int, float)):
        print(num, "数値ではない値が含まれていました。")
        break  # ブレイクする
    sum_value += num
else:
    # breakされなかった時は合計した値を出力する
    print("合計", sum_value)
