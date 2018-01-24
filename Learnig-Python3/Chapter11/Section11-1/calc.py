def calc(func, arg=1):
    price_ = func(arg)  # 引数で受け取った関数funcとargでfunc(arg)を実行します
    return price_


def child(arg):
    return 400 * arg


def adult(arg):
    return 1200 * arg


# 年齢によって計算する関数を変える
age = 12
num = 3

if age < 16:
    price = calc(child, num)  # 16歳未満ならばchild()で計算する
else:
    price = calc(adult, num)  # 16歳以上であればadult()で計算する

print(f"{age}歳、{num}人は{price}円です。")
