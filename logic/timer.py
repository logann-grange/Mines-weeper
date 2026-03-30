import time

class Timer:

    def __init__(self, temps):
        self.temps = temps
        self.depart = None
        
    def start(self):
        self.depart = time.time()
        self.temps = 0
        return self.temps
        
    def ecoulement(self):
        if self.depart is None:
            return 0
        self.temps = time.time() - self.depart
        return self.temps

    def stop(self):
        if self.depart is None:
            return 0
        self.temps_final = int((time.time() - self.depart) * 100)
        self.depart = None
        self.temps = self.temps_final / 100
        return self.temps
    
    def afficher(self):
        return int(self.ecoulement())


