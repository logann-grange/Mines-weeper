class Case :

    def __init__(self, index, discover):
        self.index = index
        self.discover = discover
        self.is_bombe = None
        self.marker = 0 # 0=empty , 1=flag, 2=?
        self.num = None

    # Vérifie le nombre de mines adjacentes à une case :
    def verif_num(self, tab) :
        x = self.index[0]
        y = self.index[1]
        count = 0
        list_case = self.gener_case_adj(tab)
        for c in  list_case:
            if c.is_bombe :
                count += 1
        self.num = count
        if count > 0 :
            return True
        else :
            return False
    
    # Changement des marqueur
    def right_clic_on(self) :
        self.marker += 1
        self.marker %= 3

    # Gère la découverte des cases :
    def discovering(self, tab) :
        if self.is_bombe :
            return False
        else :
            self.discover = True
            x = self.index[0]
            y = self.index[1]
            # definition des cases adjacentes :
            list_case = self.gener_case_adj(tab)
            for c in list_case :
                if not c.verif_num(tab) and not c.discover :
                    c.discovering(tab)
                c.discover = True

    # génération de la liste de cases adjacents
    def gener_case_adj(self, tab) :
        list_case = []
        if self.index[1]-1 >= 0 :
            list_case.append(tab[self.index[0]][self.index[1]-1])
        if self.index[1]+1 < len(tab[0]) :
            list_case.append(tab[self.index[0]][self.index[1]+1])
        if self.index[0]-1 >= 0 :
            list_case.append(tab[self.index[0]-1][self.index[1]])
            if self.index[1]-1 >= 0 :
                list_case.append(tab[self.index[0]-1][self.index[1]-1])
            if self.index[1]+1 < len(tab[0]) :
                list_case.append(tab[self.index[0]-1][self.index[1]+1])
        if self.index[0]+1 < len(tab) :
            list_case.append(tab[self.index[0]+1][self.index[1]])
            if self.index[1]-1 >= 0 :
                list_case.append(tab[self.index[0]+1][self.index[1]-1])
            if self.index[1]+1 < len(tab[0]) :
                list_case.append(tab[self.index[0]+1][self.index[1]+1])
        return list_case