sum_value = 7600
while True:
    num = input("何人ですか?（qで終了）")
    if num == "q":
        print("終了しました。")
        break

    # 例外を処理する
    try:
        price = round(sum_value / int(num))
    except Exception as error:  # 例外オブジェクトをerrorで参照できるようにします
        print("エラーになりました。")
        print(error)  # エラー情報を出力する
    else:  # 例外が発生しなかった時はelseブロックが実行されます
        if price < 0:
            # マイナスの場合は無視する
            continue
        print("1人当たりの金額", price)
