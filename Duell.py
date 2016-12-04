from Game import Game

####################################################################
#   Entry point to the program
#   User is asked if they want to start a new game or a resume an existing one
#   If they choose to start an existing one, new game class is initiated, otherwise read the file
####################################################################
resumeGame = True
while resumeGame:
    print("Would you like to resume a previous game? y/n")
    resume = input()
    g = Game()
    if resume == 'y' or resume == 'Y':
        resumeGame = False
        g.begin_game(True)
    # read the file
    elif resume == 'n' or resume == 'N':
        resumeGame = False
        g.begin_game(False)
    else:
        print("Invalid Input. Please try again")
        # start a new game
