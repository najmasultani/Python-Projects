# Title: Python Rock-Paper-Scissors Game
# Description: This is a simple rock-paper-scissors game implemented in Python. Players enter their choices, and the program determines the winner based on the game rules.

# Get player names
player1 = input("Enter your name: ")
player2 = input("Enter your name: ")

# Get player choices
player1_input = input("%s, choose rock, paper, or scissors: " % player1)
player2_input = input("%s, choose rock, paper, or scissors: " % player2)

def compare(player1_input, player2_input):
    if player1_input == player2_input:
        return "It's a tie!"
    elif player1_input == 'rock':
        if player2_input == 'scissors':
            return "Rock wins!"
        else:
            return "Paper wins!"
    elif player1_input == 'scissors':
        if player2_input == 'paper':
            return "Scissors win!"
        else:
            return "Rock wins!"
    elif player1_input == 'paper':
        if player2_input == 'rock':
            return "Paper wins!"
        else:
            return "Scissors win!"
    else:
        return "Invalid input! You have not entered rock, paper, or scissors. Try again."

# Print the result
print(compare(player1_input, player2_input))
