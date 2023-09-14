

# TODO
# Пользователь вводит 3 числа,
# сказать сколько из них положительных и сколько отрицательных

first_number = int(input("Введите первое число: "))
second_number = int(input("Введите второе число: "))
third_number = int(input("Введите третье число: "))

result = (first_number > 0), (second_number > 0), (third_number > 0)

print((first_number > 0), (second_number > 0), (third_number > 0))
print("Положительных значений - " + (str(result.count(True))))
print("Отрицательных значений - " + (str(result.count(False))))
