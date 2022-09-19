""" Магические методы(данер методы - double underscore method) """

# __init__() - инициализация объекта 
# a = []
# __new__ -  конструктор, отвечает за создание объектов

# class MagicClass:
#     def __new__(cls, *args, **kwargs):
#         print('Сработал метод __new__')
#         return super().__new__(cls)

#     def __init__(self):
#         print('Сработал метод __init__')
#         self.a = 10


# obj = MagicClass()

# # Синглтон - паттерн, подразумевает наличие только одного объекта 

# class Contact:
#     _instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             return cls._instance

#         raise Exception('Объект уже создан.')

#     def __init__(self, phone, name):
#         self.phone = phone
#         self.name = name

# c1 = Contact('996555888999', 'Georgiy')
# c2 = Contact('996999666333', 'Sam')

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        # Человека читабельный отображение 
        return self.name

    def __repr__(self):
        #отображение для компьютера
        return self.name

    def __del__(self):
        #Деструктор 
        print('объект удален.')
        del self

    """ 
    Перезагрузка операторов сравнения 
    __gt__ - >
    __lt__ - <
    __eq__ - ==
    __ne__ - !=
    __ge__ - >=
    __le__ - <=
    """
    def __gt__(self, other):
        return self.age > other.age

    """
    Перегрузка математических операторов
    __add__ - +
    __sub__ - -
    __mul__ - *
    __truediv__ - /
    __floordiv__ - //
    __pow__  - **
    __mod__ - %
    """        

    def __add__(self, other):
        return self.age + other.age

    """
    Операции над атрибутами 
    __setattr__
    __getattr__
    __delattr__
    __getattribute__
    """

    def __getattr__(self, name):
        print('Получаем атрибут')
        return self.__dict__.get(name)

    def __getattribute__(self, __name: str):
        print('Сработал __getattribute__')
        return super().__getattribute__(__name)



# a = Person('Sam', 25)
# b = Person('Artur', 23)
# print(a.last_name)
# print(a.age)
# a.name - __getattr__
# a.reting = 100 - __setattr__
# del a.reting - __delattr__

# print(a > b)
# print(a.__gt__(b))
# print(a + b)
# print(a)
# list_ = []
# list_.append(a)
# print(list_)



class MyDict(dict):
    """
    __len__(self)
    __getitem__(self, key)
    __setitem__(self, key, value) - self[key] = value
    __delitem__(self, key)- del self[key]
    __contains__(self, item) - item in self

    """

    def __getitem__(self, key):
        print('__getitem__')
        return super().__getitem__(key) + 1 

    def __setitem__(self, key, value):
        print('__setitem__')
        super().__setitem__(key, value)


# obj = MyDict(a = 5, b = 6, c = 7)
# print(obj['a'])
# obj['d'] = 10
# print(obj)

class Human:
    def __init__(self, name):
        self.name = name

    def __len__(self):
        counter = 0 
        for i in self.name:
            counter += 1
        return counter

    def __contains__(self, item):
        if item in self.name:
            return True
        return False

h = Human('Sam')
print(len(h))
print('a' in h)












