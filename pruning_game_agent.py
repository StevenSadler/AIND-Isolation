"""Finish all TODO items in this file to complete the isolation project, then
test your agent's strength against a set of known agents using tournament.py
and include the results in your report.
"""
import random


class SearchTimeout(Exception):
    """Subclass base exception for code clarity. """
    pass



def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    This should be the best heuristic function for your project submission.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    
    # improved_score
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))
    return float(own_moves - opp_moves)


def custom_score_2(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    
    # center_score
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    w, h = game.width / 2., game.height / 2.
    y, x = game.get_player_location(player)
    return float((h - y)**2 + (w - x)**2)


def custom_score_3(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """
    
    # open_move_score
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    return float(len(game.get_legal_moves(player)))


def print_move(move):
    print(move[0], move[1])

class IsolationPlayer:
    """Base class for minimax and alphabeta agents -- this class is never
    constructed or tested directly.

    ********************  DO NOT MODIFY THIS CLASS  ********************

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """
    def __init__(self, search_depth=3, score_fn=custom_score, timeout=10.):
        self.search_depth = search_depth
        self.score = score_fn
        self.time_left = None
        self.TIMER_THRESHOLD = timeout


class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************

        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1,-1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.

        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # TODO: finish this function!
        """print("minimax")
        print()
        print("depth", depth)
        print("active player", game.active_player)
        print("location", str(game.get_player_location(game.active_player)))
        print("legal moves", len(game.get_legal_moves()))
        print()
        print("inactive player", game.inactive_player)
        print("inactive player location", str(game.get_player_location(game.inactive_player)))
        print("legal moves", len(game.get_legal_moves(game.inactive_player)))
        print()"""
        
        
        best_score = float("-inf")
        best_move = (-1,-1)
        if depth > 0:
            for move in game.get_legal_moves():
                v = self.min_value(game.forecast_move(move), depth - 1)
                if v > best_score:
                    best_score = v
                    best_move = move
        return best_move
    
    def terminal_test(self, game):
        """ Return True if the game is over for the active player
        and False otherwise.
        """
        if game and len(game.get_legal_moves()) > 0:
            return False
        return True
        
    def min_value(self, game, depth):
        """ Return the value for a win (+1) if the game is over,
        otherwise return the minimum value over all legal child
        nodes.
        """
        #move_value = self.score(game, game.inactive_player)
        
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        
        if self.terminal_test(game):
            #return move_value
            return 1
             
        if depth == 0:
            move_value = self.score(game, game.inactive_player)
            #print ("min depth 0    value ", move_value, "player", game.inactive_player, "loc", game.get_player_location(game.inactive_player))
            return move_value
        
        #print ("min_value    depth", depth, "player", game.inactive_player, "loc", game.get_player_location(game.inactive_player))
        v = float("inf")
        for move in game.get_legal_moves():
            #print ("    depth ", depth, "player", game.active_player, "move", move)
            v = min(v, self.max_value(game.forecast_move(move), depth - 1))
        return v
    
    def max_value(self, game, depth):
        """ Return the value for a loss (-1) if the game is over,
        otherwise return the maximum value over all legal child
        nodes.
        """
        #move_value = self.score(game, game.active_player)
        
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        
        if self.terminal_test(game):
            #return move_value
            return -1
        
        if depth == 0:
            move_value = self.score(game, game.active_player)
            #print ("    max depth 0    value ", move_value, "player", game.inactive_player, "loc", game.get_player_location(game.inactive_player))
            return move_value
        
        #print ("   max depth", depth)
        v = float("-inf")
        for move in game.get_legal_moves():
            v = max(v, self.min_value(game.forecast_move(move), depth - 1))            
        return v


class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left
        
        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1,-1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            
        
            for depth in range(1, self.search_depth + 1):
                best_move = self.alphabeta(game, depth)                    
                print("depth searched", depth, "best_move:")
                print_move(best_move)
                    
            return best_move
                
            #return self.alphabeta(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move
    
        

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        
        
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        
        #if depth == 0 or self.terminal_test(game):
        #    return self.score(game, game.active_player)
        
        best_score = float("-inf")
        best_move = (-1,-1)
        
        for move in game.get_legal_moves():
            print_move(move)
            new_board = game.forecast_move(move)
            v = self.alphabeta_score(new_board, depth - 1, alpha, beta, True)
            if best_score < v:
                best_score = v
                best_move = move
                
        return best_move
    
        """
        print('depth', depth)
        next_depth = depth - 1
        if maximizingPlayer:
            v = float("-inf")
            for move in game.get_legal_moves():
                v = max(v, self.alphabeta(game.forecast_move(move), next_depth, alpha, beta, False))
                alpha = max(alpha, v)
                if beta <= alpha:
                    break
            return v
        else:
            v = float("inf")
            for move in game.get_legal_moves():
                v = min(v, self.alphabeta(game.forecast_move(move), depth - 1, alpha, beta, True))
                beta = min(beta, v)
                if beta <= alpha:
                    break
            return v"""
        
        """
        # TODO: finish this function!
        #print("alphabeta depth", depth)
        best_score = float("-inf")
        best_move = (-1,-1)
        
        if depth == 0 or self.terminal_test(game):
            return self.score(game, game.active_player) # , (-1,-1)
        
        
        
        if depth > 0:
            for move in game.get_legal_moves():
                self.print_move()
                next_game = game.forecast_move(move)
                #v, move_holder = self.alphabeta(next_game, depth -1 , alpha, beta)    
                v = self.max_value(game.forecast_move(move), depth - 1, alpha, beta)
                #v = self.score(game.forecast_move(move), game.active_player)
                if v > alpha:
                    alpha = v
                    best_move = move
                if alpha>=beta:
                  break;
        return best_move"""
        
    def alphabeta_score(self, game, depth, alpha=float("-inf"), beta=float("inf"), maximizingPlayer=True):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        
        #=======================================================================
        # if depth == 0 or self.terminal_test(game):
        #     return self.score(game, game.inactive_player)
        #=======================================================================
        
        print('depth', depth)
        if maximizingPlayer:
            if depth == 0 or self.terminal_test(game):
                return self.score(game, game.inactive_player)
            
            v = float("-inf")
            for move in game.get_legal_moves():
                v = max(v, self.alphabeta_score(game.forecast_move(move), depth - 1, alpha, beta, False))
                alpha = max(alpha, v)
                if beta <= alpha:
                    break
            return v
        else:
            if depth == 0 or self.terminal_test(game):
                return self.score(game, game.active_player)
            
            v = float("inf")
            for move in game.get_legal_moves():
                v = min(v, self.alphabeta_score(game.forecast_move(move), depth - 1, alpha, beta, True))
                beta = min(beta, v)
                if beta <= alpha:
                    break
            return v
    
    def terminal_test(self, game):
        """ Return True if the game is over for the active player
        and False otherwise.
        """
        if game and len(game.get_legal_moves()) > 0:
            return False
        #print("terminal test end - no legal moves")
        return True
    
    def get_active_player_score(self, game):
        return self.score(game, game.active_player)
    
    def get_inactive_player_score(self, game):
        return self.score(game, game.inactive_player)
    
    def get_player_score(self, game, player):
        return self.score(game, player)
    
    """def get_maximizing_player_score(self, game, maximizingPlayer):
        if maximizing_player:
            return self.score(game, self.player1)"""
    
class AlphaBetaPlayerMinMaxCalls(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.

        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left
        
        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_score = float("-inf")
        best_move = (-1,-1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            
        
            """for depth in range(1, self.search_depth + 1):
                print("depth", depth)
                move = self.alphabeta(game, depth)
                new_board = game.forecast_move(move)
                score = self.score(new_board, game.inactive_player)
                if best_score < score:
                    best_score = score
                    best_move = move
                    
            return best_move"""
                
            return self.alphabeta(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move
    
        

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf")):
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.

        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md

        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.

            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        
        
        # TODO: finish this function!
        #print("alphabeta depth", depth)
        best_score = float("-inf")
        best_move = (-1,-1)
        
        if depth == 0 or self.terminal_test(game):
            return self.score(game, game.active_player) # , (-1,-1)
        
        
        
        if depth > 0:
            for move in game.get_legal_moves():
                self.print_move()
                next_game = game.forecast_move(move)
                #v, move_holder = self.alphabeta(next_game, depth -1 , alpha, beta)    
                v = self.max_value(game.forecast_move(move), depth - 1, alpha, beta)
                #v = self.score(game.forecast_move(move), game.active_player)
                if v > alpha:
                    alpha = v
                    best_move = move
                if alpha>=beta:
                  break;
        return best_move
    
    def terminal_test(self, game):
        """ Return True if the game is over for the active player
        and False otherwise.
        """
        if game and len(game.get_legal_moves()) > 0:
            return False
        #print("terminal test end - no legal moves")
        return True
    
    def max_value(self, game, depth, alpha, beta):
        """ Return the value for a loss (-1) if the game is over,
        otherwise return the maximum value over all legal child
        nodes.
        """
        move_value = self.score(game, game.active_player)
        #print ("max_value    depth", depth, "player", game.inactive_player, "loc", game.get_player_location(game.inactive_player), "score", move_value)
        
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        
        if self.terminal_test(game):
            #return move_value
            return -1
            pass
        
        if len(game.get_legal_moves()) == 0:
            return float("-inf")
        
        if depth == 0:
            #move_value = self.score(game, game.active_player)
            return move_value
        
        
        
        v = float("-inf")
        for move in game.get_legal_moves():
            v = max(v, self.min_value(game.forecast_move(move), depth - 1, alpha, beta))
            if v >= beta:
                return v
            
            alpha = max(alpha, v)
        return v
        
        
        
        """
        
        #print("max_value depth", depth, "   legal moves", len(game.get_legal_moves()))
        v = float("-inf")
        
        for move in game.get_legal_moves():
            #v = max(v, self.score(game.forecast_move(move), game.active_player))
            
            if depth > 0:
                v = max(v, self.min_value(game.forecast_move(move), depth - 1, alpha, beta))
            else:
                v = max(v, self.score(game, game.active_player))
            
            if v >= beta:
                return v
            
            alpha = max(alpha, v)
            
        return v"""
    
    def min_value(self, game, depth, alpha, beta):
        """ Return the value for a win (+1) if the game is over,
        otherwise return the minimum value over all legal child
        nodes.
        """
        move_value = self.score(game, game.inactive_player)
        #print ("max_value    depth", depth, "player", game.inactive_player, "loc", game.get_player_location(game.inactive_player), "score", move_value)
        
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        
        if self.terminal_test(game):
            #return move_value
            return 1
            pass
        
        if len(game.get_legal_moves()) == 0:
            return float("inf")
        
        if depth == 0:
            #move_value = self.score(game, game.inactive_player)
            return move_value
        
        
        
        v = float("inf")
        for move in game.get_legal_moves():
            v = min(v, self.max_value(game.forecast_move(move), depth - 1, alpha, beta))
            if v <= alpha:
                return v
            
            beta = min(beta, v)
        return v
        
        """
        #print("min_value depth", depth, "   legal moves", len(game.get_legal_moves()))
        v = float("inf")
        for move in game.get_legal_moves():
            #v = min(v, self.score(game.forecast_move(move), game.active_player))
            
            
            if depth > 0:
                v = min(v, self.max_value(game.forecast_move(move), depth - 1, alpha, beta))
            else:
                v = min(v, self.score(game, game.active_player))
            
            if v <= alpha:
                return v
            
            beta = min(beta, v)
            
        return v"""
