# import math

print("Ax^2 + Bx + C = 0")
a = int(input("Enter A : "))
b = int(input("Enter B : "))
c = int(input("Enter C : "))

if a + b + c == 0:
    X1 = 1
    X2 = c / a
    print("X1 = ", X1)
    print("X2 = ", X2)

else:
    delta = (b ** 2) - (4 * a * c)
    print("Delta = ", delta)
    # radicialdelta = math.sqrt(delta)
    radicialdelta = delta ** 0.5
    if delta > 0 :
        X1 = ((-b) + radicialdelta) / (2 * a)
        X2 = ((-b) - radicialdelta) / (2 * a)
        print("X1 = ", X1)
        print("X2 = ", X2)
input("Press Any Key To Exit ")
