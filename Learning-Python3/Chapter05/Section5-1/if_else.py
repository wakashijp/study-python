sum1 = 50 + 37 + 10
limit = 100
if sum1 >= limit:
    result = "合格"
else:
    result = "不合格"
    result += "／" + str(sum1 - limit)

print(sum1)
print("-" * 20)
print(result)
