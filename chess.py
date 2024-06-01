from abc import ABC, abstractmethod
import copy

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
        print(self.piece_type, end="")

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
        # Special handling of the case where pawn cannot capture peices that are in front
        if x_dist == 0 and matrix[move.final_pos[0]][move.final_pos[1]] != None:
            return False
        f1 = (x_dist == 0)
        if self.color == "W":
            # Simple one move upwards (basic pawn move)
            flag1 = f1
            flag1 &= (y_displacement == 1)
            # Initial 2 square upwards
            flag2 = f1
            if move.initial_pos[0] == 1:
                flag2 &= (y_displacement == 2)
            # Capture pieces present diagonally up.
            flag3 = (x_dist == 1) and (1 == y_displacement)
            counter_piece = matrix[move.final_pos[0]][move.final_pos[1]]
            if counter_piece == None:
                flag3 = False
            else:
                flag3 &= (counter_piece.color == "B")
            # No suuport for en passant right now.
            if flag1 or flag2 or flag3:
                return True
        if self.color == "B":
            # Simple one move downwards (basic pawn move)
            flag1 = f1
            flag1 &= (y_displacement == -1)
            # Initial 2 square downwards
            flag2 = f1
            if move.initial_pos[0] == 6:
                flag2 &= (y_displacement == -2)
            # Capture pieces present diagonally down.
            flag3 = (x_dist == 1) and (-1 == y_displacement)
            counter_piece = matrix[move.final_pos[0]][move.final_pos[1]]
            if counter_piece == None:
                flag3 = False
            else:
                flag3 &= (counter_piece.color == "W")
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
    def __king_check(self):
        # TODO 
        pass
    
    def __piece_in_path(self):
        # TODO
        pass

    def initialize_board(self):
        self.matrix = [
            [Rook("B"), Knight("B"), Bishop("B"), Queen("B"), King("B"), Bishop("B"), Knight("B"), Rook("B")],
            [Pawn("B"), Pawn("B")  , Pawn("B")  , Pawn("B") , Pawn("B"), Pawn("B")  , Pawn("B")  , Pawn("B")],
            [None     , None       , None       , None      , None     , None       , None       , None     ],
            [None     , None       , None       , None      , None     , None       , None       , None     ],
            [None     , None       , None       , None      , None     , None       , None       , None     ],
            [None     , None       , None       , None      , None     , None       , None       , None     ],
            [Pawn("W"), Pawn("W")  , Pawn("W")  , Pawn("W") , Pawn("W"), Pawn("W")  , Pawn("W")  , Pawn("W")],
            [Rook("W"), Knight("W"), Bishop("W"), Queen("W"), King("W"), Bishop("W"), Knight("W"), Rook("W")]
        ]

    def is_valid_move(self, move):
        ix, iy, fx, fy = move.initial_pos[0], move.initial_pos[1], move.final_pos[0], move.final_pos[1]
        ipiece, fpiece = matrix[ix][iy], matrix[fx][fy]
        # If piece is not present at the initial location
        if ipiece == None:
            return False
        # If it wrong colored piece
        if ipiece != self.to_move:
            return False
        # If same colored piece present at final location
        if fpiece != None and fpiece.color == self.to_move:
            return False
        # Check is overall piece movement is allowed in first place
        if not ipiece.allowed_move(move, self.matrix):
            return False
        # No other checks for Knight
        if ipiece.piece_type == "N":
            return True
        # Check there are any piece of any color in the path before final pos
        if self.__piece_in_path(move):
            return False
        # Check if the move causes check to king
        if self.__king_check(move):
            return False
        return True

    def make_move(self, move):
        ix, iy, fx, fy = move.initial_pos[0], move.initial_pos[1], move.final_pos[0], move.final_pos[1]
        ipiece, fpiece = matrix[ix][iy], matrix[fx][fy]
        fpiece = copy.deepcopy(ipiece)
        ipiece = None
        self.print_board()

    def check_state(self):
        # TODO
        pass

    def print_board(self):
        for i in range(0, 8):
            for j in range(0, 8):
                self.matrix.print_piece()
                print(", ")
            print("")

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
