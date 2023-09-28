tedad = int(input("How many files do you need ? "))
extention = input("Enter the format of the files ? ")

for i in range(tedad) :
	f = open(f"{i+1}.{extention}","w")

print("Done")
