from random import randint

number = randint(1, 10)
chances = 5

print("Welcome to number guessing game")

while chances > 0:
    print(f"You have {chances} left")
    guess = input("Guess the number between 1-10 : ")

    try:
        guess = int(guess)

        if guess == number:
            print("You won!")
            break
        elif guess > number:
            if chances == 5:
                print("Try smaller")
        else:
            if chances == 5:
                print("Try bigger")

        chances -= 1

    except ValueError:
        print("Entry must be a number. Try again")
else:
    print("Game over! The number was", number)
