
####################################################################
#   Game Class
####################################################################
class Computer:
    def __init__(self, board, active_player):
        self.activePlayer = active_player
        self.board = board

    def get_moves(self):
        for i in range(8):
            for j in range(9):
                print("HEI")
