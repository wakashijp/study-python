numbers = [4, 8, 15, 16, 23, 42]
num = int(input("受験番号を入力してください。： "))

if num in numbers:  # 数値が含まれているかどうかを調べる
    print("合格です。")
else:
    print("不合格です。")
