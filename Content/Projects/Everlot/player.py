
def move(direction, allActionsForLocation, player):
    if allActionsForLocation[direction][0] != "None":
        player['location'] = allActionsForLocation[direction][0]
    return



def playerRequestToMove(action):
    return action in ['Go North', 'Go South', 'Go East', 'Go West']

def playerRequestToBuy(action):
    return "Buy" in action

def addBlackSmithItems(action, allActionsForLocation):
    items = ''.join(action.split('.')[1]).strip()
    items = items.split(';')
    for item in items:
        dictEntry  = item.split('-')
        newAction = "Buy "+dictEntry[0].strip()
        newConsequence = int(dictEntry[1].strip())
        allActionsForLocation.update({newAction : [newConsequence]})
    del allActionsForLocation['Talk to Blacksmith']

    return

def processTransaction(action, allActionsForLocation, player):
    item = action.split("Buy ")[1]
    price = allActionsForLocation[action][0]
    if player['money'] < price:
        print("Cannot afford item.")
        return
    player['money'] = player['money']-price
    player['inventory'].append(item)
    del allActionsForLocation[action]
    print("Purchased {0} for {1}".format(item, str(price)))
    print("Adding to inventory...")
    print(player['inventory'])


def processConsequence(action, consequence, player):
    if len(consequence) > 1:
        if consequence[1] == "kill":
            player['health'] = 0
        elif consequence[1] == "Inventory":
            player['inventory'].append(action.split(" "))

def isMagical(item):
    return True if item in ['Sword of Asphedele', 'Magic Wand'] else False

def attack(enemy, item):
    weaponDamage = {"Basic Sword": 10, "Basic Shield": 0, "Magic Wand": 60, "Sword of Asphdele": 80}
    if enemy['name'] == "Dark Knight":
        if isMagical(item):
            enemy['health'] = enemy['health'] - (weaponDamage[item]*40)  # Damage suppression 60%
        else:
            print("The attack had no effect.")
    elif enemy['name'] == 'Troll':
        enemy['health'] = enemy['health'] - weaponDamage[item]




def performAction(action, allActionsForLocation, player):

    if action in allActionsForLocation.keys():

        if playerRequestToMove(action):
            move(action, allActionsForLocation, player)
        elif playerRequestToBuy(action):
            processTransaction(action.strip(), allActionsForLocation, player)
        else:
            consequence = allActionsForLocation[action]
            print(consequence[0])
            processConsequence(action , consequence, player)

            if action.lower() == "talk to blacksmith":
                print("Adding Items...")
                addBlackSmithItems(consequence[0], allActionsForLocation)
    else:
        print("Not a valid move in this location.")

