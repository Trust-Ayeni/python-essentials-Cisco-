import random

# initialize the board
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

# define the function for printing the board
def print_board():
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board[0] + "   |   " + board[1] + "   |   " + board[2] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board[3] + "   |   " + board[4] + "   |   " + board[5] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   " + board[6] + "   |   " + board[7] + "   |   " + board[8] + "   |")
    print("|       |       |       |")
    print("+-------+-------+-------+")

# define the function for checking if the game is over
def check_game_over():
    if board[0] == board[1] == board[2] != ' ':
        return True
    elif board[3] == board[4] == board[5] != ' ':
        return True
    elif board[6] == board[7] == board[8] != ' ':
        return True
    elif board[0] == board[3] == board[6] != ' ':
        return True
    elif board[1] == board[4] == board[7] != ' ':
        return True
    elif board[2] == board[5] == board[8] != ' ':
        return True
    elif board[0] == board[4] == board[8] != ' ':
        return True
    elif board[2] == board[4] == board[6] != ' ':
        return True
    elif ' ' not in board:
        return 'tie'
    else:
        return False

# make the first move - computer plays 'X' in the middle
board[4] = 'X'
print_board()

# game loop
while True:
    # user move
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if move < 1 or move > 9:
            print("Invalid input. Please enter a number between 1 and 9.")
            continue
        if board[move - 1] != ' ':
            print("That square is already occupied. Please choose another one.")
            continue
        break
    board[move - 1] = 'O'
    print_board()
    result = check_game_over()
    if result:
        if result == 'tie':
            print("The game ends in a tie.")
        else:
            print("Congratulations! You win!")
        break
    # computer move
    while True:
        computer_move = random.randint(1, 9)
        if board[computer_move - 1] == ' ':
            break
    board[computer_move - 1] = 'X'
    print_board
