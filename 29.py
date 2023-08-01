a = 0
b = 1
n = int(input("Enter the number of terms: "))
for i in range(n):
    print(a)
    # c = a + b
    # a = b
    # b = c
    a, b = b, a + b

# -----------------------------------

# for i in range(100):
#     if a < 100 :
#         print(a)
#         c = a + b
#         a = b
#         b = c
