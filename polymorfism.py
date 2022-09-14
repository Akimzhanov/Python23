""" Полиморфизм """

#Полиморфизм - принцип ООП, который заключается в использовании одной сущности(метод, оператор) для различных типов объектов 

# + 
# num1 = 10
# num2 = 30
# print(num1 + num2) # сложение 

# str1 = 'hbg'
# str2 = 'hnbgfv'
# print(str1 + str2) # конкатенация строк 

# class A:
#     def method1(self):
#         return 10 + 10

    
# class B:
#     def method1(self):
#         return 'Era' + 'syl'
# objA = A()
# objB = B()
# for obj in (objA, objB):
#     print(obj.method1())

# class Cat:
#     def meow(self):
#         print('мяу')

# class Dog:
#     def bark(self):
#         print('гав')

# cat1 = Cat()
# dog1 = Dog()

# for animal in (cat1, dog1):
#     if type(animal) is Cat:
#         animal.meow()
#     else:
#         animal.bark()



# class Cat:
#     def sound(self):
#         print('мяу')

# class Dog:
#     def sound(self):
#         print('гав')

# cat1 = Cat()
# dog1 = Dog()

# for animal in (cat1, dog1):
#     animal.sound()

""" Абстракция """
# Абстракция - сущность без конкретной реализации 

# class Animal:
#     def __init__(self) -> None:
#         self.eat()
#         self.sound()
#         self.move()

#     def eat(self):
#         raise NotImplementedError(self.__class__.__name__)
    
#     def sound(self):
#         raise NotImplementedError(self.__class__.__name__)

#     def move(self):
#         raise NotImplementedError(self.__class__.__name__)


# class Cow(Animal):
#     pass


# cow = Cow()
# cow.eat()

# from abc import ABC, abstractmethod

# class AbstactClass(ABC):
#     def get_x(self):
#         return 'x'

#     @abstractmethod
#     def abs_method(self):
#         pass


# class ConcreateClass(AbstactClass):
#     def method1(self):
#         print(5252525)

#     def abs_method(self):
#         return 'world'

# obj = ConcreateClass()








