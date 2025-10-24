"""
Tic Tac Toe Player
"""

import math
import copy

# Initialing the game variables
X = "X"
O = "O"
EMPTY = None

# Initialing the board as empty
def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_counter = 0
    o_counter = 0

    for row in range(len(board)) :                       # Counts the numer of symbols on the board
        for col in range(len(board[row])) :
            if board[row][col] == X :
                        x_counter += 1
            elif board[row][col] == O :
                        o_counter += 1
    if x_counter == o_counter :              # If == 0 or same number, X turn
         return X
    return min(x_counter, o_counter)

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for row in board :                                 # Checks for empty cells
         for col in board[row] :
              if board[row][col] == EMPTY :
                   actions += (row, col)
    if len(actions) == 0 :
         return
    return actions                                      # action[0] = row | action[1] = col


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if not action : 
         raise ValueError
    played_board = copy.deepcopy(board)                 # deepocopy the board for MiniMax
    played_board[action[0]][action[1]] = player(board)  # implement player action on the board 
    return played_board                                


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # ROWS
    for i in range(len(board)) :                                               # For each row
         if board[i][0] == board[i][1] == board[i][2] == X :# If the row is complete with Xs
              print(1)
              return X                          # X wins
         if board[i][0] == board[i][1] == board[i][2] == O :   # If the row is complete with Os
              return O                          # O wins
    # COLUMNS
    for i in range(len(board[0])) :
         if board[0][i] == board[1][i] == board[2][i] == X :   # If the column is complete with Xs
              print(2)
              return X                          # X wins
         if board[0][i] == board[1][i] == board[2][i] == O :   # If the column is complete with Os
              return O                         # O wins
    # DIAGONALS
    if board[0][0] == board[1][1] == board[2][2] == X or board[0][2] == board[1][1] == board[2][0] == X : # If one diag is complete with Xs
        print(3)
        return X                                # X wins
    if board[0][0] == board[1][1] == board[2][2] == O or board[0][2] == board[1][1] == board[2][0] == O : # If one diag is complete with Xs
        return O                                # O wins
    # NO WINNER
    return None 


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == False :
     for row in range(len(board)) :
          for col in range(len(board[0])) :
               if board[row][col] == EMPTY :
                    return False
    else :
         return winner(board)
    


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X :
         return 1           # If X wins, utility = 1
    elif winner(board) == O :
         return -1          # Elif O wins, utility = -1
    else :
         return 0           # Else, utility = 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
