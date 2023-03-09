# Author: Kevin Sabbe
# GitHub username: sabbekosu
# Date: 3/8/2023
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
    """
    A class to represent a checker piece on the board.

    Responsibilities:
    - Store information about the piece, including its color and position.
    - Be able to move the piece.
    - Determine if the piece is eligible for promotion to king or triple king.

    Communicates with:
    - Board: to determine if a move is valid and to update its position on the board.
    """

    def __init__(self, color, position):
        """
        Initialize the Checker object.

        Parameters:
        - color (str): the color of the checker, either "black" or "white".
        - position (tuple): the (x, y) position of the checker on the board.
        """
        pass

    def move(self, new_position):
        """
        Move the checker to a new position.

        Parameters:
        - new_position (tuple): the (x, y) position to move the checker to.
        """
        pass

    def is_eligible_for_promotion(self):
        """
        Check if the checker is eligible for promotion to king or triple king.

        Returns:
        - bool: True if the checker is eligible for promotion, False otherwise.
        """
        pass


class Board:
    """
    A class to represent the game board.

    Responsibilities:
    - Store information about the pieces on the board.
    - Determine if a move is valid.
    - Update the board after a move.
    - Print the board.

    Communicates with:
    - Checker: to determine if a move is valid and to update the positions of the checkers.
    """

    def __init__(self):
        """
        Initialize the Board object.
        """
        pass

    def is_valid_move(self, current_position, new_position):
        """
        Check if a move is valid.

        Parameters:
        - current_position (tuple): the (x, y) position of the checker to move.
        - new_position (tuple): the (x, y) position to move the checker to.

        Returns:
        - bool: True if the move is valid, False otherwise.
        """
        pass

    def update_board(self, current_position, new_position):
        """
        Update the board after a move.

        Parameters:
        - current_position (tuple): the (x, y) position of the checker to move.
        - new_position (tuple): the (x, y) position to move the checker to.
        """
        pass

    def print_board(self):
        """
        Print the current state of the board.
        """
        pass


class Player:
    """
    A class to represent a player in the game.

    Responsibilities:
    - Store information about the player, including their name and color.
    - Create checkers for the player.
    - Determine the next move.

    Communicates with:
    - Checker: to create checkers for the player.
    - Board: to determine if a move is valid.
    """

    def __init__(self, name, color):
        """
        Initialize the Player object.

        Parameters:
        - name (str): the name of the player.
        - color (str): the color of the player's checkers, either "black" or "white".
        """
        pass

    def create_checkers(self):
        """
        Create checkers for the player.
        """
        pass

    def get_next_move(self, board):
        """
        Determine the next move for the player.

        Parameters:
        - board (Board): the current state of the board.

        Returns:
        - tuple: the (current_position, new_position) tuple representing the move to
        """
