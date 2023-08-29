def myhash(x):
    if len(str(x)) == 1:
        return x
    else:
        # digits = []
        # for i in str(x):
        #     digits.append(int(i))
        digits = [int(i) for i in str(x)]
        x = sum(digits)
        return myhash(x)


print(myhash(98))
