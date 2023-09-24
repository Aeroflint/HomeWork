

# TODO **Вывести четные числа от 2 до N по 5 в строку

N = int(input("Введите число!: "))
for i in range(2, N):
    if i % 2 == 0:
        print(i, end =" ")
