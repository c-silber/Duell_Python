import re


####################################################################
#   File Class
####################################################################
class File:
    def __init__(self, board, tournament, next_player):
        self.board = board
        self.tournament = tournament
        self.comp_score = tournament.get_computer_score()
        self.human_score = tournament.get_human_score()
        self.next_player = "Human"
        if next_player == "Computer":
            self.next_player = "Computer"

    def write_to_file(self):
        print ("Please enter the name of the file to save to: ")
        f = open(input(), 'w')
        f.write("Board:\n")
        for i in range(8):
            for j in range(9):
                f.write(str(self.board.get_value(i, j)))
                f.write(" ")
            f.write("\n")
        f.write("\n")
        f.write("Computer Wins: " + str(self.comp_score))
        f.write("\n\n")
        f.write("Human Wins: " + str(self.human_score))
        f.write("\n\n")
        f.write("Next Player: " + str(self.next_player))

    def read_from_file(self):
        file_name = True
        while file_name:
            try:
                print("Please enter the file name: ")
                f = open(input(), 'r')
                file_name = False
                f.readline()

                count = 0
                for line in range(8):
                    new = re.findall(r'\S+', f.readline())
                    for i in range(9):
                        self.board.set_value(count, i, new[i])
                    count += 1

                f.readline()
                self.tournament.set_computer_score(f.readline()[15])
                f.readline()
                self.tournament.set_human_score(f.readline()[12])
                f.readline()
                active_player = f.readline()[13]
                if active_player == "C":
                    self.next_player = "Computer"
                else:
                    self.next_player = "Human"
            except FileNotFoundError:
                print("File not found. Try again")

    def get_next_player(self):
        return self.next_player
