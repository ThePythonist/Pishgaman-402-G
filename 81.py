fname = "reza"
lname = "yazdani"
percent = 70
# msg = f"""
# Moshtarake gerami {fname.capitalize()} {lname.capitalize()} shoma {percent}% az baste khod ra
# masraf kardid.
# """

msg = """
Moshtarake gerami {} {} shoma {}% az baste khod ra
masraf kardid.
""".format(fname.capitalize(), lname.capitalize(), percent)

print(msg)
