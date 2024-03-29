from setup import darkKnight


def move(direction, allActionsForLocation, player):
    if allActionsForLocation[direction][0] != "None":
        player['location'] = allActionsForLocation[direction][0]


def removeAction(action, allActionsForLocation):
    del allActionsForLocation[action]

def removeItemFromInventory(item, player):
    player['inventory'].remove(item)

def addAction(consequence, location, world):
    consequence = consequence.strip().split("-")
    world[location]['actions'].update({consequence[1].strip(): [consequence[2].strip()]})

def playerRequestToMove(action):
    return action in ['go north', 'go south', 'go east', 'go west']

def playerRequestToAttack(action):
    return "Attack" in action

def addItemToInventory(item, player):
    player['inventory'].append(item)

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

    return

def processTransaction(action, allActionsForLocation, player):
    item = action.split("Buy ")[1]
    price = allActionsForLocation[action][0]

    if player['money'] < price:
        print("Cannot afford item.")
        return False

    if item == "Armor":
        player['health'] = player['health'] + 50

    player['money'] = player['money']-price
    player['inventory'].append(item)
    print("Purchased {0} for {1}".format(item, str(price)))
    print("Adding to inventory...")
    print(player['inventory'])
    return True

def getItem(action):
    action = action.strip().split(" ")
    item = "".join(action[1:]).strip()
    return item

def processConsequence(action, consequence, player, world):
    if len(consequence) > 1:
        if consequence[1] == "kill":
            player['health'] = 0
        elif consequence[1] == "inventory":
            item = getItem(action)
            addItemToInventory(item, player)
        elif "Add Action" in consequence[1]:
            addAction(consequence[1], player['location'], world)
        elif "HEALTH" in consequence[1]:
            health = int(consequence[1].strip().split(" - ")[1])
            player['health'] = player['health'] - health
            print("Your Health: {0}".format(player['health']))


def isMagical(item):
    return True if item in ['Sword of Asphedele', 'Magic Wand'] else False

def attack(enemy, item):
    weaponDamage = {"Basic Sword": 10, "Basic Shield": 0, "Magic Wand": 60, "Sword of Asphdele": 80, "Wraith Master" : 100}
    if enemy['name'] == "Dark Knight":
        if isMagical(item):
            enemy['health'] = enemy['health'] - (weaponDamage[item]*40)  # Damage suppression 60%
        else:
            print("The attack had no effect.")
    elif enemy['name'] == 'Troll':
        enemy['health'] = enemy['health'] - weaponDamage[item]
    print("{0}'s health is now {1}".format(enemy['name'], enemy['health']))

def getEnemyAndItem(action):
    action = action.strip().split("Attack ")
    action = "".join(action[1:])
    action = action.strip().split(" with ")
    item = "".join(action[1])
    enemy = "".join(action[0])
    return enemy, item


def performAction(action, allActionsForLocation, player, world):

    if action.lower() in allActionsForLocation.keys():

        if playerRequestToMove(action):
            move(action, allActionsForLocation, player)
            return
        elif playerRequestToBuy(action):
            if not processTransaction(action.strip(), allActionsForLocation, player):
                return
        elif playerRequestToAttack(action):
            enemy, item = getEnemyAndItem(action)
            attack(enemy, item)
        else:
            consequence = allActionsForLocation[action]
            print(consequence[0])
            processConsequence(action, consequence, player, world)

            if action.lower() == "talk to blacksmith":
                print("Adding Items...")
                addBlackSmithItems(consequence[0], allActionsForLocation)
        removeAction(action, allActionsForLocation)
    else:
        print("Not a valid move in this location.")

