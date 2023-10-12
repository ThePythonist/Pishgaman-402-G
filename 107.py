import random


# def generate(digits):
#     password = []
#
#     for i in range(digits):
#         # x = random.randint(0, 9)
#         x = random.choice(range(0, 10))
#         password.append(str(x))
#
#     password = "".join(password)
#     print(password)
#
#
# generate(8)

def generate(digits):
    password = [str(i) for i in random.sample(range(0, 10), digits)]
    # pswd = ",".join(password)
    pswd = "".join(password)
    print(pswd)


generate(6)
