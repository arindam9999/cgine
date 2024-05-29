import random

from move import Move
from board import Board

class Game:
    def random_gen(self):
        list1 = [1, 2, 3, 4, 5, 6]
        rand = random.choice(list1)
        return rand%2

    def validate_piece(self, piece):
        return piece in self.piece_list:
    
    def validate_pos(self, pos):
        return (pos[0] in self.column_list) and (pos[1] in self.row_list)
    
    def get_move_prompt(self):
        move = None
        while True:
            piece, initial_pos, final_pos = input(f"{self.users[self.to_play].name} your move:").split(" ")
            f1, f2, f3 = self.validate_piece(piece), self.validate_pos(initial_pos), self.validate_pos(final_pos)
            if f1 & f2 & f3:
                move = Move(f2, f3)
                if self.board.is_valid_move(move):
                    return move
                else:
                    print("Not a possible move! Please retry!")
            else:
                if f1 == 0:
                    print(f"Your piece {piece} is incorrect", end="")
                if f2 == 0:
                    print(", Your initial pos {initial_pos} is incorrect", end="")
                if f3 == 0:
                    print(", Your final pos {final_pos} is incorrect", end="")
                print("Please retry!")

    def play_new_game(self):
        flag = self.random_gen()
        while True:
            move = self.get_move_prompt()
            self.board.make_move(move)
            self.moves.append(move)
            state = board.check_state()
            if state in ["W", "L", "D"]:
                self.users[self.to_play].score += self.state_2_score[state]
                self.users[self.to_play].status[-1] = state
                self.users[1 - self.to_play].status[-1] = self.complimentry_state[state]
                break 
            self.to_play = 1 - self.to_play

    def choose_color_prompt(self):
        flag = self.random_gen()
        self.users[flag].color[-1] = "W"
        self.users[1 - flag].color[-1] = "B"
        self.to_play = flag

    def __init__(self, users):
        self.state_2_score = {
            "W":1,
            "L":0,
            "D":0.5
        }
        self.complimentry_state = {
            "W":"L",
            "L":"W",
            "D":"D"
        }
        self.piece_list = ["P", "R", "B", "K", "Q", "K"]
        self.column_list = ["a", "b", "c", "d", "e", "f", "g", "h"]
        self.row_list = ["1", "2", "3", "4", "5", "6", "7", "8"]
        
        self.users = users
        for user in self.users:
            user.color.append("U")
            user.status.append("U")
        self.choose_color_prompt()

        self.board = []
        self.moves = []
        self.to_play = 0
