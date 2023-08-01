flag = 1

while flag:
    entry = input("Type something : ")
    print(entry)
    if entry == "exit":
        flag = 0
        # break
else:
    print("Flag has turned into exit")
