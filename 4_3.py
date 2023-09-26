

# TODO *Заполнить словарь где ключами будут выступать числа от 0 до n,
#  а значениями вложенный словарь с ключами "name" и "email", а значения
#  для этих ключей будут браться с клавиатуры

# d = {a: a ** 2 for a in range(7)}

data = {}
name = input("Введите имя: ")
email = input("введите email: ")
# n = (n for n in range(0, n)):
# n = int(input("Введите число: "))
n = int(input("Введите число!: "))
# a = for i in range(0, n)
data = {n: {
    'name': name,
    'email': email
}}
for n in range(0, n):
    print(data)








# # for i in range(0, n):
# print(dict.items(data))




# data = {}
# n = int(input("Введите число!: "))
# name = input("Введите имя!: ")
# email = input("Введите email!: ")
#
# data = {i for i in range(0, n)}
#
# # n = input("D")
# # a = (int(n) + 5)
# unique_data = dict()
#
# new_data = unique_data.pop(name, email)
#
# # data = {
# #     0: {name: 'Alex', email: 'alex@gmail.com'},
# #     1: {name: 'Petya', email: 'petya@gmail.com'},
# #     2: {name: 'Masha', email: 'masha@gmail.com'}
# # }
# #
# # print(data) * 3
#
# print(new_data(name, email))