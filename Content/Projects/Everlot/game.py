from setup import *
from player import *



def startGame(world, player):

    player['location'] = list(world.keys())[0]
    gameOver = False
    while player['health'] != 0 and not gameOver:
        print(player['location'])
        displayDescription(player['location'])
        displayActions(list(getLocationActions(player['location']).keys()))
        #displayWorld()
        userCommand = input("Enter a Command: ")
        performAction(userCommand, getLocationActions(player['location']), player)



def displayDescription(location):
    print(location)
    if world[location]['visited']:
        print(world[location]['short description'])
    else:
        world[location]['visited'] = True
        print(world[location]['long description'])


def displayActions(locations):
    for i in locations:
        print(i)

def getLocationActions(location):
    return world[location]['actions']

def displayWorld():
    print(world['layout'])