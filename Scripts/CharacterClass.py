class Character:
    def __init__(self, name, deck, gamemanager):
        self.name = name
        self.hp = 30

        self.deck = deck
        self.gauge = []
        self.boost = []
        self.discard = []

        self.gamemanager = gamemanager

    def advance(self, n):
        """prend en argument un int qui représente le nombre de cases dont le perso avancera
        (advance = avancer, si on rencontre un ennemi,
        on lui passe derriére mais cela ne compte pas pour un mouvement)"""
        if n < 0:
            raise ValueError("tried to advance for a negative amount")
        direction = self.gamemanager.getdirection(self)
        n *= direction
        index = self.gamemanager.getpos(self)
        if n + index > 8:
            n = 8 - index
        elif n + index < 0:
            n = -index
        target = index + n
        if n < 0:
            targets = [i for i in range(n, 0)]
        else:
            targets = [i for i in range(1, n + 1)]
        for nbr in targets:
            if self.gamemanager.board[nbr + index] is not None:
                if index + nbr == 8:
                    target -= 1 * direction
                elif target < 8:
                    target += 1 * direction
        self.gamemanager.insert(self, target)
        return True

    def close(self, n):
        """La meme fonction que advance mais le perso ne peut traverser d'autres persos"""
        if n < 0:
            raise ValueError("tried to close for a negative amount")
        direction = self.gamemanager.getdirection(self)
        n *= direction
        index = self.gamemanager.getpos(self)
        if n + index > 8:
            n = 8 - index
        elif n + index < 0:
            n = -index
        target = index + n
        if n < 0:
            targets = [i for i in range(n, 0)]
        else:
            targets = [i for i in range(1, n + 1)]
        for nbr in targets:
            if self.gamemanager.board[nbr + index] is not None:
                target = index + nbr - 1 * direction
        self.gamemanager.insert(self, target)
        return True

    def retreat(self, n):
        """fait reculer le personnage de n cases"""
        if n < 0:
            raise ValueError("tried to retreat for a negative amount")
        direction = self.gamemanager.getdirection(self)
        n *= direction
        index = self.gamemanager.getpos(self)
        if index - n > 8:
            n = - 8 + index
        elif index - n < 0:
            n = index
        target = index - n
        self.gamemanager.insert(self, target)
        return True

    def pull(self, target, n):
        """fait avancer l'ennemi vers vous"""
        target.close(n)
        return True

    def push(self, target, n):
        """fait reculer l'ennemi"""
        target.retreat(n)
        return True

    def __repr__(self):
        return self.name + " (" + str(self.hp) + ")"
