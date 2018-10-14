# world
world = {}
darkKnight = {"name": "Dark Knight", "health": 200}


inventory = ["Wand of Azaroth"]
health = 100
status = "Knave"
player_location = ""
money = 100
player = {"inventory": inventory, "health": health, "status":status, "location": player_location, "money":money}

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
        longDescription = longDescription + line.strip() + "\n"
        line = fileDescriptor.readline()
    return longDescription

def getActionsForLocation(fileDescriptor):
    actions = {}
    line = fileDescriptor.readline()
    while(line.strip() != "END"):
        action= line.split(":")
        actions[action[0].strip()] = [action[1].strip()]
        if len(action) > 2:
            actions[action[0].strip()].append(action[2].strip())
        line = fileDescriptor.readline()
    return actions


def printInstructions():
    print("Enter the commands and beat the Dark Knight. Type help for more info.\n"
          "There are some hidden features in the game, so have fun!")


def printWelcomeMessage():
    print('''
     __      __       .__                                  __           ___________                  .__          __   
/  \    /  \ ____ |  |   ____  ____   _____   ____   _/  |_  ____   \_   _____/__  __ ___________|  |   _____/  |_ 
\   \/\/   // __ \|  | _/ ___\/  _ \ /     \_/ __ \  \   __\/  _ \   |    __)_\  \/ // __ \_  __ \  |  /  _ \   __\
 \        /\  ___/|  |_\  \__(  <_> )  Y Y  \  ___/   |  | (  <_> )  |        \\   /\  ___/|  | \/  |_(  <_> )  |  
  \__/\  /  \___  >____/\___  >____/|__|_|  /\___  >  |__|  \____/  /_______  / \_/  \___  >__|  |____/\____/|__|  
       \/       \/          \/            \/     \/                         \/           \/''')