import tkinter as tk
import generation_tableau 

class AffichageTableau:
    def __init__(self,tableau):
        self.tableau = tableau
        self.root = tk.Tk()
        self.root.title(f"Démineur - {self.tableau.difficulté}")
        self.boutons = []
        self.create_grid()
        
    def create_grid(self):
        frame= tk.Frame(self.root)
        frame.pack(padx=5, pady=5)
        for i,row in enumerate(self.tableau.tab):
            bouton_row = []
            for j,case in enumerate(row):
                bouton = tk.Button(frame, width=3, height=1, relief="raised",bg="lightgray")
                bouton.grid(row=i, column=j, padx=1, pady=1)
                bouton_row.append(bouton)
            self.boutons.append(bouton_row)
            
    
               
