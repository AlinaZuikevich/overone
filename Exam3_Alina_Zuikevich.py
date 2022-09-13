# # exam_3_1
# # Напишите функцию, которая будет принимать номер кредитной карты и показывать
# # только последние 4 цифры.Остальные цифры должны заменяться звездочками
# def card_hide(card):
#     result = '*' * len(str(card)[:-4]) + str(card)[-4:]
#     return result
#
# print(card_hide(int(input())))


# # exam_3_2
# # Напишите функцию, которая проверяет: является ли слово палиндромом
# def palindrom(str):
#     if len(str)<=1:
#         return 'Cлово является палиндромом'
#     if str[0] != str[-1]:
#         return 'Cлово не является палиндромом'
#     return palindrom(str[1:-1])
#
# print(palindrom(input()))


# # exam_3_3
# # Напишите классы Круг, Прямоугольник, Квадрат. Каждый класс должен содержать метод нахождения
# # площади фигуры.Используйте:- Наследование - Абстрактный класс и методы
# # - Округлите площадь круга до 2х чисел после запятой - Число π возьмите из модуля math
# from abc import ABC, abstractmethod
# import math
#
# class Figures(ABC):
#
#     @abstractmethod
#     def area(self):
#         pass
#
#
# class Square(Figures):
#
#     def __init__(self, side_sq):
#         self.side_sq = side_sq
#
#     def area(self):
#         return f'Площадь квадрата = {self.side_sq ** 2}'
#
#
# class Rectangle(Figures):
#
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length
#
#     def area(self):
#         return f'Площаль прямоугольника = {self.width * self.length}'
#
#
# class Circle(Figures):
#
#     def __init__(self, radius):
#         self.radius = radius
#
#     def area(self):
#         return f'Площадь круга равна = {round(math.pi * (self.radius ** 2), 2)}'
#
#
# square = Square(4)
# rectangle = Rectangle(2, 6)
# circle = Circle(3)
#
# figures = [square, rectangle, circle]
#
# for i in figures:
#     print(i.area())


def card_hide(card):
    return '*' * len(str(card)[:-4]) + str(card)[-4:]

print(card_hide(int(input())))