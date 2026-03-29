from logic.case import Case
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
                    self.tab[i].append(Case((i,j), False))
        elif self.difficulté == "Moyen" :
            for i in range(16) :
                self.tab.append([])
                for j in range(16) :
                    self.tab[i].append(Case((i,j), False))
        else :
            for i in range(16) :
                self.tab.append([])
                for j in range(30) :
                    self.tab[i].append(Case((i,j), False))
                    
    
    def generate_bombes(self, first_click=None):
        if self.difficulté == "Facile":
            max_bombs = 10
            min_bombs = 5
        elif self.difficulté == "Moyen":
            max_bombs = 20
            min_bombs = 10

        elif self.difficulté == "Difficile":
            max_bombs = 99
            min_bombs = 70

        num_bombs = random.randint(min_bombs, max_bombs)
        positions = []
        for x in range(len(self.tab)):
            for y in range(len(self.tab[0])):
                if first_click is not None and (x, y) == first_click:
                    continue
                positions.append((x, y))

        random.shuffle(positions)
        for x, y in positions[:num_bombs]:
            self.tab[x][y].is_bombe = True
            
    def reset_tableau(self):
        for row in self.tab:
            for case in row:
                case.is_bombe = None
                case.discover = False
                case.marker = 0
                case.num = None
    
    def is_victory(self):
        for row in self.tab:
            for case in row:
                if not case.is_bombe and not case.discover:
                    return False
        return True                    
            
        

