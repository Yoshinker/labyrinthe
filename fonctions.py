class Robot:
    """Classe du joueur, comportant sa position et ses mouvements"""

    def __init__(self, tuple_position, carte):
        """Constructeur"""

        self.x = tuple_position[0]
        self.y = tuple_position[1]
        self.map = carte
        self.old = ' '

    def __repr__(self):
        tableau = str()
        for j in range(len(self.map[0])):
            for i in self.map:
                tableau += i[j]
            tableau += '\n'
        return tableau

    def verification(self):
        """Renvoie les mouvements possible du robot"""
        hauteur = len(self.map[0])
        base = len(self.map)
        can_up, can_down, can_left, can_right = True, True, True, True
        if self.map[self.x-1][self.y] == "O":
            can_left = False
        if self.map[self.x+1][self.y] == "O":
            can_right = False
        if self.map[self.x][self.y-1] == "O":
            can_up = False
        if self.map[self.x][self.y+1] == "O":
            can_down = False
        return {'up': can_up, 'down': can_down, 'left': can_left, 'right': can_right}

    def ouest(self):
        """Mouvement vers l'ouest"""
        verif = self.verification()
        if verif["left"] == True:
            self.map[self.x][self.y] = self.old
            self.old = self.map[self.x-1][self.y]
            self.x += -1
            self.map[self.x][self.y] = 'X'
            print(self)

    def est(self):
        """Mouvement vers l'est"""
        verif = self.verification()
        if verif["right"] == True:
            self.map[self.x][self.y] = self.old
            self.old = self.map[self.x+1][self.y]
            self.x += 1
            self.map[self.x][self.y] = 'X'
            print(self)
    
    def nord(self):
        """Mouvement vers le nord"""
        verif = self.verification()
        if verif["up"] == True:
            self.map[self.x][self.y] = self.old
            self.old = self.map[self.x][self.y-1]
            self.y += -1
            self.map[self.x][self.y] = 'X'
            print(self)

    def sud(self):
        """Mouvement vers le sud"""
        verif = self.verification()
        if verif["down"] == True:
            self.map[self.x][self.y] = self.old
            self.old = self.map[self.x][self.y+1]
            self.y += 1
            self.map[self.x][self.y] = 'X'
            print(self)