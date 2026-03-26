import tkinter as tk

class ChoixDifficulte(tk.Frame):
    def __init__ (self, master, on_difficulte_chosen=None):
        super().__init__(master, bg="#f0f0f0")
        self.master = master
        self.on_difficulte_chosen = on_difficulte_chosen
        self.master.title("Choix de la difficulté")
        self.master.geometry("400x300")
        self.master.resizable(False, False)
        self.place(relx=0.5, rely=0.5, anchor="center")
        self.create_widgets()
    
    def create_widgets(self):

        self.canvas = tk.Canvas(self, width=400, height=75, bg="#f0f0f0", highlightthickness=0)
        self.canvas.pack(pady=10)
        self.canvas.create_oval(100, 5, 300, 70, fill="black", outline="black")

        # affichage du logo au centre de l'ovale
        self.image = tk.PhotoImage(file="assets/images/logo.png")
        self.canvas.create_image(200, 40, image=self.image, anchor="center")

        self.label = tk.Label(self, text="Choisissez la difficulté")
        self.label.pack(pady=20)

        self.button_facile = tk.Button(self, text="Facile", command=self.facile)
        self.button_facile.pack(pady=10)

        self.button_moyen = tk.Button(self, text="Moyen", command=self.moyen)
        self.button_moyen.pack(pady=10)

        self.button_difficile = tk.Button(self, text="Difficile", command=self.difficile)
        self.button_difficile.pack(pady=10)

    def facile(self):
        if self.on_difficulte_chosen:
            self.on_difficulte_chosen("Facile")

    def moyen(self):
        if self.on_difficulte_chosen:
            self.on_difficulte_chosen("Moyen")

    def difficile(self):
        if self.on_difficulte_chosen:
            self.on_difficulte_chosen("Difficile")    
        
