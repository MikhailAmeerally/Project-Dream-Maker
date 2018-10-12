'''
Special Commands are commands that will be added to the location if certain conditions are met.
These are not the same as consequential actions because these do not require you to DO something
before getting this command, like ask a question. Instead, these commands are added when the right
conditions are met.
'''

wraith_master_text_description = """Merlin sees a wand that looks familiar to him. He asks you if that's the
Wand of Azaroth. He starts doing backflips and screaming the Dark Knight will be vanquished. He asks you if you have
a sword of any kind. You say yes, pulling out your flimsy sword.

Merlin takes the sword and the wand from you and cross them on his tree stump to make a cross. He recites an encantation,
And then there is a blinding light. When the light dims, you see a sword. But this isn't your sword. This is the 
Wraith Master Sword. You take the sword and thank Merlin. Merlin is still doing backflips."""

WRAITH_MASTER_CMD = "Get Wraith Master"
WRAITH_MASTER = "Add Action - {0} - {1}".format(WRAITH_MASTER_CMD, wraith_master_text_description)