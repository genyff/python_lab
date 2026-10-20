# Завдання 1. Клас Rectangle — 2 б.
# Створіть клас Rectangle з атрибутами width і height. Реалізуйте методи area(), perimeter() та info(). Метод
# info() повинен виводити розміри прямокутника, площу та периметр.
# Створіть щонайменше два об'єкти Rectangle з різними розмірами та продемонструйте роботу всіх методів.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2*(self.width + self.height)
    def info(self):
        return (f"Висота прямокутника: {self.height}, ширина: {self.width}, площа прямокутника: {self.area()}, периметр: {self.perimeter()}")
prk = Rectangle(5, 8)
print(prk.info())

prk = Rectangle(46, 19)
print(prk.info())


# Завдання 2. Клас Student — 3 б.
# Створіть клас Student. Атрибути: name — ПІБ учня, grades — список оцінок. Реалізуйте add_grade(),
# average() та __str__().
# add_grade() додає оцінку лише в діапазоні 1–12. Некоректна оцінка не повинна потрапити до списку.
# average() повертає середній бал або 0, якщо оцінок немає. __str__() повертає зрозумілий рядок з ПІБ,
# оцінками та середнім балом.

class Student:
    def __init__(self, name, grades=None):
        self.name = name
        self.grades = grades if grades is not None else []

    def add_grade(self, grade):
        if 1 <= grade <= 12:
            self.grades.append(grade)

    def average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"ПІБ учня: {self.name}, оцінки: {self.grades}, середній бал: {self.average():.2f}"

student = Student("Лисенко Вікторія", [10, 11, 12, 9, 12])
print(student)

student.add_grade(9)
student.add_grade(15)
student.add_grade(10)
print(student)


# Завдання 3. Група об'єктів Student — 3 б.
# Використайте клас Student із завдання 2. Створіть список щонайменше з 5 об'єктів Student та додайте
# кожному кілька оцінок.
# Виведіть усіх учнів та їхні середні бали. Знайдіть учня з найвищим середнім балом. Якщо найкращий
# результат однаковий у кількох учнів, виведіть усіх таких учнів.
# Вимога: список повинен містити саме об'єкти Student, а не словники.

students_list = [
    Student("Лисенко Вікторія", [10, 11, 12, 9, 12]),
    Student("Гриценко Катерина", [8, 9, 10, 11, 12]),
    Student("Данилюк Аліна", [8, 7, 6, 5, 4]),
    Student("Руденко Павло", [10, 9, 7, 5, 12]),
    Student("Яремчук Поліна", [10, 11, 12, 9, 12]),
    Student("Павлюк Тимофій", [8, 7, 10, 9, 4])
]

students_list[0].add_grade(9)
students_list[1].add_grade(7)
students_list[2].add_grade(5)
students_list[3].add_grade(8)
students_list[4].add_grade(9)
students_list[5].add_grade(12)

print("Список усіх учнів ")
for student in students_list:
    print(student)

max_avr=0
for student in students_list:
    if student.average() > max_avr:
        max_avr = student.average()

print("Найкращий учень\Найкращі учні")
for student in students_list:
    if student.average() == max_avr:
        print(student)

# Завдання 4. Клас BankAccount або Wallet — 4 б.
# Створіть клас BankAccount або Wallet з атрибутами owner та balance. Реалізуйте методи deposit(amount),
# withdraw(amount) та info().
# deposit() не повинен дозволяти нульове або від'ємне поповнення. withdraw() не повинен дозволяти
# нульову/від'ємну суму та списання понад поточний баланс. Після успішної операції баланс об'єкта
# змінюється.
# Створіть щонайменше два рахунки/гаманці. Для кожного продемонструйте кілька успішних та
# помилкових операцій. Наприкінці виведіть стан обох об'єктів.

class Wallet:
    def __init__(self, owner, balance=None):
        self.owner = owner
        self.balance = balance if balance is not None else 0
    def info(self):
        return (f"Овнєр рахунку: {self.owner}, баланс: {self.balance}")
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Операція поповнення успішна. Поточний стан рахунку: ", self.info())
        else:
            print("Операція поповнення нeуспішна")
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Операція зняття успішна. Поточний стан рахунку: ", self.info())
        else:
            print("Операція зняття неуспішна")

account1 = Wallet("Гриценко Катерина")
account2 = Wallet("Данилюк Аліна")
print(account1.info())
print(account2.info())

account1.deposit(90)
account2.deposit(7)
print(account1.info())
print(account2.info())
account1.deposit(-12)
account2.deposit(0)


account1.withdraw(16)
account2.withdraw(9)
print(account1.info())
print(account2.info())








