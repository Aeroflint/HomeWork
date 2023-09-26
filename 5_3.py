

# TODO **Вывести четные числа от 2 до N по 5 в строку


N = int(input("Введите число!: "))
for i in range(2, N):
     if i % 2 == 0:
         print(i, end = " " )

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

