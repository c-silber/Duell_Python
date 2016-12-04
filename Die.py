

####################################################################
#   Die Class
####################################################################
class Die:
    def __init__(self, top, right):
        self.top = top
        self.right = right
        self.key = False
        if top == 1 and right == 1:
            self.key = True

    def roll_die(self, source_x, source_y, dest_x, dest_y, direction):
        frontal = abs(dest_x - source_x)
        lateral = abs(dest_y - source_y)

        up = (dest_x < source_x)
        right = (source_y < dest_y)

        if direction == 'f':
            self.get_frontal(frontal, up)
            self.get_lateral(lateral, right)
        else:
            self.get_lateral(lateral, right)
            self.get_frontal(frontal, up)

    def get_frontal(self, frontal, up):
        if not self.key:
            temp_frontal = frontal
            while frontal > 0:
                if self.right == 1:
                    if self.top == 2:
                        self.top = 3
                    elif self.top == 3:
                        self.top = 5
                    elif self.top == 5:
                        self.top = 4
                elif self.right == 2:
                    if self.top == 6:
                        self.top = 3
                    elif self.top == 1:
                        self.top = 4
                    elif self.top == 3:
                        self.top = 1
                    elif self.top == 4:
                        self.top = 6
                elif self.right == 3:
                    if self.top == 1:
                        self.top = 2
                    elif self.top == 2:
                        self.top = 6
                    elif self.top == 5:
                        self.top = 1
                    elif self.top == 6:
                        self.top = 5
                elif self.right == 4:
                    if self.top == 1:
                        self.top = 5
                    elif self.top == 2:
                        self.top = 1
                    elif self.top == 5:
                        self.top = 6
                    elif self.top == 6:
                        self.top = 2
                elif self.right == 5:
                    if self.top == 1:
                        self.top = 3
                    elif self.top == 3:
                        self.top = 6
                    elif self.top == 4:
                        self.top = 1
                    elif self.top == 6:
                        self.top = 4
                elif self.right == 6:
                    if self.top == 4:
                        self.top = 5
                    elif self.top == 2:
                        self.top = 4
                    elif self.top == 3:
                        self.top = 2
                    elif self.top == 5:
                        self.top = 3
                frontal -= 1

            if (not up) and (temp_frontal % 2 != 0):
                self.top = 7 - self.top

    def get_lateral(self, lateral, right):
        if not self.key:
            while lateral > 0:
                if right:
                    temp = 7 - self.right
                    self.right = self.top
                    left = 7 - self.right
                    self.top = temp
                else:
                    temp = self.right
                    left = self.top
                    self.right = 7 - left
                    self.top = temp
                lateral -= 1

    def get_top(self):
        return self.top

    def get_right(self):
        return self.right
