# imports
from setup import *
from game import startGame

inventory = []
health = 100
status = "Knave"
player_location = ""
money = 50
player = {"inventory": inventory, "health": health, "status":status, "location": player_location, "money":money}


file = open('world.txt')

line = file.readline()
while line:

    if line.strip() == "LOCATION":
        title = getTitle(file)
        short = getShortDescription(file)
        long = getLongDescription(file)
        world[title] = {"short description": short, "long description": long, "visited": False}

    if line.strip() == "LAYOUT":
        world['layout'] = getWorldLayout(file)

    if line.strip() == "ACTIONS":
        actionsList = getActionsForLocation(file)
        world[title]['actions'] = actionsList

    line = file.readline()


startGame(world, player)


