import sys
from datetime import datetime

file = "./log.txt"

if len(sys.argv) < 2:  # 1個目の引数はファイル名なので2個以上のときに処理します
    sys.exit()

now = str(datetime.now())  # 現在の日時データ
memo = sys.argv[1]  # コマンドラインから引数を受け取ったメモ
line = '-' * 10  # 区切り線

with open(file, "a") as fileobj:  # 追記モードのファイルオブジェクト
    fileobj.write(now + "\n")
    fileobj.write(memo + "\n")
    fileobj.write(line + "\n")
