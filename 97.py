# lines = open("words.txt").readlines()
# new_lines = []
# for i in lines :
#     new_lines.append(i[:-1])
#
# print(new_lines)
# -----------------------------------------
# lines = open("words.txt").read()
# print(lines.replace("\n"," "))
# -----------------------------------------
# lines = open("words.txt").read().split("\n")
# print(lines)
# -----------------------------------------
lines = open("words.txt").readlines()
new_lines = []
for i in lines :
    new_lines.append(i.strip())

print(new_lines)
