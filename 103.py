lines = open("words.txt").read().split("\n")
items = []
digits = [str(i) for i in range(0, 10)]

for i in lines:
    if not i.isdigit():
        for j in digits:
            if j in i:
                items.append(i)
                break

print(items)
