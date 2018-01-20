import tkinter as tk
import tkinter.filedialog as fd
from random import random


# 書き出すデータを作る
def getdata():
    num = random()
    return str(num)  # ストリングデータを返します


# tkアプリウインドウを表示しない
root = tk.Tk()
root.withdraw()

# 保存ダイアログを表示する
file = fd.asksaveasfilename(
    initialfile="mydata",
    defaultextension=".txt",
    title="保存場所を選んでください。",
    filetypes=[("TEXT", ".txt")]
)

# パスが選ばれたならば保存する
savedata = getdata()  # 保存するデータを取得する
if file:
    with open(file, "w", encoding="utf_8") as fileobj:  # ファイルを開く
        len_ = fileobj.write(savedata)
        print(f"{len_}文字保存しました。")
