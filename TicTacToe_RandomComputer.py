'''
TicTacToe game with one randomized player, on a 3x3 field.
Cool things to add / improve on:
	1. Improve syntax for efficiency / make the program more 'pythonic'
	2. Improve user-friendliness
	3. Add a time limit for each turn
	4. Make the game size dynamic
	5. Make computer intelligent
'''
import random

# Board: field numbers as printed
board = ['1','2','3','4','5','6','7','8','9']

# Lists to log moves made by each player
moves_players = [[],[]]

# The indexes across which players can win
wins = ((0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6))

# Pieces
xo = ['O', 'X']

# Execute game
def main():
    print_board()
    while True:
        turn(0)
        turn(1)

# Print board in 3x3 format
def print_board():
    print("\nCurrent board:\n")
    position = 0
    for i in range(3):
        for j in range(3):
            print(board[j + position] + " ", end = "")
        print()
        position = position + j + 1 # better way to do this? --> see dynamic version
    print()

# Iterate one turn
def turn(player):
    entry(player)
    print_board()
    game_status()

# Player input, repromt if input is invalid
def entry(player):
    if player == 0:
        while True:
            try:
                n = int(input(f"Player {player + 1}, what field do you want to play? "))
                if n-1 in range(0,9) and n-1 not in moves_players[0] and n-1 not in moves_players[1]: # Condense!
                    break
                else:
                    print("\nInvalid input, please try again:\n")
            except:
                print("\nInvalid input, please try again:\n")
    elif player == 1:
        while True:
            n = random.choice(board)
            if n not in xo:
                n = int(n)
                break
            else:
                pass
    # Log into game board
    if player == 0:
        board[n-1] = "X"
    else:
        board[n-1] = "O"
    # Log move
    moves_players[player].append(n-1)

# Checks game status: win, tie or next turn
def game_status():
    if won(moves_players[0]):
        print("Player 1 wins!")
        exit()
    elif won(moves_players[1]):
        print("Player 2 wins!")
        exit()
    elif board_full():
        print("It's a tie.")
        exit()
    else:
        print("New turn: ", end="")

# Check if player has won
def won(player):
    for i in range(len(wins)):
        match_counter = 0
        for j in range(len(wins[i])):
            if wins[i][j] in player:
                match_counter += 1
            if match_counter == 3:
                return True

# Checks for full board
def board_full():
    counter = 0
    for item in board:
        if item == "X" or item == "O": # Condense!
            counter += 1
    if counter == 9:
        return True
    return False

main()