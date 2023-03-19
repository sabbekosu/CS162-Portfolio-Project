# Author: Kevin Sabbe
# GitHub username: sabbekosu
# Date: 3/19/2023
# Description: A Checkers game playable by two players
class InvalidMoveError(Exception):
    """
    An exception to raise when an invalid move is attempted.

    Attributes:
    - message (str): A description of the error.
    - current_position (tuple): The (x, y) position of the checker being moved.
    - new_position (tuple): The (x, y) position the checker is being moved to.
    """


class GameOverError(Exception):
    """
    An exception to raise when the game is over.

    Attributes:
    - message (str): A description of the error.
    """


class Checker:
    def __init__(self, color):
        self.is_captured = None
        self.is_triple_king = None
        self.color = color
        self.is_king = False

    def __repr__(self):
        if self.is_captured:
            return "X"
        else:
            color_str = "W" \
                if self.color == "white" else "B"
            king_str = "K" \
                if self.is_king else ""
            triple_king_str = "3K" \
                if self.is_triple_king else ""
            return f"{color_str}{king_str}{triple_king_str}"


class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.checkers = []
        self.king_count = 0
        self.triple_king_count = 0
        self.captured_pieces_count = 0

    def get_king_count(self):
        return self.king_count

    def get_triple_king_count(self):
        return self.triple_king_count

    def get_captured_pieces_count(self):
        return self.captured_pieces_count


class Checkers:
    def __init__(self):
        self.board = [
            [None, Checker("black"), None, Checker("black"), None, Checker("black"), None, Checker("black")],
            [Checker("black"), None, Checker("black"), None, Checker("black"), None, Checker("black"), None],
            [None, Checker("black"), None, Checker("black"), None, Checker("black"), None, Checker("black")],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [Checker("white"), None, Checker("white"), None, Checker("white"), None, Checker("white"), None],
            [None, Checker("white"), None, Checker("white"), None, Checker("white"), None, Checker("white")],
            [Checker("white"), None, Checker("white"), None, Checker("white"), None, Checker("white"), None],
        ]
        self.players = {"white": None, "black": None}
        self.current_player = None

    def create_player(self, name, color):
        if color != "white" and color != "black":
            raise ValueError("Invalid player color")

        if self.players[color]:
            raise ValueError("Player color already taken")

        player = Player(name, color)
        self.players[color] = player

        return player

    def print_board(self):
        for row in self.board:
            print(row)

    def get_checker_details(self, row, col):
        checker = self.board[row][col]
        if not checker:
            return None

        return {"color": checker.color, "is_king": checker.is_king}

    def game_winner(self):
        white_checkers = 0
        black_checkers = 0

        for row in self.board:
            for checker in row:
                if checker and checker.color == "white":
                    white_checkers += 1
                elif checker and checker.color == "black":
                    black_checkers += 1

        if white_checkers == 0 and black_checkers > 0:
            return "black"
        elif black_checkers == 0 and white_checkers > 0:
            return "white"
        else:
            return None

    def is_valid_move(self, from_row, from_col, to_row, to_col):
        if not self.board[from_row][from_col]:
            return False

        if self.board[to_row][to_col]:
            return False

        if self.board[from_row][from_col].color == "white":
            if to_row >= from_row:
                return False
        else:
            if to_row <= from_row:
                return False

        row_diff = abs(from_row - to_row)
        col_diff = abs(from_col - to_col)

        if row_diff != col_diff:
            return False

        if row_diff == 1:
            return True

        mid_row = (from_row + to_row) // 2
        mid_col = (from_col + to_col) // 2

        if not self.board[mid_row][mid_col]:
            return False

        if self.board[mid_row][mid_col].color == self.board[from_row][from_col].color:
            return False

        return True
