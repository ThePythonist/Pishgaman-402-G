def f1(text):
    text = text.split()
    lengths = []

    for word in text:
        lengths.append(len(word))

    longest = max(lengths)

    for i in text:
        if len(i) == longest:
            print(i)


txt = "python is a high level programming language"


# f1(txt)

def f2(text):
    text = text.split()
    text.sort(key=len)
    print(text[-1])


txt = "python is a high level programming language"


# f2(txt)

def f3(text):
    text = text.split()
    print(text, end=' : ')
    print(max(text, key=len))


txt = "python is a high level programming language"
f3(txt)
