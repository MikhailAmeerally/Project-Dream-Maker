from setup import *
from player import *
from setup import printWelcomeMessage, printInstructions
import SpecialCommands



def startGame(world, player):
    specialCommands = {SpecialCommands.WRAITH_MASTER_CMD: getWraithMaster}
    printWelcomeMessage()
    printInstructions()

    nonPlayerCommands = {"help": myHelp, "Show World": displayWorld, "inventory": showInventory}
    player['location'] = list(world.keys())[0]
    gameOver = False
    while player['health'] != 0 and not gameOver:
        displayDescription(player['location'])
        displayActions(list(getLocationActions(player['location']).keys()))
        updateLocation(player['location'], world)
        userCommand = input("Enter a Command: ")

        if isSpecialCommand(userCommand, specialCommands):
            specialCommands[userCommand]()

        if inputIsPlayerAction(userCommand, nonPlayerCommands):
            performAction(userCommand, getLocationActions(player['location']), player, world)

        # Merlin's Tower Special Command
        if player['location'] == "Merlin's Tower" and "Wand of Azaroth" in player['inventory'] \
                and "Basic Sword" in player['inventory']:
            addAction(SpecialCommands.WRAITH_MASTER, player['location'], world)



def showInventory():
    print(player['inventory'])

def isSpecialCommand(userCommand, specialCommands):
    return userCommand in list(specialCommands.keys())

def updateLocation(location, world):
    if not world[location]['visited']:
        world[location]['visited'] = True

def displayDescription(location):
    print(location)
    print(world[location]['short description']) if world[location]['visited'] else print(world[location]["long description"])

def getWraithMaster():
    removeItemFromInventory('Basic Sword', player)
    removeItemFromInventory('Wand of Azaroth', player)
    addItemToInventory('Wraith Master', player)


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



