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


def performAction(action, allActionsForLocation):

    if action in allActionsForLocation.keys():

        if playerRequestToMove(action):
            consequence = move(action, allActionsForLocation)
        else:
            consequence = allActionsForLocation[action]

        return (True, consequence)
    else:
        return (False, "Not a real move here.")




