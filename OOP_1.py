# Hometask_14_1 - Hometask_14_2
# Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age. Класс
# имеет три метода: jump, run, bark. Каждый метод выводит сообщение на экран. Создать объект класса Dog,
# вызвать все методыобъекта и вывести на экран все его атрибуты.
# Добавить в класс Dog метод change_name.Метод принимает на вход новое имя и меняет атрибут имени у объекта.
# Создать один объект класса. Вывести имя. Вызвать метод change_name. Вывести имя.

class Dog:

    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        return f'{self.name} jumping'

    def run(self):
        return f'{self.name} running'

    def bark(self):
        return f'{self.name} barks'

    def change_name(self, new_name):
        self.name = new_name


dog_1 = Dog(30, 6.2, "Archie", 3)

print(dog_1.__dict__)
print(dog_1.jump(), dog_1.run(), dog_1.bark(), sep='\n')

print(dog_1.change_name(input()), dog_1.__dict__, sep='\n')
