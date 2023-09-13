# TODO
#  Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами

# version 1.0
a = input("Введите предложение!: ")
sentence = a.split()
result = "-".join(sentence)
print(result)

# Version 2.0
a = input("Введите предложение!: ")
print(a.replace(" ", "-"))


