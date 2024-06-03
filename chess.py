from abc import ABC, abstractmethod
import copy

class Move:
    def print_move(self):
        print(self.initial_pos, self.final_pos)
    
    def __init__(self, initial_pos, final_pos):
        self.initial_pos = [ord(initial_pos[0]) - ord("a"), ord(initial_pos[1]) - ord("1")]
        self.final_pos = [ord(final_pos[0]) - ord("a"), ord(final_pos[1]) - ord("1")] 

    

class Piece(ABC):
    @abstractmethod
    def set_piece_type(self):
        pass

    @abstractmethod
    def allowed_move(self):
        pass
    
    def get_candidate_moves(self, x, y, is_valid_matrix_location):
        """
        Gives all possible moves, with highest degrees of freedom
        """
        moves = []
        for i in range(1, self.__class__.RANGE_OF_MOTION + 1):
            for dx, dy in self.__class__.UNIT_VECTORS:
                X, Y = x + i * dx, y + i * dy 
                if not is_valid_matrix_location(X, Y):
                    continue 
                move = Move(Board.pos_array_2_string_converter(x, y), Board.pos_array_2_string_converter(X, Y))
                moves.append(move)
        return moves 
    
    def print_piece(self):
        print(f"{self.piece_type}({self.color})", end="")

    def __init__(self, color):
        self.color = color 
        self.is_pawn = False
        self.piece_type = "U"
        self.set_piece_type()


