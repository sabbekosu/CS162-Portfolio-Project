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
        player1 = game.create_player("Alice", "White")
        self.assertIsInstance(player1, Player)
        self.assertEqual(player1.player_name, "Alice")
        self.assertEqual(player1.piece_color, "White")

    def test_create_player_invalid_color(self):
        game = Checkers()
        with self.assertRaises(ValueError):
            game.create_player("Alice", "InvalidColor")

    def test_play_game_out_of_turn(self):
        game = Checkers()
        player1 = game.create_player("Alice", "White")
        player2 = game.create_player("Bob", "Black")

        with self.assertRaises(OutofTurn):
            game.play_game("Bob", (5, 6), (4, 7))

    def test_play_game_invalid_player(self):
        game = Checkers()
        player1 = game.create_player("Alice", "White")

        with self.assertRaises(InvalidPlayer):
            game.play_game("InvalidPlayer", (2, 1), (3, 0))

    def test_play_game_invalid_move(self):
        game = Checkers()
        player1 = game.create_player("Alice", "White")

        with self.assertRaises(InvalidSquare):
            game.play_game("Alice", (2, 1), (4, 1))

    def test_get_checker_details(self):
        game = Checkers()
        player1 = game.create_player("Alice", "White")
        player2 = game.create_player("Bob", "Black")
        game.print_board()
        self.assertEqual(game.get_checker_details((1, 0)), "White")
        self.assertEqual(game.get_checker_details((0, 0)), None)
        self.assertEqual(game.get_checker_details((6, 5)), "Black")

    def test_get_checker_details_invalid_square(self):
        game = Checkers()

        with self.assertRaises(InvalidSquare):
            game.get_checker_details((8, 0))

    def test_game_winner(self):
        game = Checkers()
        player1 = game.create_player("Alice", "White")
        player2 = game.create_player("Bob", "Black")

        self.assertEqual(game.game_winner(), "Game has not ended")

    def test_white_piece_makes_a_regular_move_no_pieces_captured(self):
        player1 = self.game.create_player("Alice", "White")
        player2 = self.game.create_player("Bob", "Black")

        self.game.play_game("Alice", (1, 0), (0, 1))
        self.assertEqual(self.game.get_checker_details((1, 0)), None)
        self.assertEqual(self.game.get_checker_details((0, 1)), "White")

    def test_black_piece_makes_a_regular_move_no_pieces_captured(self):
        player1 = self.game.create_player("Alice", "White")
        player2 = self.game.create_player("Bob", "Black")

        # Move a white piece to allow black's turn
        self.game.play_game("Alice", (6, 1), (5, 0))  # Correct starting position for a white piece

        initial_black_piece = self.game.board[0][5]
        self.assertEqual("Black", initial_black_piece.color)

        # Move the black piece to an empty space
        self.game.play_game("Bob", (0, 5), (1, 4))

        # Check if the black piece has moved to the new position
        moved_black_piece = self.game.board[1][4]
        self.assertEqual("Black", moved_black_piece.color)

        # Check if the initial position is now empty
        empty_initial_position = self.game.board[0][5]
        self.assertIsNone(empty_initial_position)

    def test_white_captures(self):
        player1 = self.game.create_player("Alice", "White")
        player2 = self.game.create_player("Bob", "Black")

        # Move a white piece
        self.game.play_game("Alice", (1, 0), (0, 1))

        # Move a black piece
        self.game.play_game("Bob", (6, 1), (5, 0))

        # Move the white piece to capture the black piece
        self.game.play_game("Alice", (0, 1), (2, 3))
        self.assertEqual(self.game.get_checker_details((0, 1)), None)
        self.assertEqual(self.game.get_checker_details((1, 2)), None)
        self.assertEqual(self.game.get_checker_details((2, 3)), "White")


if __name__ == '__main__':
    unittest.main()
