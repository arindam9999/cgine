import random

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
            print(f"{self.user1} score is {self.user1_score}.")
            print(f"{self.user2} score is {self.user2_score}.")

    def closing_prompt(self):
        print("Byeee!")

    def play_new_game(self):
        # TODO
        list1 = [1, 2, 3, 4, 5, 6]
        rand = random.choice(list1)
        if rand%2 == 0:
            self.user1_score += 1
        else:
            self.user2_score += 1

    def play_new_match(self):
        resp = "Y"
        while True:
            if resp == "Y":
                resp = self.new_game_prompt()
                if resp == "Y":
                    self.play_new_game()
                    self.match_stats_prompt()
            else:
                self.closing_prompt()
                break

    def __init__(self):
        self.user1 = input("Name of first user? ")
        self.user2 = input("Name of second user? ")
        self.user1_score = 0
        self.user2_score = 0
        self.match_list = []