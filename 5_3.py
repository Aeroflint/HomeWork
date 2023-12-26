

# TODO **Вывести четные числа от 2 до N по 5 в строку


N = int(input("Введите число!: "))
# c = 0
# for i in range(2, N+1, 2):
#     print(i, end=" ")
#     c += 1
#     if c == 5:
#         c = 0
        print()

numbers = list(range(2, n + 1, 10))
for i in range(0, len(numbers),5):
    for j in range(i, i+9, 2):
        if j <= n:
        print(j, end=" ")
    else:
        break
    print()




# n = int(input())
# a = []
# for i in range(2, n):
#     row = input().split()
#     for i in range(len(row)):
#         row[i] = int(row[i])
#     a.append(row)
# print(a, end = " ")


        # for row in matrix:
        #     print(row)
                # print(N[i][j], end = ' ')
# print()
# for i in range(2, N):
#     for j in range(2, N):
#         print((int(i[i - 1][j])) + (int(i[i - m + 1][j])) + (int(i[i][j - 1])) + (int(i[i][j - n + 1])),
#                 end=" " if j < m - 1 else '\n')

