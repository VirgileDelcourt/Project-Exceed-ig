from Scripts.CharacterClass import Character
from Scripts.Characters import Banan


class GameManager:
    """GameManager, Game Master, Dugeon Master ?
    Peut importe ce que vous l'appelez, c'est lui qui s'occupe de 
    garder en mémoire tout ce qui n'a pas trait aux joueurs 
    (surtout l'état du terrain)"""
     
    def __init__(self, player1, player2):
        """Prend en argument les deux joueurs et commence la partie"""
        self.board = [None for _ in range(9)]
        if issubclass(type(player1), Character):
            player1.gamemanager = self
        if issubclass(type(player2), Character):
            player2.gamemanager = self
        self.insert(player1, 2)
        self.insert(player2, 6)

    def insert(self, character, position):
        """Prend en argument un objet Character et un int (entre 0 et 8)
        enleve le personnage si il était deja sur le terrain
        puis le place sur la case voulue.
        Essayer de le placer sur une case ou il y a deja quelque chose renvoit une erreur"""
        if self.board[position] is not None:
            raise RuntimeError("tried to place " + str(character) + " in a non-empty space")
        else:
            if character in self.board:
                self.board[self.getpos(character)] = None
            self.board[position] = character
            return True

    def getdirection(self, character):
        """prend en argument un objet Character
        renvoie 1 si il regarde à droite et -1 si il regarde à gauche.
        Son orientation est décidée en fonction de sa position relative à l'ennemi
        (il regarde toujours l'ennemi)"""
        for tile in self.board[0:self.getpos(character)]:
            if tile is not None:
                return -1  #left
        return 1  #right

    def getpos(self, character):
        """prend en argument un objet Character
        et renvoi un int qui représente sa position sur le terrain
        renvoi une erreur si le personnage n'est pas sur le terrain"""
        if character not in self.board:
            raise ValueError(str(character) + " not on board")
        else:
            return self.board.index(character)


if __name__ == '__main__':
    banan = Banan(1, None)
    banan2 = Banan(2, None)
    pap = GameManager(banan, banan2)
    print(pap.board)
    banan.push(banan2, 100)
    print(pap.board)
    print(" ")
