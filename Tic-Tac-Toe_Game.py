# Tic-Tac-Toe Game

# Tic-Tac-Toe is a two-player game played on a 3x3 grid. Players take turns marking empty cells with their symbol ('X' or 'O') to form a line of three symbols horizontally, vertically, or diagonally. The game ends when a player wins or there are no more empty cells.

# To simplify the implementation process, you can split it into 2 main steps:

# step 1: Drawing the board
board = [' ' for _ in range(9)]

# Function to print the board
def print_board():
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")


# Step 2: Drawing Tic-Tac-Toe

# Function to check if the game is over
def is_game_over():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return True
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return True
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ' or board[2] == board[4] == board[6] != ' ':
        return True
    # Check if the board is full
    if ' ' not in board:
        return True
    return False

# Function to check if a move is valid
def is_valid_move(move):
    if move < 0 or move >= 9:
        return False
    if board[move] != ' ':
        return False
    return True

# Function to make a move
def make_move(move, player):
    board[move] = player

# Function to get player's move
def get_move(player):
    while True:
        move = input("Player " + player + ", enter your move (0-8): ")
        try:
            move = int(move)
            if is_valid_move(move):
                return move
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Try again.")

# Function to determine the winner and loser
def determine_winner():
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            return board[i]
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] != ' ':
            return board[i]
    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        return board[0]
    if board[2] == board[4] == board[6] != ' ':
        return board[2]
    return None

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board()
    current_player = 'X'
    while not is_game_over():
        move = get_move(current_player)
        make_move(move, current_player)
        print_board()
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'
    winner = determine_winner()
    if winner:
        print("Player", winner, "wins!")
    else:
        print("It's a draw!")

# Start the game
play_game()