class King(Piece):
    # Static variables
    UNIT_VECTORS = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
    RANGE_OF_MOTION = 1

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
    # Static variables
    UNIT_VECTORS = [[1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
    RANGE_OF_MOTION = 7

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
    # Static variables
    UNIT_VECTORS = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-2, -1], [-1, -2], [1, -2], [2, -1]]
    RANGE_OF_MOTION = 1

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
    # Static variables
    UNIT_VECTORS = [[1, 1], [-1, 1], [-1, -1], [1, -1]]
    RANGE_OF_MOTION = 7

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
    # Static variables
    UNIT_VECTORS = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    RANGE_OF_MOTION = 7

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
    # Static variables
    UNIT_VECTORS = [[0, 1], [0, 2], [1, 1], [-1, 1]]
    RANGE_OF_MOTION = 1

    def allowed_move(self, move, matrix):
        if move.initial_pos == move.final_pos:
            return False
        x_dist, y_dist = [abs(move.final_pos[i] - move.initial_pos[i]) for i in range(0, 2)]
        min_dist, max_dist = min(x_dist, y_dist), max(x_dist, y_dist)
        y_displacement = move.final_pos[1] - move.initial_pos[1]
        # Special handling of the case where pawn cannot capture peices that are in front
        if x_dist == 0 and matrix[move.final_pos[1]][move.final_pos[0]] != None:
            return False
        f1 = (x_dist == 0)
        if self.color == "W":
            # Simple one move upwards (basic pawn move)
            flag1 = f1
            flag1 &= (y_displacement == 1)
            # Initial 2 square upwards
            flag2 = f1
            if move.initial_pos[1] == 1:
                flag2 &= (y_displacement == 2)
            else:
                flag2 = False
            # Capture pieces present diagonally up.
            flag3 = (x_dist == 1) and (1 == y_displacement)
            counter_piece = matrix[move.final_pos[1]][move.final_pos[0]]
            if counter_piece == None:
                flag3 = False
            else:
                flag3 &= (counter_piece.color == "B")
            # TODO: No suport for en passant right now.
            print(flag1, flag2, flag3, y_displacement,  y_displacement == 2, flag2 &)
            if flag1 or flag2 or flag3:
                return True
        if self.color == "B":
            # Simple one move downwards (basic pawn move)
            flag1 = f1
            flag1 &= (y_displacement == -1)
            # Initial 2 square downwards
            flag2 = f1
            if move.initial_pos[1] == 6:
                flag2 &= (y_displacement == -2)
            else:
                flag2 = False
            # Capture pieces present diagonally down.
            flag3 = (x_dist == 1) and (-1 == y_displacement)
            counter_piece = matrix[move.final_pos[1]][move.final_pos[0]]
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
    # Static variables
    COLUMN_LIST = ["a", "b", "c", "d", "e", "f", "g", "h"]
    ROW_LIST = ["1", "2", "3", "4", "5", "6", "7", "8"]
    PIECE_LIST = ["P", "R", "B", "K", "Q", "N"]
    COLOR_MAP = {
        0:"W",
        1:"B"
    }

    @staticmethod
    def pos_array_2_string_converter(x, y):
        return Board.COLUMN_LIST[x] + str(Board.ROW_LIST[y])

    def is_valid_matrix_location(self, X, Y):
        for val in [X, Y]:
            if val < 0 or val >= 8:
                return False 
        return True

    def __piece_in_path(self, move):
        """
        Creating the unit vector for the path and following it one step at a time to see if piece in path
        """
        ix, iy, fx, fy = move.initial_pos[0], move.initial_pos[1], move.final_pos[0], move.final_pos[1]
        dx, dy = (0 if (fx - ix) == 0 else abs(fx - ix)//(fx - ix)), (0 if (fy - iy) == 0 else abs(fy - ix)//(fy - iy))
        x, y = ix, iy 
        while x < fx or y < fy:
            x, y = x + dx, y + dy 
            if x == fx and y == fy:
                break
            if self.matrix[y][x] != None:
                return True
        return False

    def __is_check_from_knight(self):
        color, king_location, matrix = self.to_move, self.__iu_king_location, self.__iu_matrix
        dy = [1, 2, 2, 1, -1, -2, -2, -1]
        dx = [2, 1, -1, -2, -2, -1, 1, 2]
        x, y = king_location[color]
        for i in range(0, 8):
            X, Y = x + dx[i], y + dy[i] 
            # Case we X, Y not part of matrix
            if not self.is_valid_matrix_location(X, Y):
                continue 
            # Case where no piece in the current location
            if matrix[Y][X] == None:
                continue
            if (matrix[Y][X].piece_type == "N") and (matrix[Y][X].color != matrix[Y][X].color):
                return True 
        return False 
    
    def __is_row_column_diagonal_check(self):
        color, king_location, matrix = self.to_move, self.__iu_king_location, self.__iu_matrix
        x, y = king_location[color]
        # (alpha, beta) is the unit vector for the eight possible directions
        for alpha, beta in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
            dx = [i * alpha for i in range(1, 8)]
            dy = [i * beta for i in range(1, 8)]
            for i in range(0, 7):
                X, Y = x + dx[i], y + dy[i] 
                # Case we X, Y not part of matrix
                if not self.is_valid_matrix_location(Y, X):
                    continue 
                # Case where no piece in the current location
                if matrix[Y][X] == None:
                    continue
                # Path guarded by some piece
                if (matrix[Y][X].color == matrix[y][x].color):
                    break 
                # Case when Opp Pawn
                if matrix[Y][X].piece_type == "P":
                    if (alpha != 0 and beta == 1) and (dx[i] == alpha and dy[i] == beta):
                        return True 
                    else:
                        break
                # Case when Opp King
                if matrix[Y][X].piece_type == "K":
                    if dx[i] == alpha and dy[i] == beta:
                        return True
                    else:
                        break
                # Opposite colored Queen in open path
                if (matrix[Y][X].piece_type == "Q"):
                    return True 
                # Opposite colored Bishop in open path
                if matrix[Y][X].piece_type == "B":
                    if alpha != 0 and beta != 0:
                        return True 
                    else:
                        break
                # Opposite colored Rook in open path
                if matrix[Y][X].piece_type == "R":
                    if alpha == 0 or beta == 0:
                        return True
                    else:
                        break
        return False

    def __is_check_state(self):
        # Check if there is any check to the king in the current board state
        if self.__is_check_from_knight() or self.__is_row_column_diagonal_check():
            return True 
        return False
    
    def __king_check(self, move):
        self.make_move(move, False)
        return self.__is_check_state()

    def initialize_board(self):
        self.matrix = [
            [Rook("W"), Knight("W"), Bishop("W"), Queen("W"), King("W"), Bishop("W"), Knight("W"), Rook("W")],
            [Pawn("W"), Pawn("W")  , Pawn("W")  , Pawn("W") , Pawn("W"), Pawn("W")  , Pawn("W")  , Pawn("W")],
            [None     , None       , None       , None      , None     , None       , None       , None     ],
            [None     , None       , None       , None      , None     , None       , None       , None     ],
            [None     , None       , None       , None      , None     , None       , None       , None     ],
            [None     , None       , None       , None      , None     , None       , None       , None     ],
            [Pawn("B"), Pawn("B")  , Pawn("B")  , Pawn("B") , Pawn("B"), Pawn("B")  , Pawn("B")  , Pawn("B")],
            [Rook("B"), Knight("B"), Bishop("B"), Queen("B"), King("B"), Bishop("B"), Knight("B"), Rook("B")],
        ]

    def is_valid_move(self, move, external=True):
        ix, iy, fx, fy = move.initial_pos[0], move.initial_pos[1], move.final_pos[0], move.final_pos[1]
        ipiece, fpiece = self.matrix[iy][ix], self.matrix[fy][fx]
        # If piece is not present at the initial location
        if ipiece == None:
            if external:
                print(f"Error! Piece not present at the initial Location! {iy}, {ix}")
            self.print_board()
            return False
        # If it wrong colored piece
        if ipiece.color != self.__class__.COLOR_MAP[self.to_move]:
            if external:
                print(f"Error! trying to move the wrong colored piece! {ipiece.color}, {ipiece.piece_type}")
            return False
        # If same colored piece present at final location
        if fpiece != None and fpiece.color == self.__class__.COLOR_MAP[self.to_move]:
            if external:
                print(f"Error! Trying to capture same colored piece ({ipiece.color}, {ipiece.piece_type}), ({fpiece.color}, {fpiece.piece_type})")
            return False
        # Check is overall piece movement is allowed in first place
        if not ipiece.allowed_move(move, self.matrix):
            if external:
                print(f"Error! This piece does not move like that bro! ({ix}, {iy}), ({fx}, {fy}), ({ipiece.color}, {ipiece.piece_type})")
            return False
        # No other checks for Knight
        if ipiece.piece_type == "N":
            return True
        # Check there are any piece of any color in the path before final pos
        if self.__piece_in_path(move):
            if external:
                print("Error! There is a piece in the path")
            return False
        # Check if the move causes check to king
        if self.__king_check(move):
            if external:
                print("Error! Can't leave your king high and dry mate!")
            return False
        return True

    def make_move(self, move, actual_move=True):
        matrix = None 
        if not actual_move:
            self.__iu_matrix = copy.deepcopy(self.matrix)
            matrix = self.__iu_matrix
        else:
            matrix = self.matrix 
        ix, iy, fx, fy = move.initial_pos[0], move.initial_pos[1], move.final_pos[0], move.final_pos[1]
        ipiece = copy.deepcopy(matrix[iy][ix])
        matrix[fy][fx], matrix[iy][ix] = ipiece, None
        # TODO: Handle the case when pawn moves to the last rank, and pawn promotion
        if actual_move:
            # If king move then update king location
            if ipiece.piece_type == "K":
                self.king_location[self.to_move] = [fx, fy]
            # Update the color to move
            self.to_move = 1 - self.to_move
            # # Print the board status
            # self.print_board()
        else:
            self.__iu_king_location = copy.deepcopy(self.king_location)
            # If king move then update king location
            if ipiece.piece_type == "K":
                self.__iu_king_location[self.to_move] = [fx, fy]
    
    def get_all_possible_moves(self):
        """
        1. Need to get all the candidate moves for all pieces of that color
        2. Check among all those moves which ones are valid
        3. Return a list of all the valid moves
        """
        # TODO: Create function to get all possible moves 
        possible_move_list = []
        for y in range(0, 8):
            for x in range(0, 8):
                piece = self.matrix[y][x]
                if piece == None:
                    continue
                if piece.color != self.__class__.COLOR_MAP[self.to_move]:
                    continue 
                moves = piece.get_candidate_moves(x, y, self.is_valid_matrix_location)
                for move in moves: 
                    if self.is_valid_move(move, False):
                        possible_move_list.append(move)
        return possible_move_list

    def check_state(self):
        in_check = False 
        if self.__is_check_state():
            in_check = True
        all_possible_moves = self.get_all_possible_moves()
        if all_possible_moves == 0:
            if in_check:
                return "W"
            else:
                return "D"
        else:
            return "R"

    def print_board(self):
        print("\n------------------------------------------------")
        for i in range(7, -1, -1):
            print("| ", end="")
            for j in range(0, 8):
                if self.matrix[i][j] == None:
                    if (i + j)%2 == 0:
                        print("####| ", end="")
                    else:
                        print("    | ", end="")
                    continue
                self.matrix[i][j].print_piece()
                print("| ", end="")
            print("\n------------------------------------------------")

    def promote_to(self):
        # TODO
        pass

    def __init__(self):
        self.matrix = []
        self.to_move = 0
        self.king_location = [[4, 0], [4, 7]]

        self.__iu_king_location = [[4, 0], [4, 7]]
        self.__iu_matrix = []

        self.initialize_board()
