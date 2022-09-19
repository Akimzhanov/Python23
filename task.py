# #5
# class Phone:
#     def __init__(self, name, last_name, phone):
#         self.name = name
#         self.last_name = last_name
#         self.phone = phone

#     def get_info(self):
#         print(f'Контакт: {self.name} {self.last_name}, телефон: {self.phone}')  


# contact = Phone('Erasyl', 'Akimzhanov', +996997121714)
# contact.get_info()

# #6
# class Salary:
#     percent = 8

#     def __init__(self, salary, experience):
#         self.salary = salary
#         self.experience = experience

#     def count_percent(self):
#         a = (self.salary * self.percent / 100) * self.experience
#         return a

# obj = Salary(15000, 10)
# print(obj.count_percent())


# #7
# from datetime import date

# class Nobel:
#     def __init__(self, category, year, winner):
#         self.category = category
#         self.year = year
#         self.winner = winner
    
#     def get_year(self):
#         current_year = date.today().year
#         return f'выиграл {current_year - self.year} лет назад' 

# winner1 = Nobel('Литература', 1971, 'Пабло Неруда') 
# print(winner1.category, winner1.year, winner1.winner) 
# print(winner1.get_year())
  
# winner2 = Nobel('Литература', 1994, 'Кэндзабуро Оэ') 
# print(winner2.category, winner2.year, winner2.winner) 
# print(winner2.get_year())

"""
Создайте класс Password, экземеплярами класса являются пароли в виде строк. У класса должен быть метод validate для валидации пароля:

В начале, проверьте, что пароль состоит из минимум 8 символов, но меньше 15, если условие не соблюдено, должны выйти ошибка с текстом:
                        Password should be longer than 8, and less than 15
Вторая проверка должна проверять что пароль содержит цифры, и в случае отсутствия цифр, выводить ошибку с текстом:
                        Password should contain numbers too
Третья проверка, проверяет содержит ли пароль буквы и в случае не совпадения, выводит ошибку с текстом:
                        Password should contain letters as well
В конце проверьте, содержит ли пароль хотя бы один из символов: '@', '#', '&', '$', '%', '!', '~', '*', если условие не выполнено выводите ошибку с текстом:
                        Your password should have some symbols
если одно из условий не выполнено, выводите соответствующее исключение, если же все условия выполнены метод validate должен возвращать строку:

                        Ваш пароль сохранен.
Также переопределите метод __str__, чтобы при попытке распечатать сам пароль, вам выдавалась строка из звездочек количество которых равно длине пароля.

К примеру, если пароль joe@123456, при попытке распечатать пароль, в терминал должно выводиться: **********"""


#8
# class Password:
#     def __init__(self, password) -> None:
#         self.password = password


#     def validate(self):
#         if len(self.password) < 8 or len(self.password) > 15:
#             raise Exception ('Password should be longer than 8, and less than 15')
        
#         check_num = list(filter(lambda x: x.isdigit(), self.password))
#         if len(check_num) == 0:
#             raise Exception ('Password should contain numbers too')

#         check_letter = list(filter(lambda x: x.isalpha(), self.password))
#         if len(check_letter) == 0:
#             raise Exception ('Password should contain letters as well')
        

#         ls = ['@', '#', '&', '$', '%', '!', '~', '*']
#         check_sym = list(filter(lambda x:  x in ls, self.password))
#         if len(check_sym) == 0:
#             raise Exception ('Your password should have some symbols')
#         return 'Ваш пароль сохранен.'
#     def __str__(self) -> str:
#         password_2 = len(self.password)
#         return password_2 * '*'
        

        


# password = Password('erasyl@12345')
# print(password.validate())


#9
# Создайте класс Math, у экземпляра которого должно быть свойство value. У классa Math должно быть 3 метода:

# get_factorial - возвращает факториал числа(перемножить все составные числа до самого числа)

# get_sum - возвращает сумму цифр числа

# get_mul_table - возвращает таблицу умножения для числа до 10 в формате:

# Создайте экземпляр класса и примените к нему все методы.

# Например, если экземпляром класса Math является число 11,

# вызов get_factorial возвратит такой результат:

# 39916800 
# т.к 1 x 2 x 3 x 4 x 5 x 6 x 7 x 8 x 9 x 10 x 11 = 39916800

# метод get_sum, возвратит:

# 2 
# т.к число 11 состоит из двух цифр 1 и 1, сумма 1 + 1 = 2

# метод get_mul_table возвратит:

# 11 x 1 = 11 
# 11 x 2 = 22 
# 11 x 3 = 33 
# 11 x 4 = 44 
# 11 x 5 = 55 
# 11 x 6 = 66 
# 11 x 7 = 77 
# 11 x 8 = 88 
# 11 x 9 = 99 
# 11 x 10 = 110 


class Math:
    def __init__(self, num) -> None:
        self.num = num

    def get_factjrial(self):
        chislo = 1
        for x in range(1, self.num + 1):
            chislo *= x

        return chislo

    # def get_sum(self):



    def get_mul_table(self):
        for x in range(1, self.num):
            print(f'{self.num} x {x} = {self.num * x}')
        



a = Math(11)
print(a.get_mul_table())


















