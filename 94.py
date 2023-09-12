def f1():
    lines = open("words.txt").readlines()
    lines.sort(key=len)
    print(lines[-1])


# f1()

def f2():
    lines = open("words.txt").readlines()
    print(len(max(lines, key=len)))


# f2()

def f3():
    lines = open("words.txt").readlines()
    maxlen = len(max(lines, key=len))

    for i in lines:
        if len(i) == maxlen:
            print(i)


f3()
