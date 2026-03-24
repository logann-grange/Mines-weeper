from case import Case
import random

class Tableau:
    def __init__(self,difficulté):
        self.difficulté = difficulté
        self.tab = []
        self.create_tableau()
        
    def create_tableau(self):
        if self.difficulté == "Facile" :
            for i in range(9) :
                self.tab.append([])
                for j in range(9) :
                    self.tab[i].append(Case((i,j), False, 0))
        elif self.difficulté == "Moyen" :
            for i in range(16) :
                self.tab.append([])
                for j in range(16) :
                    self.tab[i].append(Case((i,j), False, 0))
        else :
            for i in range(16) :
                self.tab.append([])
                for j in range(30) :
                    self.tab[i].append(Case((i,j), False, 0))
                    
    
    def generate_bombes(self):
        if self.difficulté == "Facile":
            max_bombs = 10
            min_bombs = 5
        elif self.difficulté == "Moyen":
            max_bombs = 20
            min_bombs = 10

        elif self.difficulté == "Difficile":
            max_bombs = 30
            min_bombs = 20
        else:
            raise ValueError("Invalid difficulty level. Choose 'easy', 'medium', or 'hard'.")

        num_bombs = random.randint(min_bombs, max_bombs)
        for _ in range(num_bombs):
            x = random.randint(0, len(self.tab)-1)
            y = random.randint(0, len(self.tab[0])-1)
            if not self.tab[x][y].is_bombe:
                self.tab[x][y].is_bombe = True
            
        

