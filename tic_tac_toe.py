import random

# Display the board
def display_board():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])
    print()


# Check whether a player has won
def check_winner(player):
    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combination in winning_combinations:
        if (board[combination[0]] == player and
            board[combination[1]] == player and
            board[combination[2]] == player):
            return True

    return False


# Check whether the board is full
def board_full():
    for cell in board:
        if cell == " ":
            return False
    return True


# Computer's move
def computer_move():
    empty_cells = []

    for i in range(9):
        if board[i] == " ":
            empty_cells.append(i)

    # Try to win
    for position in empty_cells:
        board[position] = "O"

        if check_winner("O"):
            return

        board[position] = " "

    # Try to block the player
    for position in empty_cells:
        board[position] = "X"

        if check_winner("X"):
            board[position] = "O"
            return

        board[position] = " "

    # Take the center if available
    if board[4] == " ":
        board[4] = "O"
        return

    # Otherwise choose a random empty position
    position = random.choice(empty_cells)
    board[position] = "O"


# Main program
board = [" " for i in range(9)]

print("TIC TAC TOE")
print("You are X")
print("Computer is O")

while True:

    # Player's turn
    display_board()

    position = int(input("Enter position (1-9): "))

    if position < 1 or position > 9:
        print("Invalid position")
        continue

    index = position - 1

    if board[index] != " ":
        print("Cell occupied")
        continue

    board[index] = "X"

    if check_winner("X"):
        display_board()
        print("You win!")
        break

    if board_full():
        display_board()
        print("It's a draw!")
        break

    # Computer's turn
    computer_move()

    print("Computer has made its move.")

    if check_winner("O"):
        display_board()
        print("Computer wins!")
        break

    if board_full():
        display_board()
        print("It's a draw!")
        break