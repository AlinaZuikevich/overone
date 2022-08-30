# # Hometask_13_4
# # Напишите функцию, которая создает список случайных элементов. На фход функция
# # принимает кол-во элементов, минимальное и максимальное значение
# import random
#
# def rand_nums(a, b, c):
#     new_ls = []
#     for i in range(a):
#         new_ls.append(random.randint(b, c))
#     return new_ls
# print(rand_nums(7, 2, 12))
# # или
# # a, b, c = list(map(int, input().split()))
# # print(rand_nums(a, b, c))


# # №13.12
# # Пользователь делает вклад N рублей на X лет под 10 % годовых, т.е. каждый год размер
# # его вклада увеличивается на 10%. Напишите функцию, которая возвращает накопленную сумму.
# def bank(n, x):
#     if x == 1:
#         return n*1.1
#     if x > 1:
#         return bank((n*1.1),(x-1))
#
# n = int(input())
# x = int(input())
# print(bank(n, x))

