def calc(num):
    unit_price = 180  # 単価
    if not num.isdigit():  # 数字かどうかチェックする
        return None  # 数字でないときは中断する
    price = int(num) * unit_price
    return price


# キーボードから引数を入力して試す
while True:
    number = input("個数を入れてください。（qで終了）： ")
    if number == "":
        continue
    elif number == "q":
        break

    # calc()で計算する
    result = calc(number)  # calc()を呼び出す
    print(result)
