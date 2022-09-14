""" Миксины """

# # Mixin - это классы которые используются для дополнения функционала других классов именно путем наследования. От мексинов нельзя создавать объекты.

# class MicrowaveMixin:
#     def heat(self):
#         print('грею еду')

# class Fridge:
#     def cold(self):
#         print('охлаждаю еду')

# class TV:
#     def watch_tv(self):
#         print('смотрю телевизор')

# class Cooker:
#     def cook(self):
#         print('готовлю еду')



# class Kitchen(MicrowaveMixin, TV, Cooker, Fridge):
#     p = 10 

# class BaseClass():
#     def eat(self):
#         pass 

# class BaseMixin:
#     def eat(self):
#         print('я ем детей')

# class ChildrenClass(BaseMixin, BaseClass):
#     pass

# obj = ChildrenClass()
# obj.eat()


# При наследовании миксинов и других классов, миксины нужны указывать в первую очередь (MRO)














