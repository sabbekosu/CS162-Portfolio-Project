# Author: Kevin Sabbe
# GitHub username: sabbekosu
# Date: 3/19/2023
# Description: A Checkers game playable by two players
class OutofTurn(Exception):
    pass


class InvalidSquare(Exception):
    pass


class InvalidPlayer(Exception):
    pass


class Checker:
    def __init__(self, color, rank="regular"):
        self.color = color
        self.rank = rank

    def __str__(self):
        if self.rank == "regular":
            return self.color
        else:
            return f"{self.color}_{self.rank}"

    def __repr__(self):
        return str(self)

    def is_king(self):
        return self.rank == "king"

    def is_triple_king(self):
        return self.rank == "triple_king"


class Player:
    def __init__(self, player_name, piece_color):
        self.player_name = player_name
        self.piece_color = piece_color
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
        self.board = self._init_board()
        self.players = []
        self.turn = "White"
        self.current_player = None

    def _init_board(self):
        board = [[None] * 8 for _ in range(8)]

        for x in range(8):
            for y in range(8):
                if (x + y) % 2 == 1:
                    if y < 3:
                        board[x][y] = Checker("White")
                    elif y > 4:
                        board[x][y] = Checker("Black")

        return board

    def create_player(self, player_name, piece_color):
        if piece_color not in ["Black", "White"]:
            raise ValueError("Invalid piece_color. Must be 'Black' or 'White'.")

        player = Player(player_name, piece_color)
        self.players.append(player)
        if not self.current_player:
            self.current_player = player
        return player

    def _switch_current_player(self):
        if self.current_player == self.players[0]:
            self.current_player = self.players[1]
        else:
            self.current_player = self.players[0]

    def _is_valid_move(self, start, end, checker):
        start_x, start_y = start
        end_x, end_y = end
        dx = end_x - start_x
        dy = end_y - start_y

        if checker.color == "White":
            direction = 1
        else:
            direction = -1

        if checker.is_king or checker.is_triple_king:
            if abs(dx) != abs(dy) or dx * direction < 0:
                return False
        else:
            if dx != direction or abs(dy) != 1:
                return False

        if self.board[end_x][end_y]:
            return False

        return True

    def play_game(self, player_name, start, end):
        # Find the player
        player = None
        for p in self.players:
            if p.player_name == player_name:
                player = p
                break

        if not player:
            raise InvalidPlayer(f"Invalid player: {player_name}")

        # Check if it's the player's turn
        if player.piece_color != self.turn:
            raise OutofTurn("It is not this player's turn.")

        # Move the piece and get the number of captured pieces
        captured_pieces = self._move_piece(player.piece_color, start, end)

        # Update the player's captured_pieces_count
        player.captured_pieces_count += captured_pieces

        # Switch the turn to the other player
        self.turn = "Black" if self.turn == "White" else "White"

        return captured_pieces

    def get_checker_details(self, square_location):
        x, y = square_location
        if x < 0 or x >= 8 or y < 0 or y >= 8:
            raise InvalidSquare("Invalid square location.")

        checker = self.board[x][y]
        return None if not checker else checker.__repr__()

    def print_board(self):
        for row in self.board:
            print(row)

    def _move_piece(self, piece_color, start, end):
        start_x, start_y = start
        end_x, end_y = end
        dx, dy = end_x - start_x, end_y - start_y

        # Check if the starting square is valid
        if not (0 <= start_x < 8 and 0 <= start_y < 8):
            raise InvalidSquare(f"Invalid starting square: {start}")

        # Check if the destination square is valid
        if not (0 <= end_x < 8 and 0 <= end_y < 8):
            raise InvalidSquare(f"Invalid destination square: {end}")

        start_piece = self.board[start_x][start_y]
        end_piece = self.board[end_x][end_y]

        # Check if the piece in the starting square belongs to the player
        if not start_piece or start_piece.color != piece_color:
            raise InvalidSquare(f"Invalid starting square: {start}")

        # Check if the destination square is empty
        if end_piece is not None:
            raise InvalidSquare(f"Invalid destination square: {end}")

        captured_pieces = 0
        # Calculate the absolute difference between the starting and destination squares
        abs_dx, abs_dy = abs(dx), abs(dy)

        is_king_or_triple_king = start_piece.rank in {"king", "triple_king"}

        if is_king_or_triple_king or (abs_dx == 1 and abs_dy == 1):
            # Regular move
            self.board[end_x][end_y] = self.board[start_x][start_y]
            self.board[start_x][start_y] = None
        elif abs_dx == 2 and abs_dy == 2:
            # Capture move
            middle_x, middle_y = (start_x + end_x) // 2, (start_y + end_y) // 2
            middle_piece = self.board[middle_x][middle_y]
            if middle_piece and middle_piece.color != piece_color:
                self.board[end_x][end_y] = self.board[start_x][start_y]
                self.board[start_x][start_y] = None
                self.board[middle_x][middle_y] = None
                captured_pieces = 1
            else:
                raise InvalidSquare(f"Invalid move: {start} to {end}")
        elif is_king_or_triple_king and abs_dx == abs_dy:
            # Diagonal move for a king or triple king
            step_x, step_y = dx // abs_dx, dy // abs_dy
            current_x, current_y = start_x + step_x, start_y + step_y
            while current_x != end_x and current_y != end_y:
                current_piece = self.board[current_x][current_y]
                if current_piece:
                    if current_piece.color == piece_color:
                        raise InvalidSquare(f"Invalid move: {start} to {end}")
                    elif not captured_pieces:
                        captured_pieces = 1
                    else:
                        raise InvalidSquare(f"Invalid move: {start} to {end}")
                current_x += step_x
                current_y += step_y

            if captured_pieces:
                self.board[end_x][end_y] = self.board[start_x][start_y]
                self.board[start_x][start_y] = None
                self.board[current_x - step_x][current_y - step_y] = None
            else:
                raise InvalidSquare(f"Invalid move: {start} to {end}")
        else:
            raise InvalidSquare(f"Invalid move: {start} to {end}")

            # Update the piece rank if it reaches the opponent's side or returns to its original side
        if end_piece.rank != "triple_king":
            if piece_color == "White" and end_y == 7:
                end_piece.rank = "king"
            elif piece_color == "Black" and end_y == 0:
                end_piece.rank = "king"
            elif end_piece.rank == "king" and (
                    (piece_color == "White" and end_y == 0) or (piece_color == "Black" and end_y == 7)):
                end_piece.rank = "triple_king"

        return captured_pieces

    def _has_valid_moves(self, player_color):
        for start_x in range(8):
            for start_y in range(8):
                checker = self.board[start_x][start_y]
                if checker and checker.color == player_color:
                    for dx in [-1, 1]:
                        for dy in [-1, 1]:
                            end_x = start_x + dx
                            end_y = start_y + dy
                            if 0 <= end_x < 8 and 0 <= end_y < 8:
                                if self._is_valid_move((start_x, start_y), (end_x, end_y), checker):
                                    return True
        return False

    def game_winner(self):
        white_checkers_count = 0
        black_checkers_count = 0
        white_has_moves = False
        black_has_moves = False

        for row in self.board:
            for checker in row:
                if checker:
                    if checker.color == "White":
                        white_checkers_count += 1
                        if not white_has_moves:
                            white_has_moves = self._has_valid_moves(checker.color)
                    else:
                        black_checkers_count += 1
                        if not black_has_moves:
                            black_has_moves = self._has_valid_moves(checker.color)

        if white_checkers_count == 0 or (white_checkers_count > 0 and not white_has_moves):
            return self.players[1].player_name
        elif black_checkers_count == 0 or (black_checkers_count > 0 and not black_has_moves):
            return self.players[0].player_name
        else:
            return "Game has not ended"
