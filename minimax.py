
'''
    p150 minimax psudo code
    function MINIMAX-SEARCH(game, state) returns an action
    player ←game.TO-MOVE(state)
    value, move←MAX-VALUE(game, state)
    return move

    function MAX-VALUE(game, state) returns a (utility, move) pair
    if game.IS-TERMINAL(state) then return game.UTILITY(state, player), null
    v←−∞
    for each a in game.ACTIONS(state) do
    v2, a2←MIN-VALUE(game, game.RESULT(state, a))
    if v2 > v then
    v, move←v2, a
    return v, move

    function MIN-VALUE(game, state) returns a (utility, move) pair
    if game.IS-TERMINAL(state) then return game.UTILITY(state, player), null
    v←+∞
    for each a in game.ACTIONS(state) do
    v2, a2←MAX-VALUE(game, game.RESULT(state, a))
    if v2 < v then
    v, move←v2, a
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
        v = min_value(gameState.result(a))
        if v > best_score:
            best_score = v
            best_move = a
    return best_move
 
def min_value(gameState):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    print('min val started')
    m = None
    v = float("-inf")
    for g in gameState.actions():
        v2 = max_value( gameState.result( g))
        if v2 < v:
            v = v2
            m = a
    print('min val:', v)
    return v
 
def max_value(gameState):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.

    function MAX-VALUE(game, state) returns a (utility, move) pair
    if game.IS-TERMINAL(state) then return game.UTILITY(state, player), null
    v←−∞
    for each a in game.ACTIONS(state) do
    v2, a2←MIN-VALUE(game, game.RESULT(state, a))
    if v2 > v then
    v, move←v2, a
    return v, move
    """

    print('max val started')
    m = None
    v = float("-inf")
    for g in gameState.actions():
        v2 = min_value(gameState.result( g))
        if v2 > v:
            v = v2
            m = a

    print('max val:', v)
    return v

    
