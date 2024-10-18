
'''
    p154 abs psudo code
    function ALPHA-BETA-SEARCH(game, state) returns an action
    player ←game.TO-MOVE(state)
    value, move←MAX-VALUE(game, state,−∞
    , +∞)
    return move

    function MAX-VALUE(game, state, α, β) returns a (utility, move) pair
    if game.IS-TERMINAL(state) then return game.UTILITY(state, player), null
    v←−∞
    for each a in game.ACTIONS(state) do
    v2, a2←MIN-VALUE(game, game.RESULT(state, a), α, β)
    if v2 > v then
    v, move←v2, a
    α ←MAX(α, v)
    if v ≥β then return v, move
    return v, move

    function MIN-VALUE(game, state, α, β) returns a (utility, move) pair
    if game.IS-TERMINAL(state) then return game.UTILITY(state, player), null
    v←+∞
        for each a in game.ACTIONS(state) do
            v2, a2←MAX-VALUE(game, game.RESULT(state, a), α, β)
            if v2 < v then
                v, move←v2, a
                β ←MIN(β, v)
            if v ≤α then return v, move
    return v, move
'''


def alpha_beta_search(gameState):
    """ Return the move along a branch of the game tree that
    has the best possible value.  A move is a pair of coordinates
    in (column, row) order corresponding to a legal move for
    the searching player.
    
    You can ignore the special case of calling this function
    from a terminal state.
    """

    print('abs started')
    alpha = float("-inf")
    beta = float("inf")
    best_score = float("-inf")
    best_move = None
    for a in gameState.actions():
        v = min_value(gameState.result(a), alpha, beta)
        if v > best_score:
            best_score = v
            best_move = a
    return best_move
 
def min_value(gameState, alpha, beta):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    u = gameState.utility(gameState.player())
    if u != 0: return u
    
    v = float("inf")
    for g in gameState.actions():
        v2 = max_value( gameState.result( g), alpha, beta)
        if v2 < v:
            v = v2
            beta = min(beta, v)
        if v <= alpha: break

    # print('min val:', v)
    return v
 
def max_value(gameState, alpha, beta):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.

   function MAX-VALUE(game, state, α, β) returns a (utility, move) pair
    if game.IS-TERMINAL(state) then return game.UTILITY(state, player), null
    v←−∞
    for each a in game.ACTIONS(state) do
        v2, a2←MIN-VALUE(game, game.RESULT(state, a), α, β)
        if v2 > v then
            v, move←v2, a
            α ←MAX(α, v)
        if v ≥β then return v, move
    return v, move
    """
    u = gameState.utility(gameState.player())
    if u != 0: return u

    v = float("-inf")
    for g in gameState.actions():
        v2 = min_value(gameState.result( g), alpha, beta)
        if v2 > v:
            v = v2
            alpha = max(alpha, v)
        if v >= beta: break
    # print('max val:', v)
    return v

    
