# # exam_1_1
# # С клавиатуры вводится семизначное число.
# # Посчитать сколько в нем четных цифр и сколько нечетных.
# n = int(input())
# even = 0
# odd = 0
#
# while n != 0:
#     last = n % 10
#     if last % 2 == 0:
#         even += 1
#     else:
#         odd += 1
#     n = n // 10
#
# print(even, odd)


# # exam_1_2
# # С клавиатуры вводится семизначное число. Найти сумму его цифр.
# n = int(input())
# summ = 0
#
# while n != 0:
#     last = n % 10
#     summ += last
#     n = n // 10
#
# print(summ)


# exam_1_3
#С клавиатуры вводится семизначное число. Найти произведение его 1,2 и 5 цифр
# # var №1
# n = input()
# print(int(n[0])*int(n[1])*int(n[4]))

# # var №2
# n = int(input())
# mult = 1
# iter = 1
#
# while n != 0:
#     last = n % 10
#     if iter == 3 or iter == 6 or iter == 7:
#         mult *= last
#     n = n // 10
#     iter += 1
#
# print(mult)


# # exam_2_1
# # С клавиатуры вводится строка. Посчитаться в ней количество гласных букв.
# word = input().lower()
# letters = 'eyuioa'
# vow = 0
#
# for i in word:
#     if i in letters:
#         vow += 1
#
# print(vow)


# # exam_2_2
# # С клавиатуры вводится строка. Вывести на экран все гласные
# # буквы (построчно или в одну строку значения не имеет)
# word = input().lower()
# letters = 'eyuioa'
#
# for i in word:
#     if i in letters:
#         print(i, end = ' ')


# # exam_3_1
# # Генерируются 2 рандомных числа (a, b) от 1 до 20. Сравнить
# # их 9 раз и посчитать сколько раз a > b и наоборот, b > a
# import random
# a_more_b = 0
# b_more_a = 0
#
# for i in range(9):
#     a = random.randint(1, 20)
#     b = random.randint(1, 20)
#     print(a, b)
#     if a > b:
#         a_more_b += 1
#     elif b > a:
#         b_more_a += 1
#
# print('----------------')
# print(a_more_b, b_more_a)


# # exam_3_2
# # Сравнить вводимое пользователем число от 1 до
# # 20 N раз с рандомным числом от 1 до 20.
# # Каждый раз, когда рандомное число больше, выводить на
# # экран номер данной итерации.
# import random
# n = int(input('Введите число для сравнения:'))
# times = int(input('Сколько раз будем сравнивать:'))
# iter = 1
#
# while iter <= times:
#     r = random.randint(1, 20)
#     print(r)
#     if r > n:
#         print("iteration number", iter)
#     iter += 1

# # exam_4_1
# # Посчитать сколько раз встречается определенная цифра в числаx.
# # Количество введенных чисел, искомая цифра и числа, в которых может встречаться
# # искомая цифра, задаются с клавиатуры.
# goal = int(input("Какую цифру будем искать:"))
# times = int(input("Сколько раз будем искать эту цифру:"))
# c = 0
#
# for i in range(times):
#     number = int(input("Введите число:"))
#     while number:
#         last = number % 10
#         if last == goal:
#             c += 1
#         number = number // 10
#
# print(c)


# # exam_5_1
# # С клавиатуры вводится строка, содержащая буквы, числа, символы, пробелы.
# # Если в строке есть математические знаки, то вывести их на экран.
# word = input()
# signs = '+-*/'
#
# for i in word:
#     if i in signs:
#         print(i)


# # exam_6_1
# # С клавиатуры вводится строка, содержащая буквы, числа, символы, пробелы.
# # Посчитать сколько пар букв нижнего регистра стоит рядом во введенной строке.
# word = input()
# pair_down = 0
#
# for i in range(1, len(word)):
#     if word[i-1].islower() and word[i].islower():
#         pair_down += 1
#
# print(pair_down)


# # exam_6_2
# # С клавиатуры вводится строка, содержащая буквы, числа,
# # символы, пробелы. Посчитать сколько в строке  согласных букв.
# s = input().lower()
# vow = 'yuioea'
# c = 0
#
# for i in s:
#     if i not in vow:
#         c += 1
#
# print(c)
