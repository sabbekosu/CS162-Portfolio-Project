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




if __name__ == '__main__':
    unittest.main()
