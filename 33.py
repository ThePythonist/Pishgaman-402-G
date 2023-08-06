numbers = [1, 2, 3, 4, 5]

# for i in range(5):
#     x = int(input("Enter any number : "))
#     if 5 < x < 11:
#         numbers.append(x)
#
# # numbers.sort()
# print(numbers)

# -----------------------------------------------

while not len(numbers) == 10:
    x = int(input("Enter any number : "))
    if 5 < x < 11:
        numbers.append(x)

print(numbers)

# -----------------------------------------------

# n = 0
#
# while n != 5:
#     x = int(input("Enter any number : "))
#     if 5 < x < 11:
#         numbers.append(x)
#         n += 1
#
# print(numbers)
