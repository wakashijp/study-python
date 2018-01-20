import tkinter as tk
import tkinter.filedialog as fd

# tkアプリウインドウを表示しない
root = tk.Tk()
root.withdraw()

# オープンダイアログを表示する
file = fd.askopenfilename(  # fileにはダイアログで選択したファイルのパスが入ります
    title="ファイルを選んでください。",
    # ダイアログで選択できるファイルの種類を指定します
    filetypes=[("TEXT", ".txt"), ("TEXT", ".py"), ("HTML", ".html")]
)

# ファイルが選択されたならば開く
if file:  # パスが入っていればTrue
    with open(file, "r", encoding="utf_8") as fileobj:  # ファイルを開く
        text = fileobj.read()  # ファイルを読み込む
        print(text)
