items = [True, 15, 3.2, "Python", 12, False, (), 9.2]
numbers = []

for i in items:
    if type(i) == int or type(i) == float:
        numbers.append(i)

print(numbers)
