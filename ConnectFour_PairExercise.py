# Python implementation of a (dynamic) Connect4 Game by Andreas and Elsita
# LEFT TO DO: function that checks for diagonal wins

# board
row = 6
col = 7
list = [[] for x in range(col)] 

# set the number of players and game status
player_count = 2
game_over = False


# play game
def play_game():
  print_intro()
  print_board(list)
  nextPlayer = alternate(player_count)
  while not game_over:
    one_turn(nextPlayer.__next__())

# prints intro :-)
def print_intro():
  print("Welcome Andreas' and Elsita's implementation of Connect-Four!\n\nYou can set:\n 1. the size of the board\n 2. the number of players\n\nEnjoy!!")

# one turn
def one_turn(player_id):
  print()
  input_move(player_id)
  print_board(list)
  check_vertical(player_id)
  check_horizontal(player_id)
  check_vertical(player_id)

# print board
def print_board(list):
  print('\nBoard:')
  rows = 1
  for item in list:
    print(f'{rows}: ', end='')
    print(item)
    rows += 1

# input player's move
def input_move(player_id):
  while True:
    try:
      move_col = int(input(f'Player {player_id}, please choose a column: ')) - 1 
      if move_col in range(col):
        list[move_col].append(player_id)
        break
      else:
        print(f"\nInvalid input, please pick a column from 1 to {col}: \n")
    except:
      print("\nInvalid input, please try again:\n")
      return False

# cycles through players
def alternate(player_count):
  while True:
    for i in range(player_count):
      yield i+1

# check for vertical win
def check_vertical(player_id):
  counter = 0
  for i in range(col):
    for j in range(len(list[i])):
      if list[i][j] == player_id:
        counter += 1
      else:
        counter = 0 # had trouble making a "reset counter funciton"
    if counter >= 4:
      print(f"Vertical win for Player {player_id} across column #{i+1}!")
      global game_over
      game_over = True
      break
    else:
      counter = 0

# check for horizontal win
def check_horizontal(player_id):
  counter = 0
  for j in range(row):
    for i in range(col):
      try:
        list[i][j]
        if list[i][j] == player_id:
          counter += 1
        else:
          counter = 0
      except:
        pass
    if counter >= 4:
      print(f"Horizontal win for Player {player_id} across row #{j+1}!")
      global game_over
      game_over = True
      break
    else:
      counter = 0

# check for diagonal win (in progress)
def check_vertical(player_id):
  counter = 0
  for i in range(col):
    for index, row in enumerate(list):
      try: # handle for index out of range
        position = row[index-i] # case: negative indexes
        if position == player_id:
          counter += 1
          print(f"Counter {counter}, position {position}, i: {i}")
      except:
        pass
      if counter >= 4:
        print(f"Diagonal win in starting at column {i+1}")
        global game_over
        game_over = True
        counter = 0
        break
      

play_game()
