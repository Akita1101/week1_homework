column_number = int(input("行数を入力してください:"))
row_number = int(input("列数を入力してください:"))

for x in range(1, column_number + 1):
    for y in range(1, row_number + 1):
        print(x * y, end=" ")
    print("")