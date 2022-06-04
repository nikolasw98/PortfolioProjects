# Game simulator
## Game's user-defined classes

import math                                                                                                             # math module used for rounding minion stats

class Character:
    '''class that represents characters in a game'''
    def __init__(self, name, lvl=1, hp=100, at=10, df=1, exp=1):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.at = at
        self.df = df
        self.maxhp = hp
    # implementations of methods setlvl(), sethp(), setat(), setdf(), and setexp()

    def rename(self, name):
        '''Renames the character'''
        self.name = name

    def setlvl(self, lvl):
        '''Sets character level (lvl)'''                                                                                ## ensures lvl cannot be below 1 (base level)
        if lvl <= 1:
            self.lvl = 0
        else:
            self.lvl = lvl

    def sethp(self, hp):
        '''Set HP to new value, or set HP to 0 if hp is below 0'''                                                      ## ensures no negative hp
        if hp <= 0:
            self.hp = 0
        else:
            self.hp = hp

    def setat(self, at):
        '''Sets character's attack level (at)'''
        self.at = at

    def setdf(self, df):
        '''Sets character's defense level (df)'''
        self.df = df

    def setexp(self, exp):
        '''Sets character's experience (exp)'''
        self.exp = exp

    def getname(self):
        '''Returns character's name'''
        return self.name

    def getlvl(self):
        '''Returns character's level (lvl)'''
        return self.lvl

    def gethp(self):
        '''Returns character's health points (hp)'''
        return self.hp

    def getmaxhp(self):
        '''Returns character's max hp'''
        return self.maxhp

    def getat(self):
        '''Returns character's attack level (at) '''
        return self.at

    def getdf(self):
        '''Returns character's defense level (df)'''
        return self.df

    def getexp(self):
        '''Returns character's experience (exp)'''
        return self.exp

    def attack(self, other):                                                                                            # self.character deals damage to other.character; damage = (self.at - other.df)
        '''Reduces other.name's HP by damage, where damage = (self.at - other.df)'''
        if self.at > other.df:                                                                                          ## make sure there is no healing
            other.sethp(other.hp - (self.at - other.df))
        else:
            print(self.name, " is too weak.")
        print(self.name, " attacked ", other.name, ". ", self.name, "'s HP is ", self.hp, "/", self.maxhp,". ",
              other.name, "'s HP is ", other.hp, "/", other.maxhp, ". ", sep="")                                        ## prints action: characters' hp and the names of both the attacking character and the damaged character
        if self.hp == 0:                                                                                                ## prints the defeated chracter's name
            print(other.name, " defeated ", self.name, sep="")
        elif other.hp == 0:
            print(self.name, " defeated ", other.name, sep="")

