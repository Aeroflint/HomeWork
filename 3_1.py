
# TODO Заполнить список степенями числа 2 (от 2^1 до 2^n).


n = int(input("Введите степень числа 2: "))
new_numbers = [2 ** n for n in range(1, n)]
print(new_numbers)
