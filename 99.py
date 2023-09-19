lines = open("words.txt").read().replace("\n", " ")
open("onelinewords.txt", "w").write(lines)
print("Done")
