lines = open("words.txt").readlines()
inglist = []
for line in lines:
    # if line[-4:-1] == "ing\n":
    if line[-4:-1] == "ing":
        inglist.append(line)

print(inglist)
