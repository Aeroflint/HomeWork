

# TODO Вывести первые N чисел кратные M и больше K

# data = {N}
N = int(input("Введите число 1: "))
M = int(input("Введите число 2: "))
K = int(input("Введите число 3: "))

for new in range(K,N,M):
    if N % M == 0 and N > K:
        print(new)
    else:
        print("Что-то не то!")





