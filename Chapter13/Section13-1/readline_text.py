file = "./data/tsuretsuregusa.txt"

with open(file, "r", encoding="utf_8") as fileobj:  # ファイルオブジェクトを作る
    while True:
        line = fileobj.readline()  # 1行ずつ読み込む
        aline = line.rstrip()  # 改行を取り除く
        if aline:  # 文字列があれば出力する
            print(aline)
        else:
            break  # 読み込みを終了する
