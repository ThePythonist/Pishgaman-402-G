while True:
    number = int(input("Enter a number : "))

    if len(str(number)) == 5:
        for i in str(number):
            print(i)
        break
    else:
        print("Number must be 5 digits")
