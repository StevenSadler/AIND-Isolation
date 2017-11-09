"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
import sample_players

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""
    
    def timeLeft(self):
        return 1000
    
    def print_move(self, move):
        print (move[0],move[1])
        
    def print_moves(self, moves):
        for move in moves:
            self.print_move(move)

    def setUp(self, width=7, height=7):
        reload(game_agent)
        self.player1 = "Player1"
        self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2, width, height)
        
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO', 'test_upper FAILED')
        
    def xtest_get_legal_moves(self):
        self.setUp(3,2)
        game = self.game
        game.apply_move((0,0))
        moves = game.get_legal_moves()
        self.print_moves(moves)
        
        print('number of legal moves', len(moves))
        
    def xtest_minimax(self):
        self.setUp(5,5)
        game = self.game
        minimaxPlayer = game_agent.MinimaxPlayer(1, game_agent.custom_score)
        
        #self.game.apply_move((0,2))
        #self.game.apply_move((0,4))
        
        print('##################################################')
        print(game.to_string())
        print('##################################################')
        
        for i in range(25):
        
            moves = game.get_legal_moves()
            if len(moves) == 0:
                break
            
            self.print_moves(moves)
            print('active player', game.active_player)
            print('minimax number of legal moves', len(moves))
                   
            move = minimaxPlayer.get_move(game, self.timeLeft)
            self.print_move(move)
            game.apply_move((move))
            
            print('##################################################')
            print(game.to_string())
            print('##################################################', i)
        
        
        if game.is_loser(game.active_player):
            print(game.active_player, "has lost the game")
            print(game.inactive_player, "has won the game")
        
    def xtest_alphabeta(self):
        self.setUp(5,5)
        game = self.game
        alphaBetaPlayer = game_agent.AlphaBetaPlayer(1, game_agent.custom_score)
        
        #self.game.apply_move((0,2))
        #self.game.apply_move((0,4))
        
        print('##################################################')
        print(game.to_string())
        print('##################################################')
        
        for i in range(25):
        
            moves = game.get_legal_moves()
            if len(moves) == 0:
                break
            
            self.print_moves(moves)
            print('active player', game.active_player)
            print('alphaBetaPlayer number of legal moves', len(moves))
                   
            move = alphaBetaPlayer.get_move(game, self.timeLeft)
            self.print_move(move)
            game.apply_move((move))
            
            print('##################################################')
            print(game.to_string())
            print('##################################################', i)
        
        
        if game.is_loser(game.active_player):
            print(game.active_player, "has lost the game")
            print(game.inactive_player, "has won the game")
            
    def xtest_2_8x8(self):
        self.setUp(9,9)
        game = self.game
        game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 24, 18]
        #game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 47, 22]
        
        print(game.to_string())
        
        minimaxPlayer = game_agent.MinimaxPlayer()
        minimaxPlayer.time_left = self.timeLeft
        minimaxPlayer.minimax(game, 1)
        
    
        
    def xtest_a(self):
        self.setUp(9,9)
        game = self.game
        game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0,0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 57, 24]
        print(game.to_string())
        
        minimaxPlayer = game_agent.MinimaxPlayer(1, game_agent.custom_score_3)
        minimaxPlayer.time_left = self.timeLeft
        move = minimaxPlayer.minimax(game, 1)
        print()
        print("best move:")
        self.print_move(move)
        
    def xtest_b(self):
        self.setUp(9,9)
        game = self.game
        game._board_state = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0,0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 15, 13]
        print(game.to_string())
        
        minimaxPlayer = game_agent.MinimaxPlayer(2)
        minimaxPlayer.time_left = self.timeLeft
        move = minimaxPlayer.minimax(game, 1)
        print()
        print("best move:")
        self.print_move(move)
        
    def xtest_c(self):
        self.setUp(9,9)
        game = self.game
        game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 26, 20]
        print(game.to_string())
        
        minimaxPlayer = game_agent.MinimaxPlayer(2, game_agent.custom_score_3)
        minimaxPlayer.time_left = self.timeLeft
        move = minimaxPlayer.minimax(game, 2)
        print()
        print("best move:")
        self.print_move(move)
        
    def xtest_d(self):
        self.setUp(9,9)
        game = self.game
        game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0,0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 55, 56]
        print(game.to_string())
        
        minimaxPlayer = game_agent.MinimaxPlayer(2)
        minimaxPlayer.time_left = self.timeLeft
        move = minimaxPlayer.minimax(game, 2)
        print()
        print("best move:")
        self.print_move(move)
        
    def xtest_e(self):
        self.setUp(9,9)
        game = self.game
        game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 47, 56]
        print(game.to_string())
        
        minimaxPlayer = game_agent.MinimaxPlayer(2, sample_players.improved_score)
        minimaxPlayer.time_left = self.timeLeft
        move = minimaxPlayer.minimax(game, 2)
        print()
        print("best move:")
        self.print_move(move)
        
    def xtest_f(self):
        self.setUp(9,9)
        game = self.game
        game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 54, 59]
        print(game.to_string())
        
        minimaxPlayer = game_agent.MinimaxPlayer(2, sample_players.open_move_score)
        minimaxPlayer.time_left = self.timeLeft
        move = minimaxPlayer.minimax(game, 2)
        print()
        print("best move:")
        self.print_move(move)
        
    def xtest_alphabeta_e(self):
        self.setUp(7,2)
        game = self.game
        game._board_state = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 12, 4]
        print(game.to_string())
        
        alphaBetaPlayer = game_agent.AlphaBetaPlayer(2, sample_players.improved_score)
        alphaBetaPlayer.time_left = self.timeLeft
        move = alphaBetaPlayer.alphabeta(game, 1)
        print()
        print("best move:")
        self.print_move(move)
        
    def xtest_ab(self):
        self.setUp(7,2)
        game = self.game
        game._board_state = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 12, 4]
        print(game.to_string())
        
        alphaBetaPlayer = game_agent.AlphaBetaPlayer(2, sample_players.improved_score)
        alphaBetaPlayer.time_left = self.timeLeft
        
        # explore as if player 1 moves to 1,0
        move = (1,0)
        new_board = game.forecast_move(move)
        self.print_move(move)
        print("active player score", alphaBetaPlayer.get_active_player_score(new_board))
        print("inactive player score", alphaBetaPlayer.get_inactive_player_score(new_board))
        print("player 1 score", alphaBetaPlayer.get_player_score(new_board, self.player1))
        print()
        
        
        # explore as if player 1 moves to 1,4
        move = (1,4)
        new_board = game.forecast_move(move)
        self.print_move(move)
        print("active player score", alphaBetaPlayer.get_active_player_score(new_board))
        print("inactive player score", alphaBetaPlayer.get_inactive_player_score(new_board))
        print("player 1 score", alphaBetaPlayer.get_player_score(new_board, self.player1))
        print()
        
        
        ascore = alphaBetaPlayer.alphabeta(new_board, 2)
        print()
        print("best move score:", ascore)
        print("best move:")
        self.print_move(move)
        print()
        
        
        
        
    # the next 2 functions are good for testing walking the trees correctly
        
    def xtest_2_2x7(self):
        self.setUp(7,2)
        game = self.game
        game._board_state = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 12, 4]
        print(game.to_string())
        
        minimaxPlayer = game_agent.MinimaxPlayer(1, game_agent.custom_score)
        minimaxPlayer.time_left = self.timeLeft
        move = minimaxPlayer.minimax(game, 1)
        print()
        print("best move:")
        self.print_move(move)
        print()
        
    def xtest_ab_get_move(self):
        self.setUp(7,2)
        game = self.game
        game._board_state = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 12, 4]
        print(game.to_string())
        
        test_depth = 4
        
        alphaBetaPlayer = game_agent.AlphaBetaPlayer(test_depth, sample_players.improved_score)
        alphaBetaPlayer.time_left = self.timeLeft
        #move = alphaBetaPlayer.get_move(game, self.timeLeft)
        move = alphaBetaPlayer.alphabeta(game, test_depth)
        print()
        print("best move from calling alphabeta() with depth", test_depth, ":")
        self.print_move(move)
        print()
        
        move = alphaBetaPlayer.get_move(game, self.timeLeft)
        print()
        print("best move from calling get_move() with search_depth", test_depth, ":")
        self.print_move(move)
        print()
        
    # this is a test for a failed udacity test
    
    def test_2_2x7(self):
        self.setUp(9,9)
        game = self.game
        #game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 50]
        #game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 50]
        game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 46, 42]
        print(game.to_string())
        
        minimaxPlayer = game_agent.MinimaxPlayer(2, sample_players.improved_score)
        minimaxPlayer.time_left = self.timeLeft
        move = minimaxPlayer.minimax(game, 2)
        print()
        print("best move:")
        self.print_move(move)
        print()
        
    def test_ab_get_move(self):
        self.setUp(9,9)
        game = self.game
        #game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 50]
        #game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 30, 50]
        game._board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 46, 42]
        print(game.to_string())
        
        test_depth = 2
        
        alphaBetaPlayer = game_agent.AlphaBetaPlayer(test_depth, sample_players.improved_score)
        alphaBetaPlayer.time_left = self.timeLeft
        #move = alphaBetaPlayer.get_move(game, self.timeLeft)
        move = alphaBetaPlayer.alphabeta(game, test_depth)
        print()
        print("best move from calling gggg alphabeta() with depth", test_depth, ":")
        self.print_move(move)
        print()
        
        """
        move = alphaBetaPlayer.get_move(game, self.timeLeft)
        print()
        print("best move from calling get_move() with search_depth", test_depth, ":")
        self.print_move(move)
        print()"""
        
        
        
    def xtest_2_2x7(self):
        self.setUp(4,4)
        game = self.game
        game._board_state = [1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 15]
        print(game.to_string())
        
        minimaxPlayer = game_agent.MinimaxPlayer(2, sample_players.improved_score)
        minimaxPlayer.time_left = self.timeLeft
        move = minimaxPlayer.minimax(game, 2)
        print()
        print("best move:")
        self.print_move(move)
        print()
        
    def xtest_ab_get_move(self):
        self.setUp(4,4)
        game = self.game
        game._board_state = [1, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 15]
        print(game.to_string())
        
        test_depth = 2
        
        alphaBetaPlayer = game_agent.AlphaBetaPlayer(test_depth, sample_players.improved_score)
        alphaBetaPlayer.time_left = self.timeLeft
        #move = alphaBetaPlayer.get_move(game, self.timeLeft)
        move = alphaBetaPlayer.alphabeta(game, test_depth)
        print()
        print("best move from calling alphabeta() with depth", test_depth, ":")
        self.print_move(move)
        print()
        
        """
        move = alphaBetaPlayer.get_move(game, self.timeLeft)
        print()
        print("best move from calling get_move() with search_depth", test_depth, ":")
        self.print_move(move)
        print()"""
    
    
        
        
        
        
        


if __name__ == '__main__':
    unittest.main()
