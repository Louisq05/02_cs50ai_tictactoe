"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None
# Initialing the game variables

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
# Initialing the board as empty

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_counter = 0
    o_counter = 0

    for row in board :
        for col in board[row] :
            if board[row][col] == X :
                        x_counter += 1
            elif board[row][col] == O :
                        o_counter += 1
    if x_counter == o_counter == 0 :
         return X
    return max(x_counter, o_counter)

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for row in board :
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


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
