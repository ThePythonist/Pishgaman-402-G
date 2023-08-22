def check(word):
    if len(word) == len(set(word)):
        print("Tekrari nadarad")
    else:
        print("Tekrari darad")


check("mohammad")
