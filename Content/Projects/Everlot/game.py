from setup import *
from player import *


def startGame():
    global player_location
    player_location = list(world.keys())[0]
    while True:
        print(player_location)
        displayDescription(player_location)
        displayActions(list(getLocationActions(player_location).keys()))
        displayWorld()
        userCommand = input("Enter a Command: ")
        isMove, consequence = performAction(userCommand, getLocationActions(player_location))
        if isMove:
            if consequence != "None":
                player_location = consequence
            else:
                print("Cannot move that way.")
        else:
            print(consequence)



def displayDescription(location):
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