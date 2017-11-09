"""
This file contains the `Board` class, which implements the rules for the
game Isolation as described in lecture, modified so that the players move
like knights in chess rather than queens.

You MAY use and modify this class, however ALL function signatures must
remain compatible with the defaults provided, and none of your changes will
be available to project reviewers.
"""
import random
import timeit
from copy import copy

TIME_LIMIT_MILLIS = 150


class Board(object):
    """Implement a model for the game Isolation assuming each player moves like
    a knight in chess.

    Parameters
    ----------
    player_1 : object
        An object with a get_move() function. This is the only function
        directly called by the Board class for each player.

    player_2 : object
        An object with a get_move() function. This is the only function
        directly called by the Board class for each player.

    width : int (optional)
        The number of columns that the board should have.

    height : int (optional)
        The number of rows that the board should have.
    """
    BLANK = 0
    NOT_MOVED = None

    def __init__(self, player_1, player_2, width=7, height=7):
        self.width = width
        self.height = height
        self.move_count = 0
        self._player_1 = player_1
        self._player_2 = player_2
        self._active_player = player_1
        self._inactive_player = player_2

        # The last 3 entries of the board state includes initiative (0 for
        # player 1, 1 for player 2) player 2 last move, and player 1 last move
        self._board_state = [Board.BLANK] * (width * height + 3)
        self._board_state[-1] = Board.NOT_MOVED
        self._board_state[-2] = Board.NOT_MOVED

    def hash(self):
        return str(self._board_state).__hash__()

    @property
    def active_player(self):
        """The object registered as the player holding initiative in the
        current game state.
        """
        return self._active_player

    @property
    def inactive_player(self):
        """The object registered as the player in waiting for the current
        game state.
        """
        return self._inactive_player

    def get_opponent(self, player):
        """Return the opponent of the supplied player.

        Parameters
        ----------
        player : object
            An object registered as a player in the current game. Raises an
            error if the supplied object is not registered as a player in
            this game.

        Returns
        -------
        object
            The opponent of the input player object.
        """
        if player == self._active_player:
            return self._inactive_player
        elif player == self._inactive_player:
            return self._active_player
        raise RuntimeError("`player` must be an object registered as a player in the current game.")

    def copy(self):
        """ Return a deep copy of the current board. """
        new_board = Board(self._player_1, self._player_2, width=self.width, height=self.height)
        new_board.move_count = self.move_count
        new_board._active_player = self._active_player
        new_board._inactive_player = self._inactive_player
        new_board._board_state = copy(self._board_state)
        return new_board

    def forecast_move(self, move):
        """Return a deep copy of the current game with an input move applied to
        advance the game one ply.

        Parameters
        ----------
        move : (int, int)
            A coordinate pair (row, column) indicating the next position for
            the active player on the board.

        Returns
        -------
        isolation.Board
            A deep copy of the board with the input move applied.
        """
        new_board = self.copy()
        return new_board


    def get_player_location(self, player):
        """Find the current location of the specified player on the board.

        Parameters
        ----------
        player : object
            An object registered as a player in the current game.

        Returns
        -------
        (int, int) or None
            The coordinate pair (row, column) of the input player, or None
            if the player has not moved.
        """
        if player == self._player_1:
            if self._board_state[-1] == Board.NOT_MOVED:
                return Board.NOT_MOVED
            idx = self._board_state[-1]
        elif player == self._player_2:
            if self._board_state[-2] == Board.NOT_MOVED:
                return Board.NOT_MOVED
            idx = self._board_state[-2]
        else:
            raise RuntimeError(
                "Invalid player in get_player_location: {}".format(player))
        w = idx // self.height
        h = idx % self.height
        return (h, w)

    def get_legal_moves(self, player=None):
        """Return the list of all legal moves for the specified player.

        Parameters
        ----------
        player : object (optional)
            An object registered as a player in the current game. If None,
            return the legal moves for the active player on the board.

        Returns
        -------
        list<(int, int)>
            The list of coordinate pairs (row, column) of all legal moves
            for the player constrained by the current game state.
        """
    
        return [self.get_player_location(self.active_player), self.get_player_location(self.inactive_player)]

    def to_string(self, symbols=['1', '2']):
        """Generate a string representation of the current game state, marking
        the location of each player and indicating which cells have been
        blocked, and which remain open.
        """
        p1_loc = self._board_state[-1]
        p2_loc = self._board_state[-2]

        col_margin = len(str(self.height - 1)) + 1
        prefix = "{:<" + "{}".format(col_margin) + "}"
        offset = " " * (col_margin + 3)
        out = offset + '   '.join(map(str, range(self.width))) + '\n\r'
        for i in range(self.height):
            out += prefix.format(i) + ' | '
            for j in range(self.width):
                idx = i + j * self.height
                if not self._board_state[idx]:
                    out += ' '
                elif p1_loc == idx:
                    out += symbols[0]
                elif p2_loc == idx:
                    out += symbols[1]
                else:
                    out += '-'
                out += ' | '
            out += '\n\r'

        return out

