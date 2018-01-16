# マイルをメートルに換算する関数
def mile2meter(mile):
    meter = mile * 1609.344
    return meter


# 20マイルをメートルに換算する
distance = mile2meter(20)  # 引数に20を渡します
print(distance)
