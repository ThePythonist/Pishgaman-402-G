# This code is without player score records
def Game():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    end = False
    win_commbinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def Table():
        print('''
         {} | {} | {}
        -----------
         {} | {} | {}
        -----------
         {} | {} | {}
        '''.format(
            board[0],
            board[1],
            board[2],
            board[3],
            board[4],
            board[5],
            board[6],
            board[7],
            board[8],
        ))

    def Choice1():
        while True:
            a = input("Player 1 Choose : ")
            try:
                a = int(a)
                a -= 1
                if a in range(0, 9):
                    return a
                else:
                    print("That's not on the board. Try again")
            except ValueError:
                print("That's not a number. Try again")
                continue

    def Choice2():
        while True:
            a = input("Player 2 Choose : ")
            try:
                a = int(a)
                a -= 1
                if a in range(0, 9):
                    return a
                else:
                    print("That's not on the board. Try again")
            except ValueError:
                print("That's not a number. Try again")
                continue

    def Player1_Move():
        n = Choice1()
        if board[n] == "X" or board[n] == "O":
            print("\nYou can't go there. Try again")
            Player1_Move()
        else:
            board[n] = "X"

    def Player2_Move():
        n = Choice2()
        if board[n] == "X" or board[n] == "O":
            print("\nYou can't go there. Try again")
            Player2_Move()
        else:
            board[n] = "O"

    def check_board():
        count = 0
        for a in win_commbinations:
            if board[a[0]] == board[a[1]] == board[a[2]] == "X":
                print("**** Player 1 Wins ****")
                return True
            if board[a[0]] == board[a[1]] == board[a[2]] == "O":
                print("**** Player 2 Wins ****")
                return True
        for a in range(9):
            if board[a] == "X" or board[a] == "O":
                count += 1
            if count == 9:
                print("The game ends level")
                return True

    while not end:
        Table()
        end = check_board()
        if end == True:
            break
        Player1_Move()
        print()
        Table()
        end = check_board()
        if end == True:
            break
        Player2_Move()
        print()

    if input("Play again ? (y/n) : ") == "y":
        print()
        Game()
    else:
        pass


Game()
