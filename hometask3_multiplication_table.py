# Вывод таблицы умножения в восемь столбцов вида "a * b = c"

for i in range(2, 10):
    for j in range(2, 10):
        print((f"{j} * {i} = {j * i}").ljust(10),end=' '*4)
    print()