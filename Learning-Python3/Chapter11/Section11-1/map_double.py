def double(x):
    return x * 2


nums = [4, 3, 7, 6, 2, 1]
nums2 = list(map(double, nums))  # numsから順に値を取り出して、double()で実行した結果をリストにします

print(nums2)
