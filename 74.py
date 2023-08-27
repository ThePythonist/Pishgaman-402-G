def func(x, y):
    if y == 1:  # shart payan
        return x
    else:  # shart edame
        return x + func(x, y - 1)


print(func(3, 6))
