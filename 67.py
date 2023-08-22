def checknumber(items):
    numbers = []
    for x in items:
        if type(x) in [int, float]:
            numbers.append(x)

    print(numbers)


items = [True, "Nike", 12, "Adidas", 5.4, "Gucci", 11, 15, 3.5]
checknumber(items)
