def calc(num):
    unit_price = 180  # 単価
    try:
        num = float(num)  # 数値に変換する
        return num * unit_price
    except ValueError:
        return None  # 変換がエラーになったらNoneを返す


# キーボードから引数を入力して試す
while True:
    number = input("個数を入れてください。（qで終了）： ")
    if number == "":
        continue
    elif number == "q":
        break

    # calc()で計算する
    result = calc(number)
    print(result)
