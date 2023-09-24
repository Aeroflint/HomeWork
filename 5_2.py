

# TODO Сделать калькулятор: у пользователя спрашивается число, потом действие и второе число

number_1 =  int(input("Введите первое число!: "))
symbol = input("Введите = - * / : ")
number_2 = int(input("Введите второе число!: "))

if symbol == "+":
    answer = number_1 + number_2
elif symbol == "-":
    answer = number_1 - number_2
elif symbol == "*":
    answer = number_1 * number_2
elif symbol == "/":
    answer = number_1 / number_2
    if number_2 == 0:
        print("На 0 делить нельзя")
    else:
        answer = number_1 / number_2
else:
    print("Enter valid numbers")
print(int(answer))