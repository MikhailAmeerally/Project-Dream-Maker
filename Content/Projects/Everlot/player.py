inventory = {'spells': {}, 'weapons': {}, 'items': {}}
health = 100
status = "Knave"
player_location = ""


def move(direction, allActionsForLocation):
    if allActionsForLocation[direction] == "None":
        return "None"
    else:
        return allActionsForLocation[direction]



def playerRequestToMove(action):
    return action in ['North', 'South', 'East', 'West']

def playerRequestToBuy(action):
    return "Buy" in action


def performAction(action, allActionsForLocation):

    if action in allActionsForLocation.keys():

        if playerRequestToMove(action):
            consequence = move(action, allActionsForLocation)
            return True, consequence
        elif playerRequestToBuy(action):
            processTransaction(action.strip().split()[1], allActionsForLocation[action])
        else:
            consequence = allActionsForLocation[action]

        return (False, consequence)
    else:
        return (False, "Not a real move here.")

def processTransaction(itemName, cost):
    if itemName in list(inventory['weapons'].keys()) || itemName in list(inventory['items'].keys()):
        return False, 0
    else:
        



