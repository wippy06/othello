from copy import deepcopy
from othello.constants import PLAYER, AI, DEPTH

def minimax(position, depth, max_player, alpha, beta, weight, transpositionTable):
    #position is an object
    #depth is an int to show how far to go
    #max_player checks if ai wants to maximise sore or minimise score

    positionKey = hash(str(position.board))

    if positionKey in transpositionTable and depth != DEPTH:
        return transpositionTable[positionKey]

    if depth == 0 or position.winner() != None:
        return position

    best_move = position

    if max_player:
        maxEval = float("-inf")
        for move in get_all_moves(position, AI, PLAYER):
            evaluation = minimax(move, depth-1, False, alpha, beta, weight, transpositionTable).evaluate(weight)
            maxEval = max(maxEval,evaluation)

            if maxEval == evaluation:
                best_move = move

            alpha = max( alpha, maxEval)
            if beta <= alpha:
                break
    
    else:
        minEval = float("inf")
        for move in get_all_moves(position, PLAYER, AI):
            evaluation = minimax(move, depth-1, True, alpha, beta, weight, transpositionTable).evaluate(weight)
            minEval = min(minEval,evaluation)

            if minEval == evaluation:
                best_move = move

            beta = min( beta, minEval)
            if beta <= alpha:
                break

    if depth != 1:
        transpositionTable[positionKey] = best_move

    return best_move

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
