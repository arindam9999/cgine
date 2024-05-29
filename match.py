from user import User
from game import Game

class Match:
    def new_game_prompt(self):
        break_flag, resp = False, ""
        while not break_flag :
            resp = input("Do u want to play a new game? (Y/N)\n")
            if resp not in ["Y", "N"]:
                print(f"Your response is {resp}, which is not valid please input a valid response.")
            else:
                break_flag = True
        return resp

    def match_stats_prompt(self):
        break_flag, resp = False, ""
        while not break_flag :
            resp = input("Do u want to see score?(Y/N)")
            if resp not in ["Y", "N"]:
                print(f"Your response is {resp}, which is not valid please input a valid response.")
            else:
                break_flag = True
        if resp == "Y":
            print(f"{self.users[0].name} score is {self.users[0].score}.")
            print(f"{self.users[1].name} score is {self.users[1].score}.")

    def closing_prompt(self):
        print("Byeee!")

    def play_new_match(self):
        resp = "Y"
        while True:
            if resp == "Y":
                resp = self.new_game_prompt()
                if resp == "Y":
                    game = Game(self.users)
                    game.play_new_game()
                    self.game_list.append(game)
                    
                    for user in self.users:
                        user.print_user()
                    self.match_stats_prompt()
            else:
                self.closing_prompt()
                break

    def __init__(self):
        user1 = User(input("Name of first user? "))
        user2 = User(input("Name of second user? "))
        self.users = [user1, user2]
        self.game_list = []