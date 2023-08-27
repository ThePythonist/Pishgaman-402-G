def func(x, y):
    if y == 1:  # shart payan
        return x + 1
    else:  # shart edame
        return 1 + func(x, y - 1)


print(func(2, 4))
