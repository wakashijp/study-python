import sys

if len(sys.argv) < 2:  # 1個目の引数はファイル名なので2個以上のときに処理します
    print("読み込むファイル名を指定してください。")
    sys.exit()  # プログラムを中断する

file = sys.argv[1]  # ファイルのパスはargv[1]に入っています
with open(file) as fileobj:  # ファイルオブジェクトを作る
    text = fileobj.read()  # ファイルを読み込む
    print(text)
