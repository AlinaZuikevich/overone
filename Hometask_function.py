# #№Hometask_13_1
# # Из полученного списка чисел создайте список с суммами
# # этих чисел, отсортированными по возрастанию
# list_sort = []
# def nums_sum_list(number):
#     for i in number:
#         list_sort.append(sum([int(j) for j in str(i)]))
#         list_sort.sort()
#     return list_sort
#
# print(nums_sum_list(input().split()))


# #№Hometask_13_2
# # Напишите функцию f(x), которая возвращает значение следующей
# # функции, определённой на всей числовой прямой:
# def f(x):
#     if x <= -2:
#         result = 1 - (x + 2)**2
#         return result
#     if x > -2 and x <= 2:
#         result = -(x/2)
#         return result
#     if x > 2:
#         result = (x - 2)**2 + 1
#         return result
#
# print(f(float(input())))


# #№Hometask_13_3
# # Напишите функцию которая принимает на вход список целых чисел, удаляет из него
# # все нечётные значения, а чётные нацело делит на два.
# def list_edit(data):
#     for i in data:
#         if i % 2 != 0:
#             data.remove(i)
#     data = [i // 2 for i in data]
#     return data
#
# ls = [int(i) for i in input().split()]
# print(list_edit(ls))
