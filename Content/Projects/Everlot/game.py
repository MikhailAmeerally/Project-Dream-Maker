from setup import *
from player import *
from setup import printWelcomeMessage, printInstructions



def startGame(world, player):

    printWelcomeMessage()
    printInstructions()

    nonPlayerCommands = {"help": myHelp, "Show World": displayWorld}
    player['location'] = list(world.keys())[0]
    gameOver = False
    while player['health'] != 0 and not gameOver:
        displayDescription(player['location'])
        displayActions(list(getLocationActions(player['location']).keys()))
        userCommand = input("Enter a Command: ")
        if inputIsPlayerAction(userCommand, nonPlayerCommands):
            performAction(userCommand, getLocationActions(player['location']), player)



def displayDescription(location):
    print(location)
    print(world[location]['short description']) if world[location]['visited'] else print(world[location]["long description"])


def displayActions(locations):
    for i in locations:
        print(i)

def getLocationActions(location):
    return world[location]['actions']

def displayWorld():
    print(world['layout'])

def myHelp():
    print("This is a help function.")

def inputIsPlayerAction(cmd, nonPlayerCommands):
    if cmd in list(nonPlayerCommands.keys()):
        nonPlayerCommands[cmd]()
        return False
    return True

