# n = int("number")
# print(n)


# try:
#     age = int(input("age: "))
#     print("your age is:", age)
# except ValueError:
#     print("Please enter a valid age")
#

# try:
#     a = int(input("a: "))
#     b = int(input("b: "))
#     result = a/b
#     print(result)
# except ValueError:
#     print("a, b - повинні бути числами")
# except ZeroDivisionError:
#     print("Ділити на 0 нізя")
# finally:
#     print("програму завершено")

# try:
#     grade = int(input("enter your grade: "))
#     if grade < 1 or grade >12:
#         raise ValueError("grade must be betweeen 1 and 12")
#     print(f"your grade is {grade}")
#     break
# except ValueError as error_limit:
#     print(f"error: {error_limit}")

# def int_input(message):
#     while True:
#         try:
#             return int(input(message))
#         except ValueError:
#             print("Please enter an integer.")
#
# n = int(input("Enter a number: "))
# print(n)

# def input_grade():
#     while True:
#         try:
#             grade = int(input("Enter your grade 1...12"))
#             if grade < 1 or grade >12:
#                 raise ValueError("grade must be between 1 and 12")
#             return grade
#         except ValueError as error:
#             print(error)
# grade = input_grade()
# print(f"оцінка {grade} прийнята")


# price = {
#     "apple": 10,
# "banana": 20,
# }
# product = input("enter product name")
# except KeyError:
# print("product not exist")
#
# product = input("enter product name")
# price = price.get(product, "товару немає")









