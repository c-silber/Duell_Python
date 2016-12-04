

####################################################################
#   Tournament Class
####################################################################
class Tournament:
    def __init__(self, computer_score = 0, human_score = 0):
        self.computer_score = int(computer_score)
        self.human_score = int(human_score)

    def get_human_score(self):
        return int(self.human_score)

    def get_computer_score(self):
        return int(self.computer_score)

    def set_human_score(self, human_score):
        self.human_score = human_score

    def set_computer_score(self, computer_score):
        self.computer_score = computer_score

    def set_winner(self, active_user):
        if active_user == "Human":
            score = int(self.human_score)
            self.set_human_score(score + 1)
        else:
            score = int(self.computer_score)
            self.set_computer_score(score + 1)
