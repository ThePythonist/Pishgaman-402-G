def factorial(x):
    if x == 1:
        # return 1
        return x
    else:
        return x * factorial(x - 1)


print(factorial(4))
