class Case :

    def __init__(self, index, discover):
        self.index = index
        self.discover = discover
        self.is_bombe = None
        self.marker = 0 # 0=empty , 1=flag, 2=? 
        self.num = None

    def vérif_num(self, tab) :
        x = self.index[0]
        y = self.index[1]
        count = 0
        for c in [tab[x][y+1], tab[x][y-1],tab[x+1][y], tab[x+1][y+1], tab[x+1][y-1], tab[x-1][y], tab[x-1][y+1], tab[x-1][y-1]] :
            if c.is_bombe :
                count += 1
        self.num = count
        if count > 0 :
            return True
        else :
            return False
    
    def right_clic_on(self) :
        self.marker += 1
        self.marker %= 3

    def discovering(self, tab) :
        x = self.index[0]
        y = self.index[1]
        if self.is_bombe :
            return False
        else :
            self.discover = True
            list_case = [tab[x][y+1], tab[x][y-1],tab[x+1][y], tab[x+1][y+1], tab[x+1][y-1], tab[x-1][y], tab[x-1][y+1], tab[x-1][y-1]]
            for c in list_case :
                if not c.verif_num(tab) :
                    c.discovering(tab)