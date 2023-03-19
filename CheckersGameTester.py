# Author: Kevin Sabbe
# GitHub username: sabbekosu
# Date: 3/19/2023
# Description: Unit testers for different functions of the Checkers game
import unittest
from CheckersGame import Checkers, Player, Checker


class TestCheckers(unittest.TestCase):

    def test_create_player(self):
        checkers = Checkers()
        player1 = checkers.create_player("Alice", "white")
        player2 = checkers.create_player("Bob", "black")

        self.assertIsInstance(player1, Player)
        self.assertEqual(player1.name, "Alice")
        self.assertEqual(player1.color, "white")
        self.assertIsInstance(player2, Player)
        self.assertEqual(player2.name, "Bob")
        self.assertEqual(player2.color, "black")

    def test_game_winner(self):
        checkers = Checkers()
        winner = checkers.game_winner()
        self.assertIsNone(winner)

        # Black wins by eliminating all of white's checkers
        for row in range(8):
            for col in range(8):
                if isinstance(checkers.board[row][col], Checker) and checkers.board[row][col].color == "white":
                    checkers.board[row][col] = None
        checkers.print_board()
        winner = checkers.game_winner()
        self.assertEqual(winner, "black")

    def test_print_board(self):
        game = Checkers()
        game.print_board()

    def test_get_checker_details(self):
        game = Checkers()
        details = game.get_checker_details(0, 1)
        self.assertEqual(details["color"], "black")
        self.assertFalse(details["is_king"])
        details = game.get_checker_details(5, 0)
        self.assertEqual(details["color"], "white")
        self.assertFalse(details["is_king"])

    def test_player_methods(self):
        game = Checkers()
        player1 = game.create_player("Alice", "white")
        player2 = game.create_player("Bob", "black")
        self.assertEqual(player1.get_king_count(), 0)
        self.assertEqual(player1.get_triple_king_count(), 0)
        self.assertEqual(player1.get_captured_pieces_count(), 0)
        self.assertEqual(player2.get_king_count(), 0)
        self.assertEqual(player2.get_triple_king_count(), 0)
        self.assertEqual(player2.get_captured_pieces_count(), 0)


if __name__ == '__main__':
    unittest.main()
