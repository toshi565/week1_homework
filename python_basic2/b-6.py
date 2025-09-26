import random

dice_sides = int(input("サイコロの面の数は?: "))

if dice_sides < 3:
    print("エラー: サイコロの面数は3以上でお願い")
    exit()

number_of_times = int(input("何回振りますか?: "))

results_list = [random.randint(1, dice_sides) for _ in range(number_of_times)]
print(results_list)
