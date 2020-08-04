###### # Firstly make a grid

from IPython.display import clear_output

def display_board(board):
    clear_output()      # Clears the board after every go
    print('_'+board[7]+'_|_'+board[8]+'_|_'+board[9]+'_')
    print('_'+board[4]+'_|_'+board[5]+'_|_'+board[6]+'_')
    print('_'+board[1]+'_|_'+board[2]+'_|_'+board[3]+'_')   # (board) input must be list of strings
    

# Player 1 decides which letter to be, X or O.
def player_input():
    marker=''
    
    while not (marker == 'X' or marker == 'O'):                    # Only continues if letters X or O are inputted
        marker = input('Player 1, do you want to be X or O? ').upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')       
    
# Make a function returning a letter corresponding to number on board

def place_marker(board, marker, position):
    board[position] = marker                # Uses list indexing and puts a letter in for it
    
# Next write a function that returns when someone has won

def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

# Next write function which decides which player goes first

import random

def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'
    
# Next write a function that returns a boolean if there's a space free on the grid

def space_check(board,position):
    return board[position] == ' '

# Next write a funtion that returns if the board is full

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

# Next write a function that asks input from player and checks wether space is free

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input("Choose your next position: (1-9)"))
        
    return position 

# Next write a function that returns a boolean if they want to play again

def replay():
    return input("Do you want to play again? Yes or no")[0].lower() == 'y'

# Now use all functions and while loops to create the game
#INTRO
while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break