

# TODO
# Пользователь вводит 3 числа, найти среднее арифмитическое с точность 3

# first_number = float(input("Введите первое число!: "))
# second_number = float(input("Введите второе число!: "))
# third_number = float(input("Введите третье число!: "))
#
# list_number = (first_number + second_number+third_number)
# result = sum(first_number+second_number+third_number) / len(list_number)
# print(round(result, 3))

first_number = float(input("Введите первое число!: "))
second_number = float(input("Введите второе число!: "))
third_number = float(input("Введите третье число!: "))

list_number = [first_number, second_number, third_number]
result = sum(list_number) / len(list_number)
print(round(result, 3))
