numbers = []

for i in range(3):
    x = input("Type something :")
    try:
        x = float(x)
        # if str(x)[-2:] == ".0":
        if int(x) == float(x):
            numbers.append(int(x))
        else:
            numbers.append(x)
    except ValueError:
        print("Its not a number")

print(numbers)
