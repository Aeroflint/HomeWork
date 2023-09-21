

# TODO *Заполнить словарь где ключами будут выступать числа от 0 до n,
#  а значениями вложенный словарь с ключами "name" и "email", а значения
#  для этих ключей будут браться с клавиатуры

diction = {}
name_result = input("Введите имя!: ")
email_result = input("Введите email!: ")

diction = {0: {
    "name": name_result,
    "email": email_result
}}
print(diction)
