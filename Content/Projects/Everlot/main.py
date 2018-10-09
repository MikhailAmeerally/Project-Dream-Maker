#imports

def getMapLayout(fileDescriptor):
    layout = ""
    line = fileDescriptor.readline().strip()
    while (line != "END"):
        layout = layout + line + "\n"
        line = fileDescriptor.readline().strip()
    return layout

def getTitle(fileDescriptor):
    return fileDescriptor.readline().strip()

def getShortDescription(fileDescriptor):
    shortDescription = ""
    line = fileDescriptor.readline()
    while(line.strip() != "START"):
        shortDescription = shortDescription + line.strip()
        line = fileDescriptor.readline()
    return shortDescription

def getLongDescription(fileDescriptor):
    longDescription = ""
    line = fileDescriptor.readline()
    while(line.strip() != "END"):
        longDescription = longDescription + line.strip()
        line = fileDescriptor.readline()
    return longDescription

def getActionsForLocation(fileDescriptor):
    actions = {}
    line = fileDescriptor.readline()
    while(line.strip() != "END"):
        action, consequence = line.split(":")
        actions[action] = consequence
        line = fileDescriptor.readline()
    return actions




#Player
inventory = {'spells':[], 'weapons':[], 'items':[]}
health = 100
status = "Knave"
current_room = ""
actions = []

#Map
map = {}
layout = ""

file = open('map.txt')

line = file.readline()
while(line):

    if line.strip() == "LOCATION":
        title = getTitle(file)
        short = getShortDescription(file)
        long = getLongDescription(file)
        map[title] = {"short description":short, "long description":long}

    if line.strip() == "LAYOUT":
        layout = getMapLayout(file)
    line = file.readline()

    if line.strip() == "ACTIONS":
        actionsList = getActionsForLocation(file)
        map[title]['actions'] = actionsList




