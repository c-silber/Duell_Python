import random
import sys
from Board import Board
from Computer import Computer
from Die import Die
from File import File
from Tournament import Tournament


####################################################################
#   Game Class
####################################################################
class Game:
    def __init__(self):
        self.activePlayer = ""
        self.t = Tournament()

    def get_first_player(self):
        valid_spin = True
        while valid_spin:
            computer_val = random.randrange(1, 7)
            human_val = random.randrange(1, 7)
            print("Computer roll: " + str(computer_val) + " Human roll: " + str(human_val))
            if computer_val > human_val:
                valid_spin = False
                print("Computer goes first")
                self.activePlayer = "Computer"
            elif human_val > computer_val:
                valid_spin = False
                print("Human player goes first")
                self.activePlayer = "Human"
            else:
                valid_spin = True

    def begin_game(self, resume):
        # playing is set to true until the user no longer wants to play
        playing = True
        while playing:
            # create a new instance of the board
            b = Board()

            # if the user wanted to resume a previous game, restore the game state here
            if resume:
                f = File(b, self.t, "")
                f.read_from_file()
                self.activePlayer = f.get_next_player()
            else:
                self.get_first_player()

            # print the board
            b.print_board()
            self.play_game(b)

            # Once one player wins, update the tournament score and ask the user if they want to play another round
            self.t.set_winner(self.activePlayer)
            play_again = True
            while play_again:
                print(self.activePlayer + " won the round. Do you want to play again? y/n")
                new_round = input()
                if new_round == 'n' or new_round == 'N':
                    play_again = False
                    playing = False
                    print("Computer Score: " + str(self.t.get_computer_score()))
                    print("Human Score: " + str(self.t.get_human_score()))
                    if self.t.get_computer_score() > self.t.get_human_score():
                        print ("Computer has won the tournament")
                    elif self.t.get_computer_score() < self.t.get_human_score():
                        print ("You have won the tournament!")
                    else:
                        print("Tie Tournament!")
                elif new_round == 'Y' or new_round == 'y':
                    resume = False
                    play_again = False
                    playing = True

    def play_game(self, b):
        # winner is initially set to false
        winner = False
        # loop until there is a winner
        while not winner:
            self.suspend(b)
            # if the human player is active
            if self.activePlayer == "Human":
                valid = False
                while not valid:
                    self.suggestion(b)
                    print("Choose a die to move...")
                    print("    Row: ", end="")
                    source_row = int(input())
                    print ("    Column: ", end="")
                    source_column = int(input())
                    print("Choose the location to move to...")
                    print("    Row: ", end="")
                    dest_row = int(input())
                    print("    Column: ", end="")
                    dest_column = int(input())
                    if b.validate_move(source_row, source_column, dest_row, dest_column):
                        # if the move is valid, convert the source and destination
                        source_row = b.convert_coordinate("row", source_row)
                        source_column = b.convert_coordinate("column", source_column)
                        dest_row = b.convert_coordinate("row", dest_row)
                        dest_column = b.convert_coordinate("column", dest_column)
                        top_die = b.get_top(source_row, source_column)
                        right_die = b.get_right(source_row, source_column)
                        if b.check_moves(source_row, source_column, dest_row, dest_column, "H"):
                            d = Die(top_die, right_die, self.activePlayer)
                            if b.valid_direction(source_row, source_column, dest_row, dest_column) == 'b':
                                print("Do you want to move frontally or laterally? ")
                                d.roll_die(source_row, source_column, dest_row, dest_column, direction=input())
                                b.update_board(source_row, source_column, dest_row, dest_column, d.get_top(),
                                           d.get_right(), 'H')
                            else:
                                d.roll_die(source_row, source_column, dest_row, dest_column,
                                           b.valid_direction(source_row, source_column, dest_row, dest_column))
                                b.update_board(source_row, source_column, dest_row, dest_column, d.get_top(),
                                               d.get_right(), 'H')
                            b.print_board()
                            valid = True
                        else:
                            print ("Invalid move. Try again")
                if self.check_win(b):
                    winner = True
                else:
                    self.activePlayer = "Computer"
            # if the computer is active
            else:
                # Computer takes a turn
                c = Computer(b, "C")
                c.get_moves()
                b.print_board()
                # Check if winner and return
                if self.check_win(b):
                    winner = True
                else:
                    self.activePlayer = "Human"

    def suspend(self, board):
        print ("Would you like to suspend the game? y/n ", end="")
        suspend = input()
        if suspend == 'Y' or suspend == 'y':
            # Create an instance of the file class and write the existing board to the file
            f = File(board, self.t, self.activePlayer)
            f.write_to_file()
            sys.exit()
        elif suspend == 'N' or suspend == 'n':
            return
        else:
            suspend(board)

    def suggestion(self, board):
        print ("Would you like a suggestion? y/n ", end="")
        suggest = input()
        if suggest == 'Y' or suggest == 'y':
            h = Computer(board, "H")
            h.get_moves()
            return
        elif suggest == 'N' or suggest == 'n':
            return
        else:
            self.suggestion(board)

    def check_win(self, b):
        active = "H"
        if self.activePlayer == "Human":
            active = "C"

        for i in range(8):
            for j in range(9):
                if b.get_value(i, j) == active + str(11):
                    return False
        return True
