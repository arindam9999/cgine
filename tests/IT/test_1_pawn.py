import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))


from chess import Board, Move
board = Board()

board.print_board()
moves = board.get_all_possible_moves()

import sys

# Open a file in write mode
file = open('tests/IT_logs/test_1_pawn_log.txt', 'w')

# Save the original stdout so we can restore it later
original_stdout = sys.stdout

# Redirect stdout to the file
sys.stdout = file 


"""
Test that all pawn moves are working fine
1. Testing if moves are correct at the initial state
"""

# 1. Testing if moves are correct at the initial state
correct_valid_moves = [
    "P a2 a3", "P a2 a4",
    "P b2 b3", "P b2 b4",
    "P c2 c3", "P c2 c4",
    "P d2 d3", "P d2 d4",
    "P e2 e3", "P e2 e4",
    "P f2 f3", "P f2 f4",
    "P g2 g3", "P g2 g4",
    "P h2 h3", "P h2 h4",
]

test_output_valid_moves = []
for i in range(0, 8):
    matrix = [[0 for _ in range(0, 8)] for _ in range(0, 8)]
    for j in range(0, 8):
        tmp = []
        for k in range(0, 8):
            initial_pos = Board.pos_array_2_string_converter(i, 1)
            final_pos = Board.pos_array_2_string_converter(j, k)
            move_str = "P " + initial_pos + " " + final_pos
            move = Move(initial_pos, final_pos)
            board = Board()
            if not board.is_valid_move(move, False):
                continue 
            board.make_move(move)
            print(move_str)
            board.print_board()
            test_output_valid_moves.append(move_str)

if correct_valid_moves == test_output_valid_moves:
    print("SUCCESS!! TEST IN WORKING FINE!", correct_valid_moves, test_output_valid_moves, sep="\n")
else:
    print("ERROR!! TEST FAILED!", correct_valid_moves, test_output_valid_moves, sep="\n")
