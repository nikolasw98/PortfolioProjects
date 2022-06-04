# Game's functions

from gClasses import MajorCharacter

def playerCheck(x):
    '''Checks whether the user specifies an integer between 1 and 8, inclusive'''
    if type(x) != type(1) or x > 8 or x < 1:                                                                            ## user input, integer check
        while type(x) != type(1):
            print('Error. Please enter a an integer.')
            x = eval(input('How many players (enter integer between 1 and 8)? '))
            if type(x) != type(1):
                continue
            else:
                break                                                                                                   ## check whether user inputs a number between 1 and 8, inclusive
        while x > 8 or x < 1:
            print('Error. Please enter an integer between 1 and 8 (inclusive).')
            x = eval(input('How many players (enter integer between 1 and 8)? '))
            if x > 8 or x < 1:
                continue
            else:
                return int(x)
    else:
        return int(x)

def createPlayers(x, players):
    '''Creates n number of players, and adds them to a list (players)'''                                                ## create list with player names
    y = x
    x = 1
    while x <= y:                                                                                                       ## loop creates number of players specified by user
        newPlayer = MajorCharacter(input("Player {} Name: ".format(str(x))))
        players.append(newPlayer)
        x += 1
        if x <= y:
            continue
        else:
            return players                                                                                              ## returns players list

def playerstats(players):                                                                                               # prints player stats
    print(players.getname(), "'s stats: LVL ", players.getlvl(), ", HP ", players.gethp(), ", AT ", players.getat(),
          ", DF ", players.getdf(), ", EXP ", players.getexp(), sep="")

