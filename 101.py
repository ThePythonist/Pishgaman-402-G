lines = open("words.txt").readlines()
rev_lines = []

for i in lines:
    rev_lines.append(i[::-1])

open("reversedlines.txt", "w").writelines(rev_lines)
