# word = "engineer"
# d = {}
# n = 0
# for i in word:
#     d.setdefault(n, i)
#     n += 1
#
# print(d)

word = "python"
d = {}
for i in range(len(word)):
    d.setdefault(i, word[i])

print(d)
