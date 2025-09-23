# スペース区切りで出力

""" "
データを入力してください(スペース区切り) > 1 1 2 3 5 8 13 21
合計値: 54
最大値: 21
最小値: 1
平均値: 6
"""
# データ入力
data = input("データを入力してください(スペース区切り) > ")
data_list = data.split(" ")
data_list = [int(d) for d in data_list]


# 関数定義
# 合計値を計算する関数
def calculation_total(numbers: list[int]) -> int:
    total = 0
    for num in numbers:
        total += num
    return total


# 最大値を計算する関数
def calculation_max(numbers: list[int]) -> int:
    max_number = numbers[0]
    for num in numbers[1:]:
        if num > max_number:
            max_number = num
    return max_number


# 最小値を計算する関数
def calculation_min(numbers: list[int]) -> int:
    min_number = numbers[0]
    for num in numbers[1:]:
        if num < min_number:
            min_number = num
    return min_number


# 平均値を計算する関数
def calculation_avg(numbers: list[int]) -> int:
    total = calculation_total(numbers)
    return total // len(numbers)


# 計算と結果表示

# 各関数を呼び出して結果を変数に代入
total_value = calculation_total(data_list)
max_value = calculation_max(data_list)
min_value = calculation_min(data_list)
average_value = calculation_avg(data_list)

# 結果を表示
print(f"合計値: {total_value}")
print(f"最大値: {max_value}")
print(f"最小値: {min_value}")
print(f"平均値: {average_value}")
