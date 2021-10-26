"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None

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
    try:
        Xcount = 0
        Ocount = 0
        for i in board:
            for j in i:
                if j==X:
                    Xcount+=1
                if j==O:
                    Ocount+=1
        if Xcount<=Ocount:
            return X
        else:
            return O
    except:
        raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    try:
        # we need to return a set, which is unordered.
        # therefore we"ll need to utilize the enumerate function
        moves=set()
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell==EMPTY:
                    moves.add((i, j))
        return moves
    except:
        raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action in actions(board):
        new_board=copy.deepcopy(board)
        i=action[0]
        j=action[1]
        new_board[i][j]=player(new_board)
        return new_board
    else:
        raise NotImplementedError

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    try:
        Xcount=0
        Ocount=0
        if board[0][0]==board[0][1]==board[0][2]:
            if board[0][0]==X:
                Xcount+=1
            elif board[0][0]==O:
                Ocount+=1

        elif board[1][0]==board[1][1]==board[1][2]:
            if board[1][0]==X:
                Xcount+=1
            elif board[1][0]==O:
                Ocount+=1

        elif board[2][0]==board[2][1]==board[2][2]:
            if board[2][0]==X:
                Xcount+=1
            elif board[2][0]==O:
                Ocount+=1

        elif board[0][0]==board[1][0]==board[2][0]:
            if board[0][0]==X:
                Xcount+=1
            elif board[0][0]==O:
                Ocount+=1

        elif board[0][1]==board[1][1]==board[2][1]:
            if board[0][1]==X:
                Xcount+=1
            elif board[0][1]==O:
                Ocount+=1

        elif board[0][2]==board[1][2]==board[2][2]:
            if board[0][2]==X:
                Xcount+=1
            elif board[0][2]==O:
                Ocount+=1

        elif board[0][0]==board[1][1]==board[2][2]:
            if board[0][0]==X:
                Xcount+=1
            elif board[0][0]==O:
                Ocount+=1

        elif board[0][2]==board[1][1]==board[2][0]:
            if board[0][2]==X:
                Xcount+=1
            elif board[0][2]==O:
                Ocount+=1

        if Xcount>0:
            return X
        elif Ocount>0:
            return O
        else:
            return None
    except:
        raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    try:
        count=0
        for i in board:
            for j in i:
                if j is not EMPTY:
                    count+=1

        if winner(board) is not None or count==9:
            return True
        else:
            return False
    except:
        raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    try:
        playr=winner(board)
        if playr==X:
            return 1
        elif playr==O:
            return -1
        else:
            return 0
    except:
        raise NotImplementedError


def prim_value(playr):
    #returns the lowest value for the player from which we can compare as we progress
    if playr==X:
        return float('-inf')
    else:
        return float('inf')


def helper(board, best):
    # returns best score for our minimax function
    # also utilizes alpha beta pruning to improve running time
    if terminal(board):
        #base case
        return utility(board)
    playr=player(board)
    value=prim_value(playr)
    #recursion
    for move in actions(board):
        new_board=result(board, move)
        new_value=helper(new_board, value)
        if playr==X:
            if new_value > best:
                return new_value
            value=max(new_value, value)

        if playr==O:
            if new_value<best:
                return new_value
            value=min(new_value, value)
    return value

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    try:
        if terminal(board):
            return None
        #the first move
        if board==initial_state():
            return 0, 1
        playr=player(board)
        value=prim_value(playr)
        for action in actions(board):
            new_board=result(board, action)
            new_value=helper(new_board, value)

            if playr==X:
                new_value=max(new_value, value)

            if playr==O:
                new_value=min(new_value, value)

            if new_value is not value:
                value=new_value
                best_move=action

        return best_move
    except:
        raise NotImplementedError

