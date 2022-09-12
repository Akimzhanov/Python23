""" Инкасуляция
1. Ограничение доступа к определенным данным 
2. Объединение атрибутов и методов, которые работают с данными в один класс
"""
# Икапсуляция в python реализована на уровне соглашения 

"""
Модификаторы доступа: 
1. public - публичные методы и атрибуты доступны в классе, в дочерних классах и ве класса

2. protected - Защищенные атрибуты и методы досупны в классе, в дочерних классах, но не доступны вне класса

3. private - Приватные атрибуты и методы доступны только в том классе, где они определены 

"""

# class Exs:
#     public = 'public'
#     _protected = 'protected'
#     __private = 'private'

#     def pub_method(self):
#         pass

#     def _prot_method(self):
#         pass

#     def __priv_method(self):
#         pass

# enc = Exs()
# print(enc.public)
# print(enc._protected)
# # print(dir(enc))
# print(enc._Exs__private)


# class InhertClass(Exs):
#     pass

# inh = InhertClass()
# # print(inh.public)
# print(inh._protected)
# # print(dir(inh))
# print(inh._Exs__private)


""" setter & getter  - интерфейсые методы """

# class Light:
#     __turned_on = False

#     def __init__(self, brightness):
#         self.__brightness = brightness

#     #setter
#     def set_status(self):
#         self.__turned_on = True

#     #getter 
#     def get_status(self):
#         return self.__turned_on
    
#     @property
#     def brightness(self):
#         return self.__brightness


#     @brightness.setter
#     def brigjtness(self, value):
#         self.__brightness = value 



    # brightness = property(get_brightness, set_brigjtness)

# lamp = Light(50)
# lamp._Light_turned_on = True # не правильный способ
# lamp.set_status()
# print(lamp.get_status())

# print(lamp.get_status())
# print(lamp.brightness)
# lamp.brightness = 70


class Car:
    __MAX_SPEED = 300
    __MIN_SPEED = 0

    def __init__(self, color, model,max_speed, min_speed):

        self.color = color
        self.model = model
        self.max_speed = max_speed
        self.min_speed = min_speed

        if self.validate():
            raise Exception('не верная скорость интернета ')
        

    def validate(self):
        return self.max_speed > self.__MAX_SPEED or self.min_speed < self.__MIN_SPEED


car2  = Car('red', 'Toyota', 350, 0) 












