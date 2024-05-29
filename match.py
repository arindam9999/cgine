class Match:
    def new_game_prompt(self):
        break_flag, resp = False, ""
        while !break_flag :
            resp = input("Do u want to play a new game? (Y/N)\n")
            if resp is not in ["Y", "N"]:
                print(f"Your response is {resp}, which is not valid please input a valid response.")
            else:
                break_flag = True

    def match_stats_prompt(self):
        # TODO
        print("TODO")

    def closing_prompt(self):
        print("Byeee!")

    def play_new_game()

    def __init__(self, name, age):
        self.user1 = input("Name of first user? ")
        self.user2 = input("Name of second user? ")
        self.user1_score = 0
        self.user2_score = 0
        self.match_list = []

        self.new_game_prompt()

        if resp == "Y":
            self.play_new_game()
            self.match_stats_prompt()
            self.new_game_prompt()
        else:
            self.closing_prompt()
            