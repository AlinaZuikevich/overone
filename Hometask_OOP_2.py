# # №14.8-14.9
# # Создайте класс для салона красоты, чтобы можно было создавать дома с салоном
# # красоты.Методы:- Маникюр- Стрижка. Методы прописывать не надо, просто поставьте заглушку/
# # Добавьте в салон красоты метод salon_opening_hours, который сообщает салон открыт или
# # закрыт.Создайте дом с салоном красоты.Атрибуты:Час открытия салонаЧас закрытия салона
# # Посмотрите работает ли салон в 13 часов, а в 23?
# class Building:
#
#     def __init__(self, doors, windows, floors):
#         self.doors = doors
#         self.windows = windows
#         self.floors = floors
#
#     def build(self):
#         print("The building was built")
#
#     def destroy(self):
#         print("The building was destroyed")
#
# class BeautySalonMixin:
#
#     def manicure(self):
#         pass
#
#     def haircut(self):
#         pass
#
#     def salon_opening_hours(self,open_time, science_time, close_time):
#         if open_time < science_time < close_time:
#             print(f"В {science_time} часов cалон открыт")
#         else:
#             print(f"В {science_time} часов cалон закрыт")
#
# class SalonWithHouse(Building, BeautySalonMixin):
#
#     def __init__(self, open_time,close_time):
#         self.open_time = open_time
#         self.close_time = close_time
#
# s_in_h = SalonWithHouse(9, 22)
# print(f'Время работы салона: {s_in_h.open_time}-{s_in_h.close_time}')
#
# s_in_h.salon_opening_hours(s_in_h.open_time, 13, s_in_h.close_time)
# s_in_h.salon_opening_hours(s_in_h.open_time, 23, s_in_h.close_time)


# # Hometask_14_5 - 14_6
# # 1) Создать три класса: Dog, Cat, Parrot. Атрибуты каждого класса: name, age, master.
# # Каждый класс содержит конструктор и методы: run, jump, birthday(увеличивает age на 1), sleep.
# # Класс Parrot имеет дополнительный метод fly, Cat - meow, Dog - bark.
# # 2) Создать родительский класс Pet, содержащий все общие методы классов Dog, Cat, Parrot. Унаследовать Dog,
# # Cat, Parrot от класса Pet. Удалить в дочерних классах те методы, которые имеются у родительского класса.
# # Создать объект каждого класса и вызвать все его методы.
# class Pet:
#
#     def __init__(self, name, age, master):
#         self.name = name
#         self.age = age
#         self.master = master
#
#     def run(self):
#         print(f"{self.name} running")
#
#     def jump(self):
#         print(f"{self.name} jumping")
#
#     def birthday(self):
#         print(f"{self.name} is {self.age + 1} years old today")
#
#     def sleep(self):
#         print(f"{self.name} sleeping")
#
# class Dog(Pet):
#
#     def __init__(self, name, age, master):
#         super().__init__(name, age, master)
#
#     def bark(self):
#         print(f"Dog {self.name} barks")
#
# class Cat(Pet):
#
#     def __init__(self, name, age, master):
#         super().__init__(name, age, master)
#
#     def meow(self):
#         print(f"Cat {self.name} meows")
#
# class Parrot(Pet):
#
#     def __init__(self, name, age, master):
#         super().__init__(name, age, master)
#
#     def fly(self):
#         print(f"Parrot {self.name} flies")
#
#
# dog = Dog('Max', 5, 'Andrey')
# cat = Cat('Mikki', 4, 'Alex')
# parrot = Parrot('Kesha', 1, 'Alexandra')
#
# print(dog.__dict__, cat.__dict__, parrot.__dict__, sep='\n')
#
# dog.run()
# dog.birthday()
# dog.bark()
#
# cat.jump()
# cat.birthday()
# cat.meow()
#
# parrot.sleep()
# parrot.birthday()
# parrot.fly()



