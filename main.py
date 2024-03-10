from Scripts.CharacterClass import Character
from Scripts.Characters import Banan


class GameManager:
    def __init__(self, player1, player2):
        self.board = [None for _ in range(9)]
        if issubclass(type(player1), Character):
            player1.gamemanager = self
        if issubclass(type(player2), Character):
            player2.gamemanager = self
        self.insert(player1, 2)
        self.insert(player2, 6)

    def insert(self, character, position):
        if self.board[position] is not None:
            raise RuntimeError("tried to place " + str(character) + " in a non-empty space")
        else:
            if character in self.board:
                self.board[self.getpos(character)] = None
            self.board[position] = character
            return True

    def getdirection(self, character):
        for tile in self.board[0:self.getpos(character)]:
            if tile is not None:
                return -1  #left
        return 1  #right

    def getpos(self, character):
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
