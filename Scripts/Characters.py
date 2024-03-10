from Scripts.CharacterClass import Character

class Banan(Character):
    def __init__(self, nbr, gamemanager):
        super().__init__("Banan " + str(nbr), [], gamemanager)
