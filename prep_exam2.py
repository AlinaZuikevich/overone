# # exam_1_1
# # Дан список. Выведите те его элементы, которые встречаются в списке только один раз.
# ls1 = input().split()
# for i in ls1:
#     if ls1.count(i) == 1:
#         print(i)


# # exam_2_1
# # Дан список символов. Посчитайте сколько в нем пар элементов, равных друг другу (одинаковых).
# # Считается, что любые два элемента, равные друг другу, образуют одну пару, которую необходимо посчитать.
# ls = input().split()
# s = set(ls)
# print(len(ls) - len(s))


# # exam_3_if sum(tpl1) > sum(tpl2):
# #     print(f'Сумма больше в кортеже {tpl1}')
# # elif sum(tpl1) < sum(tpl2):
# #     print(f'Сумма больше в кортеже {tpl2}')1
# # Дано два кортежа. Определите сумму элементов какого из кортежей больше и выведите соответсвующее
# # сообщение в формате: «Сумма больше в кортеже …»
# tpl1 = tuple(int(i) for i in input().split())
# tpl2 = tuple(int(i) for i in input().split())
#


# # exam_3_2
# # Дан кортеж. Вывести на экран порядковый номер максимального элемента.
# tpl = tuple(int(i) for i in input().split())
# print(f"Индекс максимального элемента {tpl.index(max(tpl))}")


# # exam_4_1
# # Дана строка. Создайте из нее словарь, где ключами будут символы, а
# # значением – количество его появлений в строке.
# str = input()
# dict = {a: str.count(a) for a in str}
# print(dict)


# # exam_5_1
# # Клиент приходит в пиццерию. Реализуйте менб, чтобы клиент мог посмотреть описание и цену:
# # 1. Если клиент захочет посмотреть описание, выведите название пиццы и из чего она состоит
# # 2. Если клиент захочет посмотреть цену, выведить «пицца … стоит … рублей»
# # В качестве меню создайте словарь: ключ – пицца, значение – описание, цена за 100 грамм.

# menu = {'гавайская': [['тесто, ананасы, сыр, курица'], 5],
#         'цыпленок барбекю': [['тесто, курица, томат, соус барбекю, сыр'], 4],
#         'мексиканская': [['тесто, кур. грудка, томат, сыр, кукуруза'], 3]}
#
# piz = input('Какая пицца Вас интересует: ').lower()
# a = input('Что Вы хотели бы уточнить: ').lower()
# if  a == 'описание':
#     print(f'Пицца {piz} состоит из {menu[piz][0]}')
# if  a == 'цена':
#     print(f'Пицца {piz} стоит {menu[piz][1]} рублей')


# # exam_5_2
# # Клиент выбрал пиццу. Реализуйте заказ клиента. Клиент вводит какую пиццу он
# # хочет купить и сколько грамм. Программа выводит стоимость покупки и сколько пиццы
# # осталось в пиццерии в граммах. Не забудьте, что у Вас цена за 100 грамм!!!
# pizza = {'грибная': [['тесто', 'мука', 'грибы'], 7, 1500],
#           '3 сыра': [['сыр', 'сыр', 'сыр'], 4, 1350],
#           'неаполитана': [['сыр', 'тесто', 'специи'], 5, 950]}
#
# buy = input('Какая пицца Вас интересует: ')
# look = int(input('Сколько пиццы Вам положить: '))
#
# print(f"К оплате {pizza[buy][1]*(look/100)}")
# print(f"Пиццa {buy} осталось {pizza[buy][2]- look}")


# # exam_6_1
# # Даны 2 списка чисел, в которых могут быть одинаковые элементы. Посчитайте, сколько
# # уникальных элементов содержится только в первом списке.
# s1 = set(int(i) for i in input().split())
# s2 = set(int(i) for i in input().split())
# print(len(s1 - s2))


# # exam_8_1
# # В текстовый файл построчно записаны фамилия, имя учащихся класса и его оценка
# # за тест. Вывести на экран всех учащихся, чья оценка больше 4х баллов.
# with open("text.txt", "r") as f:
#     for line in f:
#         text = line.split()
#         if int(text[2]) > 4:
#             print(line)

# # var2
# with open("text.txt", "r") as f:
#     for i in f:
#         i = i.rstrip()
#         if int(i[-1]) > 4:
#             print(i)


# # exam_8_2
# # В текстовый файл построчно записаны фамилия, имя учащихся класса и его оценка
# # за тест. Вывести на экран сумма всех оценок.
# sum = 0
# with open("text.txt", "r") as f:
#     for line in f:
#         text = line.split()
#         sum += int(text[2])
# print(sum)

# # var2
# sum = 0
# with open("text.txt", "r") as f:
#     for i in f:
#         i = i.rstrip()
#         sum += int(i[-1])
# print(sum)


# # exam_8_3
# # В текстовый файл построчно записаны фамилия, имя учащихся класса и его оценка
# # за тест. Вывести на экран сколько всего оценок.
# lines = 0
# with open("text.txt", "r") as f:
#     for line in f:
#         lines += 1
# print(f'Всего {lines} оценок')


# # var2
# c = 0
# with open("text.txt", "r") as f:
#     for i in f:
#         i = i.rstrip()
#         c += 1
# print(c)