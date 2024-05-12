import math

def alpha_beta(state, depth, alpha, beta, maximizingPlayer):
    if depth == 0 or is_terminal(state):
        return evaluate(state), None
    
    if maximizingPlayer:
        maxEval = -math.inf
        best_move = None
        for move in get_possible_moves(state):
            child_state = make_move(state, move)
            eval, _ = alpha_beta(child_state, depth - 1, alpha, beta, False)
            if eval > maxEval:
                maxEval = eval
                best_move = move
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return maxEval, best_move
    else:
        minEval = math.inf
        best_move = None
        for move in get_possible_moves(state):
            child_state = make_move(state, move)
            eval, _ = alpha_beta(child_state, depth - 1, alpha, beta, True)
            if eval < minEval:
                minEval = eval
                best_move = move
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return minEval, best_move

def is_terminal(state):
    # Check if the state is terminal
    pass

def evaluate(state):
    # Evaluate the state and return a score
    pass

def get_possible_moves(state):
    # Get all possible moves from the current state
    pass

def make_move(state, move):
    # Apply a move to the current state and return to the new state
    pass
