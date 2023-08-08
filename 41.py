n = int(input("How many numbers do you want to enter ? "))
numbers = []

for i in range(n):
    numbers.append(int(input("Enter any number : ")))

print(max(numbers))
