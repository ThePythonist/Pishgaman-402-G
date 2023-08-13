# number = input("Enter any number : ")
# try:
#     number = int(number)
#     print("It is a number")
# except ValueError:
#     print("It is not a number")

# ------------------------------------------------

# try:
#     print(x)
# except NameError:
#     print("X not found")
#
# print("Edame")

# ------------------------------------------------

# try:
#     # x = int("ali")
#     print(x)
#     # print([1,2,3][4])
# except (NameError, ValueError, IndexError):
#     print("Something went wrong")

# ------------------------------------------------

# try:
#     # x = int("ali")
#     # print(x)
#     print([1,2,3][4])
# except (NameError, ValueError, IndexError) as error:
#     print("Something went wrong")
#     print(error)

# ------------------------------------------------

try:
    x = int("ali")
    print("It is a number")
except:
# except Exception as error:
    # print(error)
    print("Something went wrong")

print("edameye barname")
