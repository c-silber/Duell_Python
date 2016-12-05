from Die import Die


####################################################################
#   Game Class
####################################################################
class Computer:
    def __init__(self, board, active_player):
        self.activePlayer = active_player
        self.board = board
        self.status = 4
        self.move = [0, 0, 0, 0]

    def get_moves(self):
        opponent = "H" if self.activePlayer == "C" else "C"

        # iterate through the board
        for i in range(8):
            for j in range(9):
                # if it's one of the active players pieces, get all the possible moves
                valid_moves = self.board.get_moves(i, j, opponent)
                self.evaluate_move(i, j, valid_moves)
                valid_moves = self.board.get_moves(i, j, self.activePlayer)
                self.evaluate_move(i, j, valid_moves)

        self.make_move()

    def evaluate_move(self, row, column, valid_moves):
        opponent = "H"
        if self.activePlayer == "H":
            opponent = "C"

        # iterate through the board
        for i in range(8):
            for j in range(9):
                # if the move for this piece was valid... check what we can do
                if valid_moves[i][j]:
                    # if we can win the game, WIN!
                    if self.board.get_value(i, j) == opponent + "11" and  str(self.board.get_value(row, column))[0] == self.activePlayer:
                        self.status = 0
                        self.move = [row, column, i, j]
                    # if key piece of active user is in danger of capture, move it
                    elif self.status > 1 and (self.board.get_value(i, j) == self.activePlayer + "11") \
                            and (str(self.board.get_value(row, column))[0] == opponent):
                        if self.board.check_dest(i + 1, j):
                            self.status = 1
                            self.move = [i, j, i + 1, j]
                        elif self.board.check_dest(i - 1, j):
                            self.status = 1
                            self.move = [i, j, i-1, j]
                        elif self.board.check_dest(i, j+1):
                            self.status = 1
                            self.move = [i, j, i, j+1]
                        elif self.board.check_dest(i, j-1):
                            self.status = 1
                            self.move = [i, j, i, j-1]
                    # if we can capture any of the opponents pieces, let's do that
                    elif self.status > 2 and str(self.board.get_value(i, j)) != "0" and \
                                    str(self.board.get_value(i, j))[0] != self.activePlayer:
                        self.status = 2
                        self.move = [row, column, i, j]
                    elif self.status > 3 and str(self.board.get_value(row, column))[0] == self.activePlayer:
                        self.status = 3
                        self.move = [row, column, i, j]

    def make_move(self):
        # if the active player is the computer, make the move!
        source_row = self.move[0]
        source_column = self.move[1]
        dest_row = self.move[2]
        dest_column = self.move[3]

        message = "moved the "
        if self.activePlayer == "H":
            message = "recommends moving the"

        direction = " laterally"
        if self.activePlayer == "C":
            top_die = str(self.board.get_value(source_row, source_column))[1]
            right_die = str(self.board.get_value(source_row, source_column))[2]
            d = Die(top_die, right_die, self.activePlayer)
            if self.board.valid_direction(source_row, source_column, dest_row, dest_column) == 'l':
                d.roll_die(source_row, source_column, dest_row, dest_column, 'l')
            else:
                direction = " frontally"
                d.roll_die(source_row, source_column, dest_row, dest_column, 'f')
            self.board.update_board(source_row, source_column, dest_row, dest_column, d.get_top(),
                                    d.get_right(), 'C')

        if (source_row == dest_row or source_column == dest_column):
            direction = ""

        source_row = self.convert_coordinate("row", source_row)
        source_column = self.convert_coordinate("column", source_column)
        dest_row = self.convert_coordinate("row", dest_row)
        dest_column = self.convert_coordinate("column", dest_column)

        if self.status == 0:
            print ("Computer " + message + " piece at " + str(source_row) + "," +
                   str(source_column) + direction + " to " + str(dest_row) + "," + str(dest_column) +
                   " to capture the key piece and win the game")
        elif self.status == 1:
            print ("Computer " + message + " piece at "+ str(source_row) + "," +
                   str(source_column) + direction + " to " + str(dest_row) + "," + str(dest_column) +
                   " to avoid capture of key die")
        elif self.status == 2:
            print ("Computer " + message + " piece at "+ str(source_row) + "," +
                   str(source_column) + direction + " to " + str(dest_row) + "," + str(dest_column) +
                   " to capture an opponents piece")
        elif self.status == 3:
            print ("Computer " + message + " piece at "+ str(source_row) + "," +
                   str(source_column) + direction + " to " + str(dest_row) + "," + str(dest_column))

    @staticmethod
    def convert_coordinate(type, value):
        if type == "row":
            if value == 7:
                return 1
            if value == 6:
                return 2
            if value == 5:
                return 3
            if value == 4:
                return 4
            if value == 3:
                return 5
            if value == 2:
                return 6
            if value == 1:
                return 7
            if value == 0:
                return 8
        else:
            return value + 1



