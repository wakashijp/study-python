def calc(size, num=6):  # numには初期値がある
    unit_price = {"S": 120, "M": 150, "L": 180}
    price = unit_price[size] * num
    return size, num, price


# calc()を試す
a = calc("S", 2)  # sizeは"S"、numは2で計算します
print(f"{a[0]}サイズ、{a[1]}個、{a[2]}円")

b = calc("M")
print(f"{b[0]}サイズ、{b[1]}個、{b[2]}円")
