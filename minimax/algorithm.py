from copy import deepcopy
from othello.constants import PLAYER, AI

def minimax(position, depth, max_player):
    #position is an object
    #depth is an int to show how far to go
    #max_player checks if ai wants to maximise sore or minimise score

    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    
    if max_player:
        maxEval = float("-inf")
        best_move = None
        for move in get_all_moves(position, AI, PLAYER):
            evaluation = minimax(move, depth-1, False)[0]
            maxEval = max(maxEval,evaluation)
            if maxEval == evaluation:
                best_move = move

        return maxEval, best_move
    
    else:
        minEval = float("inf")
        best_move = None
        for move in get_all_moves(position, PLAYER, AI):
            evaluation = minimax(move, depth-1, True)[0]
            minEval = min(minEval,evaluation)
            if minEval == evaluation:
                best_move = move

        return minEval, best_move

def simulate_move(move, board, colour, anticolour):
    board.turn(move[0],move[1], colour, anticolour)

    return board

def get_all_moves(board, colour, anticolour):
    moves = []

    valid_moves = board.get_valid_moves(colour, anticolour)
    for move in valid_moves:
        temp_board = deepcopy(board)
        new_board = simulate_move(move, temp_board, colour, anticolour)
        moves.append(new_board)

    return moves
