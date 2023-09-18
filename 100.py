lines = open("words.txt").readlines()
lines = lines[::-1]
open("reversedwords.txt","w").writelines(lines)
