from abc import ABC, abstractmethod

class Move:
    def __init__(self, initial_pos, final_pos):
        self.initial_pos = [ord(initial_pos[0]) - ord("a"), ord(initial_pos[1]) - ord("1")]
        self.final_pos = [ord(final_pos[0]) - ord("a"), ord(final_pos[1]) - ord("1")] 
    

class Piece(ABC):
    @abstractmethod
    def set_piece_type(self):
        pass

    def allowed_move(self):
        pass
    
    def print_piece(self):
        print(self.piece_type)

    def __init__(self, color):
        self.color = color 
        self.is_pawn = False
        self.piece_type = "U"
        self.set_piece_type()


class King(Piece):
    def allowed_move(self, move, matrix):
        if move.initial_pos == move.final_pos:
            return False
        x_dist, y_dist = [abs(move.final_pos[i] - move.initial_pos[i]) for i in range(0, 2)]
        min_dist, max_dist = min(x_dist, y_dist), max(x_dist, y_dist)
        if min_dist <= 1 and max_dist <= 1:
            return True 
        else:
            return False

    def set_piece_type(self):
        self.piece_type = "K"


class Queen(Piece):
    def allowed_move(self, move, matrix):
        if move.initial_pos == move.final_pos:
            return False
        x_dist, y_dist = [abs(move.final_pos[i] - move.initial_pos[i]) for i in range(0, 2)]
        min_dist, max_dist = min(x_dist, y_dist), max(x_dist, y_dist)
        if (min_dist == 0) or (min_dist == max_dist):
            return True 
        else:
            return False

    def set_piece_type(self):
        self.piece_type = "Q"


class Knight(Piece):
    def allowed_move(self, move, matrix):
        if move.initial_pos == move.final_pos:
            return False
        x_dist, y_dist = [abs(move.final_pos[i] - move.initial_pos[i]) for i in range(0, 2)]
        min_dist, max_dist = min(x_dist, y_dist), max(x_dist, y_dist)
        if min_dist == 1 and max_dist == 2:
            return True 
        else:
            return False

    def set_piece_type(self):
        self.piece_type = "N"


class Bishop(Piece):
    def allowed_move(self, move, matrix):
        if move.initial_pos == move.final_pos:
            return False
        x_dist, y_dist = [abs(move.final_pos[i] - move.initial_pos[i]) for i in range(0, 2)]
        min_dist, max_dist = min(x_dist, y_dist), max(x_dist, y_dist)
        if min_dist == max_dist:
            return True 
        else:
            return False

    def set_piece_type(self):
        self.piece_type = "B"


class Rook(Piece):
    def allowed_move(self, move, matrix):
        if move.initial_pos == move.final_pos:
            return False
        x_dist, y_dist = [abs(move.final_pos[i] - move.initial_pos[i]) for i in range(0, 2)]
        min_dist, max_dist = min(x_dist, y_dist), max(x_dist, y_dist)
        if (min_dist == 0):
            return True 
        else:
            return False

    def set_piece_type(self):
        self.piece_type = "R"


class Pawn(Piece):
    def allowed_move(self, move, matrix):
        if move.initial_pos == move.final_pos:
            return False
        x_dist, y_dist = [abs(move.final_pos[i] - move.initial_pos[i]) for i in range(0, 2)]
        min_dist, max_dist = min(x_dist, y_dist), max(x_dist, y_dist)
        y_displacement = move.final_pos[1] - move.initial_pos[1]
        f1 = (x_dist == 0)
        if self.color == "W":
            # Simple one move upwards (basic pawn move)
            flag1 &= (y_displacement == 1)
            # Initial 2 square upwards
            flag2 = f1
            if move.initial_pos[0] == 1 and self.color == "W":
                flag2 &= (y_displacement == 2)
            # Capture pieces present diagonally up.
            counter_piece = matrix[move.final_pos[0]][move.final_pos[1]]
            flag3 = (counter_piece.color == "B") and (x_dist == 1) and (1 == y_displacement)
            # No suuport for en passant right now.
            if flag1 or flag2 or flag3:
                return True
        if self.color == "B":
            # Simple one move downwards (basic pawn move)
            flag1 &= (y_displacement == -1)
            # Initial 2 square downwards
            flag2 = f1
            if move.initial_pos[0] == 6 and self.color == "W":
                flag2 &= (y_displacement == -2)
            # Capture pieces present diagonally down.
            counter_piece = matrix[move.final_pos[0]][move.final_pos[1]]
            flag3 = (counter_piece.color == "W") and (x_dist == 1) and (-1 == y_displacement)
            # No support for en passant right now.
            if flag1 or flag2 or flag3:
                return True
        return False

    def set_piece_type(self):
        self.piece_type = "P"

    def __init__(self, color):
        super().__init__(color)
        self.is_pawn = True





class Board:
    def initialize_board(self):
        # TODO
        pass

    def is_valid_move(self, move):
        # TODO
        pass

    def make_move(self, move):
        # TODO
        pass

    def check_state(self):
        # TODO
        pass

    def print_board(self):
        # TODO
        pass

    def promote_to(self):
        # TODO
        pass

    def __init__(self):
        self.column_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
        self.row_list = ["1", "2", "3", "4", "5", "6", "7", "8"]
        self.piece_list = ["P", "R", "B", "K", "Q", "K"]

        self.matrix = []
        self.to_move = "W"
        self.king_location = [[4, 0], [4, 7]]

        self.initialize_board()
