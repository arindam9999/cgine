class User:

    def print_user(self):
        print(f"User 1, name: {self.name}, color: {self.color}, status: {self.status}, score: {self.score}.")

    def __init__(self, name):
        self.name = name
        self.color = []
        self.status = []
        self.score = 0