

# TODO
# Пользователь вводит Имя, Возраст и Город,
# сформировать приветственное сообщение путем форматирования 3-мя способами


# Version 1.0

name = str(input("Введите имя!: "))
age = int(input("Введите ваш возраст!: "))
city = str(input("Введите ваш текущий город!: "))

print(f"Меня зовут {name}. Мне {age}. Я живу в городе {city}")

# Version 2.0

name = str(input("Введите имя!: "))
age = int(input("Введите ваш возраст!: "))
city = str(input("Введите ваш текущий город!: "))

print("Меня зовут {}. Мне {}. Теперь я в городе {}".format(name, age, city))

# Version 3.0

name = str(input("Введите имя!: "))
age = int(input("Введите ваш возраст!: "))
city = str(input("Введите ваш текущий город!: "))

print("Меня зовут %s. Мне %d. Я живу в прекрасном городе %s" % (name, age, city))