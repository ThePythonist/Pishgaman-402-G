def numberstatus(x):
    # if x % 2 == 0:
    #     return "Even"
    # else:
    #     return "Odd"
    return "Even" if x % 2 == 0 else "Odd"


def numbertype(x):
    if x.isdigit():
        x = int(x)
        print(numberstatus(x))
    else:
        print("Entry is not a number")


num = input("Enter any number : ")
numbertype(num)