class MajorCharacter(Character):
    '''Subclass of character that has additional functions: recover(), fullheal(), shield(), charge()'''
    def __init__(self, name, lvl=1, hp=100, at=10, df=1, exp=1):
        Character.__init__(self, name, lvl, hp, at, df, exp)
        self.maxhp = hp
        self.shields = 0
        self.shield = 'N'
        self.charged = False
    # implementation of all Character class methods

    def recover(self, recoverpts):                                                                                      # MajorCharacter class method #1
        '''Recover the current character's HP by recoverpts UP TO the max'''
        self.hp += recoverpts
        if self.hp > self.maxhp:                                                                                        ## makes sure hp does not exceed maxhp
            self.hp = self.maxhp
        print(self.name, "'s HP has been restored to ", self.hp, "/", self.maxhp, ".", sep="")

    def fullheal(self):                                                                                                 # MajorCharacter class method #2
        '''Set character's HP to character's maxhp'''
        self.sethp(self.maxhp)
        print(self.name, "'s HP has been fully restored (", self.maxhp, "/", self.maxhp, ").", sep="")

    def setshield(self, shields):                                                                                       ## Gives character three shields; shields negate all damage for next three turns
        '''Resets character's shields'''
        if self.shields <= 0:                                                                                           ## shields are not stackable
            self.shields = 3
            print("{} now has 3 shields!".format(self.name))
        elif self.shields >= 3:
            self.shields = 3
            print("{}'s shields have been reset!".format(self.name, ))
        else:
            self.shields = shields
            print("Nothing happened! {} still has {} shields.".format(self.name, self.getshield()))

    def getshield(self):
        '''Returns the number of shields the character has left'''
        return self.shields

    def decr_shield(self):
        '''Decrease character's loses a shield for each attack from another character'''
        if self.shields >= 1:
            self.shields -= 1                                                                                           ## counter for shields when used


    def setcharge(self, charged=False):
        '''Multiplies next attack by 2.5x'''                                                                            ## not stackable
        self.charged = True

    def getcharge(self):                                                                                                ## avoids bool TypeError
        '''Returns character's charge status'''
        return self.charged

    def sethp(self, hp):
        '''Factors shields in to majorcharacter's hp'''
        if hp <= 0:
            self.hp = 0
        elif self.getshield() > 0:                                                                                      ## damage negation if shield is used
            self.decr_shield()
            if self.getshield() >= 1:
                print("{} used a shield!".format(self.name))
            elif self.getshield() == 0:
                print("{} used last shield!".format(self.name))
                self.shield = 'N'                                                                                       ## ignores damage negation once shields are used up
        elif hp >= 0 and self.getshield() == 0:
            self.hp = hp

    def attack(self, other):                                                                                            # charged attack condition added to attack function for majorcharacters
        '''Reduces other.name's HP by damage, where damage = (self.at - other.df)'''
        if self.getcharge() is True:                                                                                    ## charged attack condition (2.5x for next attack)
            self.setat(float(self.getat() * 2.5))                                                                       ## returns chraged attacked
            if self.at > float(other.df):
                other.sethp(int(float(other.hp) - (self.at - float(other.df))))
                self.charged = False
                self.setat(int(self.getat()/2.5))
            else:
                print(self.name, " is too weak.")
            print(self.name, " attacked ", other.name, ". ", self.name, "'s HP is ", self.hp, "/", self.maxhp, ". ",
                  other.name, "'s HP is ", other.hp, "/", other.maxhp, ". ", sep="")
            if self.hp == 0:                                                                                            ## prints the defeated chracter's name
                print(other.name, " defeated ", self.name, sep="")
            elif other.hp == 0:
                print(self.name, " defeated ", other.name, sep="")
        else:
            if self.at > other.df:                                                                                      ## make sure there is no healing
                other.sethp(other.hp - (self.at - other.df))
            else:
                print(self.name, " is too weak.")
            print(self.name, " attacked ", other.name, ". ", self.name, "'s HP is ", self.hp, "/", self.maxhp, ". ",
                  other.name, "'s HP is ", other.hp, "/", other.maxhp, ". ",
                  sep="")                                                                                               ## prints action: characters' hp and the names of both the attacking character and the damaged character
            if self.hp == 0:                                                                                            ## prints the defeated chracter's name
                print(other.name, " defeated ", self.name, sep="")
            elif other.hp == 0:
                print(self.name, " defeated ", other.name, sep="")

class Minion(Character):
    '''Subclass of Character, no additional attributes'''
    def __init__(self, name, lvl=1, hp=100, at=10, df=0, exp=0):
        Character.__init__(self, name, lvl, hp, at, df, exp)
        self.maxhp = hp
    # implementations of all Character class methods

