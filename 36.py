numbers = [10, 3, 5, 4, 1, 15, 14]
evens = []

for i in numbers:
    if i % 2 == 0:
        # evens.append(i)
        evens += [i]

print(evens)
