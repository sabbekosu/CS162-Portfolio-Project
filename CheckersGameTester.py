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

    def test_invalid_player(self):
        # Try to move with an invalid player name
        with self.assertRaises(InvalidPlayer):
            self.game.play_game("Kevin", (2, 1), (3, 2))

    def test_out_of_turn(self):
        # Create two players
        player1 = self.game.create_player("Alice", "White")
        player2 = self.game.create_player("Bob", "Black")

        # Move a white piece, which is not allowed because it is Black's turn
        with self.assertRaises(OutofTurn):
            self.game.play_game("Alice", (2, 1), (3, 2))

    def test_invalid_square(self):
        # Create two players
        player1 = self.game.create_player("Alice", "White")
        player2 = self.game.create_player("Bob", "Black")

        # Try to move a white piece to an invalid square
        with self.assertRaises(InvalidSquare):
            self.game.play_game("Alice", (2, 1), (9, 2))

        # Try to move a black piece to an invalid square
        with self.assertRaises(InvalidSquare):
            self.game.play_game("Bob", (7, 0), (8, 0))

    def test_king_piece_moves_two_squares_diagonal(self):
        # Create two players
        player1 = self.game.create_player("Alice", "White")
        player2 = self.game.create_player("Bob", "Black")

        # Move a white king piece two squares diagonally
        self.game.play_game("Alice", (5, 0), (3, 2))

        # Check if the white king piece has moved to the new position
        moved_white_king = self.game.board[3][2]
        self.assertEqual("White_king", moved_white_king.__str__())

        # Check if the initial position is now empty
        empty_initial_position = self.game.board[5][0]
        self.assertIsNone(empty_initial_position)

    def test_create_player_invalid_piece_color(self):
        game = Checkers()
        with self.assertRaises(ValueError):
            game.create_player("Alice", "Red")

    def test_move_piece_invalid_start_square(self):
        player1 = self.game.create_player("Alice", "White")
        player2 = self.game.create_player("Bob", "Black")

        with self.assertRaises(InvalidSquare):
            self.game.play_game("Bob", (8, 0), (6, 2))

if __name__ == '__main__':
    unittest.main()