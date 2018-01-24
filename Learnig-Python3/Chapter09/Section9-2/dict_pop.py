fruit = {"apple": 7, "orange": 5, "peach": 6}
while fruit:  # fruitが空でなければ繰り返す
    key = input("どのフルーツを取り出しますか？（qで終了）： ")
    if key == "":
        continue
    elif key == "q":
        print("終了しました。")
        break
    try:
        value = fruit.pop(key)  # keyの値を取り出して要素を削除します
        print(f"{key}は{value}個")
    except KeyError:  # 入力されたキーが辞書になかったらメッセージを表示します
        print(f"{key}はありません")
    except Exception as error:
        print(error)
        break
else:  # whileループの終了後に実行 -- fruitが空になるとループは正常に終了します
    print("もう空っぽです。")
