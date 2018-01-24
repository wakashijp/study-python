numbers = [2, 6, -3, 5, -1, 7]
sum_number = 0

# numbersの正の値だけを合算する
for num in numbers:  # numbersから順に数値をnumに取り出す
    if num > 0:
        sum_number += num  # numbersから順に取り出した値が正のときにsumに加算します。

print(sum_number)
