

# TODO Без использования collections, написать программу, которая будет создавать словарь
#  для подсчитывания количества вхождений каждой буквы в текст введенный с клавиатуры


words = input("Введите фразу!: ")

#
# def count(letter):
#     pass


for letter in words:
    print(len(letter))
# data_2 = copy(data)
data_2 = len(list(data))
print(data_2)
# data = list(words)
# print(count(data))

#  ПРОВЕРКА ВХОЖДЕНИЯ
# Для того, что проверить, есть ли элемент в списке, нужно воспользоваться оператором in:
# элемент in список
# Для обратной проверки, нет ли элемента в списке, нужно воспользоваться оператором not in:
# эдемент not in список

# Для того, чтобы узнать, сколько элементов в списке с некоторым значение, нужно воспользоваться функцией:
# list.count(значение)
# word = list(words)
#
# # for i in range(1, len(word)+1):
# #     dict[i] = word[i-1]
# dic = {i: x for i, x in enumerate(words, 1)}
# dic = dict.items(dic)
#
#
# print(dic)
