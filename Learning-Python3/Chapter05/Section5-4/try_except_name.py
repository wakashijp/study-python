sum_value = 7600
while True:
    num = input("何人ですか?（qで終了）")
    if num == "q":
        print("終了しました。")
        break

    # 例外を振り分けて例外処理を行う
    try:
        price = round(sum_value / int(num))  # この式が例外を発生する可能性があります
        if price < 0:  # マイナスの場合は無視
            continue
        print("1人あたりの金額", price)

    except ValueError:  # 数値に変換できなかったとき
        print("数値を入れてください。")

    except ZeroDivisionError:  # ゼロの割り算を行ったとき
        print("0以外の数値を入力してください。")
