numbers = []

while True:
    x = input("Enter any number : ")
    if x == "exit":
        break
    else:
        try:
            x = float(x)
            if int(x) == float(x):
                numbers.append(int(x))
            else:
                numbers.append(x)
        except ValueError:
            print("Its not a number")

print(numbers)
print("Maximum :", max(numbers))
