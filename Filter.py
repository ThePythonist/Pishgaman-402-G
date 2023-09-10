# def func(x):
#     if x >= 18:
#         return True
#     else:
#         return False
#
#
# adults = filter(func, [21, 16, 14, 15, 19])
# print(list(adults))
# print(*adults)

# --------------------------------------------------

# nums = [1, 2, 3, 4, 5, 6]
# f = list(filter(lambda x: x % 2 == 0, nums))
# print(f)

# --------------------------------------------------

ages = [21, 16, 14, 15, 19]
adults = list(filter(lambda x: x >= 18, ages))
print(adults)
