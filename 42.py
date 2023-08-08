pythons = ["farhad", "shima", "parsa", "sara", "aria"]
javas = ["shima", "ali", "farhad", "hadi", "mohammad"]
common = []

# for i in pythons:
#     for j in javas:
#         if i == j:  # Martabe ejrayi : 25
#             common.append(i)

for i in pythons:
    if i in javas:
        common.append(i)
print(common)
