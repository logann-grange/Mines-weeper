import tkinter as tk

class ChoixDifficulté(tk.Frame):
    def __init__ (self,master):
        super().__init__(master)
        self.master = master
        self.master.title("Choix de la difficulté")
        self.master.geometry("400x300")
        self.master.resizable(False, False)
        self.pack()
        self.create_widgets()
    
    def create_widgets(self):
        self.label = tk.Label(self, text="Choisissez la difficulté")
        self.label.pack(pady=20)

        self.button_facile = tk.Button(self, text="Facile", command=self.facile)
        self.button_facile.pack(pady=10)

        self.button_moyen = tk.Button(self, text="Moyen", command=self.moyen)
        self.button_moyen.pack(pady=10)

        self.button_difficile = tk.Button(self, text="Difficile", command=self.difficile)
        self.button_difficile.pack(pady=10)    