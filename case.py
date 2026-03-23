class Case :

    def __init__(self, index, is_bombe, discover, marker):
        self.index = index
        self.discover = discover
        self.is_bombe = is_bombe
        self.marker = marker # 0=empty , 1=flag, 2=? 
        self.num = None

    def vérif_num(self, tab) :
        x = self.index[0]
        y = self.index[1]
        count = 0
        for c in [tab[x][y+1], tab[x][y-1],tab[x+1][y], tab[x+1][y+1], tab[x+1][y-1], tab[x-1][y], tab[x-1][y+1], tab[x-1][y-1]] :
            if not c.is_bombe :
                count += 1
        self.num = count
    
    def right_clic_on(self) :
        self.marker += 1
        self.marker %= 3

    #def left_clic_on(self) :



        