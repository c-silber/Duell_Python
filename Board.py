

####################################################################
#   Board Class
####################################################################
class Board:
    def __init__(self):
        self.table = [[0 for i in range(9)] for j in range(8)]
        # computer dice
        self.table[0][0] = "C56"
        self.table[0][1] = "C15"
        self.table[0][2] = "C21"
        self.table[0][3] = "C62"
        self.table[0][4] = "C11"
        self.table[0][5] = "C62"
        self.table[0][6] = "C21"
        self.table[0][7] = "C15"
        self.table[0][8] = "C56"

        # human dice
        self.table[7][0] = "H56"
        self.table[7][1] = "H15"
        self.table[7][2] = "H21"
        self.table[7][3] = "H62"
        self.table[7][4] = "H11"
        self.table[7][5] = "H62"
        self.table[7][6] = "H21"
        self.table[7][7] = "H15"
        self.table[7][8] = "H56"
        self.active_user = ""

    def set_value(self, row, column, value):
        self.table[row][column] = value

    def get_value(self, row, column):
        return str(self.table[row][column])

    def get_top(self, row, column):
        return int(str(self.table[row][column])[1])

    def get_right(self, row, column):
        return int(str(self.table[row][column])[2])

    def print_board(self):
        count = 8
        print("        (1)       (2)       (3)       (4)       (5)       (6)       (7)       (8)       (9)")
        for i in range(8):
            print ("(" + str(count) + ")", end="     ")
            count -= 1
            for j in range(9):
                print(str(self.table[i][j]).ljust(10), end="")
            print(" ")

    def update_board(self, source_row, source_column, dest_row, dest_column, top, right, active):
        self.table[source_row][source_column] = "0"
        self.table[dest_row][dest_column] = active + str(top) + str(right)

    def check_moves(self, source_row, source_column, dest_row, dest_column, active_player):
        valid_move = self.get_moves(source_row, source_column, active_player)
        if valid_move[dest_row][dest_column]:
            return True
        return False

    # gets all the moves for the active die - returns true if the source/dest are a valid combination, false otherwise
    def get_moves(self, source_row, source_column, active_player):
        valid_moves = [[False for i in range(9)] for j in range(8)]

        self.active_user = str(self.table[source_row][source_column])[0]
        if active_player != self.active_user:
            return valid_moves

        top_die = int(str(self.table[source_row][source_column])[1])

        top = top_die
        x = source_row
        y = source_column

        # print("Starting at: " + str(source_row) + "," + str(source_column))
        #print("TOP: " + str(top))

        for i in reversed(range(1, top + 1)):
            #print("Checking: " + str(x - 1) + " and " + str(y + (i - 1)))
            if self.check_dest(x - 1, y + (i - 1))\
                    and (self.frontal_path(source_row, source_column, x - 1, y + (i - 1)) or self.lateral_path(source_row, source_column, x - 1, y + (i - 1))):
                valid_moves[x - 1][y + (i - 1)] = True
            x -= 1

        top = top_die
        x = source_row
        y = source_column

        for i in reversed(range(1, top + 1)):
            if self.check_dest(x - 1, y - (i - 1)) \
                    and (self.frontal_path(source_row, source_column, x - 1, y - (i - 1)) or self.lateral_path(source_row, source_column, x - 1, y - (i - 1))):
                valid_moves[x - 1][y - (i - 1)] = True
            x -= 1

        top = top_die
        x = source_row
        y = source_column

        #print ("TOP: "  + str(top))
        for i in reversed(range(1, top + 1)):
            #print("Checking: " + str(x + 1) + " and " + str(y + (i - 1)))
            if self.check_dest(x + 1, y + (i - 1))\
                    and (self.frontal_path(source_row, source_column, x + 1, y + (i - 1)) or self.lateral_path(source_row, source_column, x + 1, y + (i - 1))):
                #print ("FRONTAL " + str(self.frontal_path(source_row, source_column, x + 1, y + (i - 1))))
                valid_moves[x + 1][y + (i - 1)] = True
            x += 1

        top = top_die
        x = source_row
        y = source_column
        #print ("TOP: "  + str(top))
        for i in reversed(range(1, top + 1)):
            #print("Checking: " + str(x + 1) + " and " + str(y - (i - 1)))
            if self.check_dest(x + 1, y - (i - 1)) and (self.frontal_path(source_row, source_column, x + 1, y - (i-1) or self.lateral_path(source_row, source_column, x + 1, y - (i - 1)))):
                valid_moves[x + 1][y - (i - 1)] = True
            x += 1

        if self.check_dest(source_row + top_die, source_column) and (
                    self.frontal_path(source_row, source_column, source_row + top_die, source_column) and
                    self.lateral_path(source_row, source_column, source_row + top_die, source_column)):
            valid_moves[source_row + top_die][source_column] = True

        if self.check_dest(source_row - top_die, source_column) and (
                    self.frontal_path(source_row, source_column, source_row - top_die, source_column) and
                    self.lateral_path(source_row, source_column, source_row - top_die, source_column)):
            valid_moves[source_row - top_die][source_column] = True

        if self.check_dest(source_row, source_column + top_die) and (
                    self.frontal_path(source_row, source_column, source_row, source_column + top_die) and
                    self.lateral_path(source_row, source_column, source_row, source_column + top_die)):
            valid_moves[source_row][source_column + top_die] = True


        if self.check_dest(source_row, source_column - top_die) and (
                    self.frontal_path(source_row, source_column, source_row, source_column - top_die) and
                    self.lateral_path(source_row, source_column, source_row, source_column - top_die)):
            valid_moves[source_row][source_column - top_die] = True

        return valid_moves

    def check_dest(self, x, y):
        if x > 7 or x < 0 or y > 8 or y < 0 or str(self.table[x][y])[0] == self.active_user:
            return False
        return True

    def check_partial(self, x, y):
        if x > 7 or x < 0 or y > 8 or y < 0 or str(self.table[x][y]) != "0":
            return False
        else:
            return True

    def valid_direction(self, source_row, source_column, dest_row, dest_column):
        if source_row == dest_row or source_column == dest_column:
            return 's'
        elif self.frontal_path(source_row, source_column, dest_row, dest_column) and \
                self.lateral_path(source_row, source_column, dest_row, dest_column):
            return 'b'
        elif self.frontal_path(source_row, source_column, dest_row, dest_column):
            return 'f'
        else:
            return 'l'

    def frontal_path(self, source_row, source_column, dest_row, dest_column):
        up = (source_row > dest_row)
        right = (source_column < dest_column)

        if up:
            source_row -= 1
            while source_row > dest_row:
                if not self.check_partial(source_row, source_column):
                    return False
                source_row -= 1
            if right:
                while source_column < dest_column:
                    if not self.check_partial(dest_column, source_column):
                        return False
                    source_column += 1
            else:
                while source_column > dest_column:
                    if not self.check_partial(dest_row, source_column):
                        return False
                    source_column -= 1
        else:
            source_row += 1
            while source_row < dest_row:
                if not self.check_partial(source_row, source_column):
                    return False
                source_row += 1
                if not right:
                    while source_column > dest_column:
                        if not self.check_partial(dest_row, source_column):
                            return False
                        source_column -= 1
                else:
                    while source_column < dest_column:
                        if not self.check_partial(dest_row, source_column):
                            return False
                        source_column += 1
        return True

    def lateral_path(self, source_row, source_column, dest_row, dest_column):
        up = (source_row > dest_column)
        right = (source_column < dest_column)

        if right:
            source_column += 1
            while source_column < dest_column:
                if not self.check_partial(source_row, source_column):
                    return False
                source_column += 1
            if up:
                while source_row > dest_row:
                    if not self.check_partial(source_row, dest_column):
                        return False
                    source_row -= 1
            else:
                while source_row < dest_row:
                    if not self.check_partial(source_row, dest_column):
                        return False
                    source_row += 1
        else:
            source_column -= 1
            while source_column > dest_column:
                if not self.check_partial(source_row, source_column):
                    return False
                source_column -= 1
            if up:
                while source_row > dest_row:
                    if not self.check_partial(source_row, dest_column):
                        return False
                    source_row -= 1
            else:
                while source_row < dest_row:
                    if not self.check_partial(source_row, dest_column):
                        return False
                    source_row += 1

        return True

    # make sure that the source co-ordinates and dest co-ordinates are within the realm of the board
    @staticmethod
    def validate_move(source_row, source_column, dest_row, dest_column):
        if source_row > 10 or source_row < 1:
            print ("Source row needs to be between 1-9")
            return False
        if dest_row > 10 or dest_row < 1:
            print ("Destination row needs to be between 1-9")
            return False
        if source_column > 9 or source_column < 1:
            print ("Source column needs to be between 1-8")
            return False
        if dest_column > 9 or dest_column < 1:
            print("Destination column needs to be between 1-8")
        return True

    # convert the users co-ordinates into board-usable co-ordinates
    @staticmethod
    def convert_coordinate(type, value):
        if type == "row":
            if value == 1:
                return 7
            if value == 2:
                return 6
            if value == 3:
                return 5
            if value == 4:
                return 4
            if value == 5:
                return 3
            if value == 6:
                return 2
            if value == 7:
                return 1
            if value == 8:
                return 0
        else:
            return value - 1