class Boss(Character):
    '''Subclass of Character class with additional attribute: spawn()'''
    def __init__(self, name='Boss', lvl=1, hp=100, at=10, df=1, exp=1):
        Character.__init__(self, name, lvl, hp, at, df, exp)
        self.maxhp = hp
    ## implementations of all Character class methods

    def spawn(self, minionList=[]):
        '''Generates a Minion, named "Minion", with HP and AT equal to 1/4 (rounded down) of Boss's max.'''
        self.minionList = minionList
        self.blvl = self.getlvl()
        if (self.getmaxhp() % 4) == 0 and (self.getat() % 4) == 0:
            newminion = Minion('Minion', hp=(int(self.getmaxhp()/4)), at=(int(self.getat()/4)), df=0, exp=0)
        elif (self.getmaxhp() % 4) == 0 and (self.getat() % 4) != 0:
            newminion = Minion('Minion', hp=(int(self.getmaxhp()/4)), at=math.floor(self.getat()/4), df=0, exp=0)
        elif (self.getmaxhp() % 4) != 0 and (self.getat() % 4) == 0:
            newminion = Minion('Minion', hp=math.floor(self.getmaxhp()/4), at=(int(self.getat()/4)), df=0, exp=0)
        else:
            newminion = Minion('Minion', hp=math.floor(self.getmaxhp()/4), at=math.floor(self.getat()/4), df=0, exp=0)
        newminion.setlvl(self.blvl)
        print(self.name, " spawned Minion.", "(HP ", newminion.gethp(), ", AT ", newminion.getat(), ", DF ",
              newminion.getdf(), ")", sep="")
        self.minionList.append(newminion)
        return self.minionList

## Game functions

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

## Game program

playerlist = []                                                                                                         ## list that tracks number of players alive
spawnMinions = []                                                                                                       ## list that tracks number of minions alive
numPlayers = eval(input('How many players (enter integer from 1-8)? '))

z = playerCheck(numPlayers)
createPlayers(z, playerlist)

for players in playerlist[0:]:                                                                                          # prints player stats
    print(players.getname(), "'s stats: LVL ", players.getlvl(), ", HP ", players.gethp(), ", AT ", players.getat(),
          ", DF ", players.getdf(), sep="")

boss = Boss("Boss", lvl=1, hp=20*len(playerlist), at=100, df=0, exp=0)

while len(playerlist) > 0 and boss.gethp() > 0:
    boss.spawn(spawnMinions)
    for players in playerlist[0:len(playerlist)]:                                                                       # player actions
        print('1. Attack')
        print('2. Charge')
        print('3. Shield')
        playeraction = eval(input("{} what would you like to do? ".format(players.name)))                               ## player selects action desired
        if playeraction == 1:
            if len(spawnMinions) > 1:                                                                                   ## player can choose minion to attack if more than one minion is alive
                for minion in spawnMinions[0:]:
                    print("{} (HP {})".format(minion.name, minion.gethp()))
                    minionattacked = eval((input("{}, who would you like to attack? ")))
                    players.attack(spawnMinions[int(minionattacked-1)])
                    oppattacked = spawnMinions[int(minionattacked-1)]
                    if oppattacked.gethp() == 0:
                        spawnMinions.remove(oppattacked)
            elif len(spawnMinions) == 1:                                                                                ## attacks only spawned minion
                players.attack(spawnMinions[0])
                theminion = spawnMinions[0]
                if theminion.gethp() == 0:
                    spawnMinions.remove(spawnMinions[0])
                    continue                                                                                            ## restart loop since minions aren't alive
            else:                                                                                                       ## boss is attacked if all minions are dead
                players.attack(boss)
                if boss.gethp() == 0:
                    break                                                                                               ## end game if boss's hp is zero
        elif playeraction == 2:                                                                                         ## charges next attack
            players.setcharge()
            print('{}, your attack is charged!'.format(players.getname()))
        elif playeraction == 3:                                                                                         ## shields are used
            players.setshield(players.getshield())
    for minions in spawnMinions[0:]:                                                                                    # opponent (Minion) actions
        if len(playerlist) > 0:
            playerattacked = playerlist[(len(playerlist)-1)]                                                            ## minions attack last player to join
            minions.attack(playerattacked)
            if playerattacked.gethp() <= 0:
                playerlist.remove(playerattacked)                                                                       ## remove player once hp is 0
        else:
            break                                                                                                       ## end game if all players are dead

if len(playerlist) == 0:                                                                                                # notify player when game ends
    print('You lose.')
else:
    print('You win!')
