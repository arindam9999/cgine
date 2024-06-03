import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


from chess import Board, Move
board = Board()

board.print_board()
moves = board.get_all_possible_moves()

import sys

# Open a file in write mode
file = open('tests/IT_logs/test_random_log.txt', 'w')

# Save the original stdout so we can restore it later
original_stdout = sys.stdout

# Redirect stdout to the file
sys.stdout = file 

board = Board()
for i in range(0, 8):
    board.matrix[1][i] = None

# TEST1: Basic printing all possible moves
moves = board.get_all_possible_moves()
for move in moves:
    move.print_move()
    tmp_board = Board()
    for i in range(0, 8):
        tmp_board.matrix[1][i] = None
    if not tmp_board.is_valid_move(move):
        continue
    tmp_board.make_move(move)
    tmp_board.print_board()

