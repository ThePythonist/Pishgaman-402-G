numbers = []

for i in range(3):
    x = input("Type something :")
    try:
        x = float(x)
        numbers.append(x)
    except ValueError:
        print("Its not a number")

print(numbers)
