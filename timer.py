import time

class Timer:

    def __init__(self, temps):
        self.temps=temps
        
    def start(self):
        self.depart=time.time()
        return self.ecoulement(self.depart)
        
    def ecoulement(self,depart):    
        self.temps=time.time()-self.depart
        return self.temps

    def stop(self):
        self.temps_final = int((time.time() - self.depart)*100)
        return self.temps_final/100
    
    def afficher(self):
        return int(self.temps)


"""
fenetre.bind("<Button-1>",start()) #pour lancer le timer au clic de souris

if win==True: #pour arreter le timer
    print(f"Vous avez mis {Timer.stop()} secondes")

    
#===TESTS===#    
tim=Timer(0)
i=0
tim.start()
while i<5000000:
    tim.ecoulement(tim.depart)
    i+=1
    print(tim.afficher())
print(f"Vous avez mis {tim.stop()} secondes")
"""