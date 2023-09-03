pn = input("Enter your phone number : ")

if pn[0] == "0":
    pn = pn.replace("0", "+98", 1)
else:
    pn = f"+98{pn}"

print(pn)
