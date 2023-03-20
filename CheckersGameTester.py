# Author: Kevin Sabbe
# GitHub username: sabbekosu
# Date: 3/19/2023
# Description: Unit testers for different functions of the Checkers game
import unittest
from CheckersGame import Checkers, Player, Checker

import unittest
from CheckersGame import Checkers, Checker, Player, InvalidPlayer, OutofTurn, InvalidSquare


class TestCheckersGame(unittest.TestCase):

    def setUp(self):
        self.game = Checkers()

    def test_create_player(self):
        game = Checkers()
        player1 = game.create_player("Alice", "Black")
        game.print_board()
        self.assertIsInstance(player1, Player)
        self.assertEqual(player1.player_name, "Alice")
        self.assertEqual(player1.piece_color, "Black")

    def test_black_piece_makes_a_regular_move_no_pieces_captured(self):
        player1 = self.game.create_player("Alice", "White")
        player2 = self.game.create_player("Bob", "Black")
        # Move a black piece to an empty space
        print(self.game.get_checker_details(4,7))
        self.game.play_game("Bob", (5, 6), (4, 7))

        # Check if the black piece has moved to the new position
        moved_black_piece = self.game.board[4][7]
        self.assertEqual("Black", moved_black_piece.color)

        # Check if the initial position is now empty
        empty_initial_position = self.game.board[5][6]
        self.assertIsNone(empty_initial_position)



if __name__ == '__main__':
    unittest.main()
