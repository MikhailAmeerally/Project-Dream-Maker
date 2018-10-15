'''
Special Commands are commands that will be added to the location if certain conditions are met.
These are not the same as consequential actions because these do not require you to DO something
before getting this command, like ask a question. Instead, these commands are added when the right
conditions are met.
'''

# WRAITH MASTER
wraith_master_text_description = """Merlin sees a wand that looks familiar to him. He asks you if that's the
Wand of Azaroth. He starts doing backflips and screaming the Dark Knight will be vanquished. He asks you if you have
a sword of any kind. You say yes, pulling out your flimsy sword.

Merlin takes the sword and the wand from you and cross them on his tree stump to make a cross. He recites an encantation,
And then there is a blinding light. When the light dims, you see a sword. But this isn't your sword. This is the 
Wraith Master Sword. You take the sword and thank Merlin. Merlin is still doing backflips."""
WRAITH_MASTER_CMD = "get wraith master"
WRAITH_MASTER = "Add Action - {0} - {1}".format(WRAITH_MASTER_CMD, wraith_master_text_description)

# TROLL BRIDGE
TROLL_CMD = "answer riddle"
TROLL_text_description = "Let's play! If you get it right, not only will he let you pass, \n " \
                         "but will also give you something of importance."
TROLL = "Add Action - {0} - {1}".format(TROLL_CMD, TROLL_text_description)
TROLL_South = "Add Action - go south - Merlin's Tower"

# FLOWER FIELDS
WAND_OF_AZAROTH_text_description = "The Flower grows, and forms a shell. You peel open the petals and find a wand inside.\n" \
                                   "It's the Wand of Azaroth."
WAND_OF_AZAROTH_CMD = "water flower"
WAND_OF_AZAROTH = "Add Action - {0} - {1}".format(WAND_OF_AZAROTH_CMD, WAND_OF_AZAROTH_text_description)

# Dark Knight
DARK_KNIGHT_CMD = "give him the chest"
DARK_KNIGHT_text_description = "You offer the Dark Knight the treasure chest, that you claim is full of treasure and magical items.\n" \
                               "You tell him that he can have it on the condition that he leaves and never returns.\n\n" \
                               "He takes the chest, opens it, and then 8 tentacles pop out, grab him, and pull him into chest.\n" \
                               "You lock the chest."
DARK_KNIGHT = "Add Action - {0} - {1}".format(DARK_KNIGHT_CMD, DARK_KNIGHT_text_description)

def trollMiniGame():
    print("Enter an answer, or type idk")
    while(True):
        user = input("Enter Answer to Riddle")
        if user == "idk":
            print("You are unable to answer the Troll's riddle. You will not be able to cross.")
            return False
        user = int(user)
        if user == 3:
            print("You successfully answered the riddle. The Troll says you may cross, and gives you a watering can?")
            return True
        print("The troll laughs at your intellectual level. He knows he is smarter than you now.")

def waterFlower():
    return True
