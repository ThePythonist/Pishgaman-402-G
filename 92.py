lines = open("words.txt").readlines()
five_letters = []
for line in lines:
    if len(line) == 6:
        five_letters += [line]

print(five_letters[:100])
