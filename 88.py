m = map(lambda x: [i for i in range(1, x + 1) if x % i == 0], [6, 12, 20])

for i in m:
    print(i)
