

# TODO
# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя способами

# version 1.0

begin_sentence = input("Введите предложение!: ")
sentence = begin_sentence.split()
result = "-".join(sentence)
print(result)

# Version 2.0

begin_sentence = input("Введите предложение!: ")
print(begin_sentence.replace(" ", "-"))


