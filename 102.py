lines = open("words.txt").read().split("\n")
numbers = []

# for i in lines:
#     if i.isdigit():
#         numbers.append(i)
#

alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in lines:
    for j in alphabet:
        if j in i:
            break
    else:
        if len(i) != 0:
            numbers.append(i)
print(numbers)
