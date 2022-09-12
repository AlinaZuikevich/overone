# # Hometask_14_8
# # Добавьте в класс Pet дескриптор, чтобы нельзя было задать отрицательный возраст или 0
# class NonNegative_Zero:
#
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         if value < 0:
#             raise ValueError('Cannot be negative.')
#         elif value == 0:
#             raise ValueError('Cannot be null.')
#         instance.__dict__[self.name] = value
#
# class Pet:
#     age = NonNegative_Zero()
#
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#     def run(self):
#         print(f"{self.name} running")
#
#     def birthday(self):
#         self.age += 1
#
# class Cat(Pet):
#
#     def meow(self):
#         print(f"Cat {self.name} meows")
#
# cat = Cat('Mikki', 4, 'Alex')
#
# cat.age = int(input())
# cat.birthday()
# print(cat.age)


# # Hometask_14_9
# # Добавьте в класс Pet валидацию, чтобы у питомца было имя и хозяин
# from abc import ABC, abstractmethod
#
# class Validator(ABC):
#
#     def __set_name__(self, owner, name):
#         self.name = name
#
#     def __get__(self, instance, owner):
#         return instance.__dict__[self.name]
#
#     def __set__(self, instance, value):
#         self.validate(value)
#         instance.__dict__[self.name] = value
#
#     @abstractmethod
#     def validate(self, value):
#         pass
#
# class NonEmptyString(Exception):
#
#     def __init__(self, message):
#         self.message = message
#
# class String(Validator):
#
#     def validate(self, value):
#         if not isinstance(value, str):
#             raise TypeError(f'Expected to be an str')
#         elif len(value) == 0:
#             raise NonEmptyString('Empty string is not allowed')
#
# class Pet:
#     name = String()
#     master = String()
#
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#     def run(self):
#         print(f"{self.name} running")
#
# class Cat(Pet):
#
#     def meow(self):
#         print(f"Cat {self.name} meows")
#
# cat = Cat('Mikki', 4, 'Alex')
#
# cat.run()
# print(cat.master)
# cat.master = ''


# # exam_3
# # Напишите функцию, которая будет принимать фамилию и показывать только первую букву.
# # Буква должна быть заглавной. Остальные буквы должны заменяться звездочками.
# def family_hide(family):
#     result = family[0].upper()
#     while family:
#         for i in family[1:]:
#             result += i.replace(i, '*')
#         return result
#
# print(family_hide(input()))