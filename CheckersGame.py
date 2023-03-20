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
    def __init__(self, color, is_king=False, is_triple_king=False):
        self.color = color
        self.is_king = is_king
        self.is_triple_king = is_triple_king

    def __repr__(self):
        if self.is_triple_king:
            return f"{self.color}_Triple_King"
        elif self.is_king:
            return f"{self.color}_king"
        else:
            return self.color


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

    def play_game(self, player_name, starting_square_location, destination_square_location):
        player = next((p for p in self.players if p.player_name == player_name), None)
        if not player:
            raise InvalidPlayer("Invalid player_name.")

        if player != self.current_player:
            raise OutofTurn("It is not this player's turn.")

        start_x, start_y = starting_square_location
        end_x, end_y = destination_square_location
        checker = self.board[start_x][start_y]

        if not checker or checker.color != player.piece_color:
            raise InvalidSquare("Invalid starting square location.")

        if not self._is_valid_move(starting_square_location, destination_square_location, checker):
            raise InvalidSquare("Invalid destination square location.")

        self.board[end_x][end_y] = self.board[start_x][start_y]
        self.board[start_x][start_y] = None

        if (checker.color == "White" and end_x == 7) or (checker.color == "Black" and end_x == 0):
            if checker.is_king:
                checker.is_triple_king = True
            else:
                checker.is_king = True

        self._switch_current_player()

    def get_checker_details(self, square_location):
        x, y = square_location
        if x < 0 or x >= 8 or y < 0 or y >= 8:
            raise InvalidSquare("Invalid square location.")

        checker = self.board[x][y]
        return None if not checker else checker.__repr__()

    def print_board(self):
        for row in self.board:
            print(row)

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
