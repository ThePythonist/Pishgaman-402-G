# def f(name):
#     return "Hello" + " " + name
#
#
# print(f("nima"))
#
# greet = lambda name: "Hello" + " " + name
# print(greet("nima"))
# #
#
# # --------------------------------------------------------------------
#
#
# def power(x, y):
#     return x ** y
#
#
# print(power(4, 3))
#
# power = lambda x, y: x ** y
# print(power(2, 3))
#
#
# # --------------------------------------------------------------------
#
#
# def f(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
#
#
# print(f(4))
#
# f = lambda x: True if x % 2 == 0 else False
# print(f(8))
#
#
# # --------------------------------------------------------------------
#
#
# def rec_power(x, y):
#     if y == 1:
#         return x
#     else:
#         return x * rec_power(x, y - 1)
#
#
# print(rec_power(2, 4))
#
# tavan = lambda x, y: x if y == 1 else x * rec_power(x, y - 1)
# print(tavan(2, 3))
#
#
# # --------------------------------------------------------------------
#
#
# def factorial(n):
#     if n == 1:
#         return n
#     else:
#         return n * factorial(n - 1)
#
#
# x = input("Enter any number : ")
# print(factorial(x))
#
# factorial = lambda n: n if n == 1 else n * factorial(n - 1)
# print(factorial(x))
#
# # --------------------------------------------------------------------
#
# print((lambda x, y: x + y)(5, 4))
#
# # --------------------------------------------------------------------
#
# if (lambda x: True if x % 2 == 0 else False)(11):
#     print("Yes")
# else:
#     print("No")
