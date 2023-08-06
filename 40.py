numbers = []

for i in range(4):
    x = int(input("Enter any number : "))
    numbers.append(x)

numbers.sort()
print(numbers[::-1])
