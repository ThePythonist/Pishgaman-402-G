# def power(x):
#     return x ** 2
#
#
# squares = []
#
# for i in [2, 3, 4]:
#     # print(func(i))
#     squares.append(power(i))
#
# print(squares)
#
#
# # -------------------------------------
#
# def func(x):
#     return x ** 2
#
#
# m = map(func, [2, 3, 4])
# print(list(m))
#
# # -------------------------------------
#
m = map(lambda x: x ** 2, [2, 3, 4])
print(list(m))
#
# # -------------------------------------
