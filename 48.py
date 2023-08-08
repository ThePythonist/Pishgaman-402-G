number = int(input("Enter any number : "))
divisors = []

for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)

print(divisors)

# if divisors == [1, number]:
if len(divisors) == 2:
    print("Prime")
else:
    print("Composite")
