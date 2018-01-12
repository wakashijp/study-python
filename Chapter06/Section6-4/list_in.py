names = ["鈴木裕子", "田中里美", "桜木颯太"]
name = "里美"
result = False

for item in names:
    if name in item:  # namesから取り出した要素を調べる
        result = True
        break  # 見つかった時点でブレイクする

print(result)
