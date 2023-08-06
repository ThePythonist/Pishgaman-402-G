items = ["Java",True, 15, 3.2, "Python", 12, False, (), 9.2]
numbers = []

for i in items:
    if type(i) == str:
        numbers.append(i)

print(numbers)
