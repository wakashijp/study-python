num = 0  # numが0の場合の結果を確かめます
try:
    value = 120 / num  # numが0の時に例外を発生します
    print(value)
except ZeroDivisionError:
    print("エラーになりました。")
finally:
    print("計算終わり。")  # 例外が発生してもしなくても、最後に実行されます。
