# Game simulator
## Game program


from gClasses import Boss
from gFunctions import playerCheck
from gFunctions import createPlayers
# imports necessary game functions and classes

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
