file = "./data/fox.txt"

with open(file) as fileobj:  # ファイルオブジェクトを作る
    text = fileobj.read()  # ファイルを読み込む
    newtext = text.rstrip(".")  # 末尾のピリオドを削除しておく
    wordlist = newtext.split(" ")  # スペースで区切ってリストにする
    print(wordlist)
