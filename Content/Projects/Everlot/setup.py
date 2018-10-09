# world
world = {}


def getWorldLayout(fileDescriptor):
    layout = ""
    line = fileDescriptor.readline().strip()
    while line != "END":
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
        actions[action.strip()] = consequence.strip()
        line = fileDescriptor.readline()
    return actions



