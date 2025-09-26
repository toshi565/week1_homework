# 綺麗な九九 うっかり0を入力して固まったのでエラーを返すこととした

row = int(input("行数を入力してください: "))
column = int(input("列数を入力してください: "))

if row == 0 or column == 0:
    print("エラー: 0は入力できません。")
else:
    for i in range(1, row + 1):
        for j in range(1, column + 1):
            print(f"{j} x {i} = {i * j:2d}", end=" | ")
        print()
