import tkinter as tk
from generation_tableau import Tableau


class AffichageTableau:
    def __init__(self, difficulté):
        self.tableau = Tableau(difficulté)
        self.root = tk.Tk()
        self.root.title(f"Démineur - {self.tableau.difficulté}")
        self.boutons = []
        self.on_left_click = None
        self.on_right_click = None
        self.create_grid()

    def create_grid(self):
        frame = tk.Frame(self.root)
        frame.pack(padx=5, pady=5)
        for i, row in enumerate(self.tableau.tab):
            bouton_row = []
            for j, _ in enumerate(row):
                bouton = tk.Button(
                    frame,
                    width=3,
                    height=1,
                    relief="raised",
                    bg="lightgray",
                    command=lambda x=i, y=j: self.click_bouton_left(x, y),
                )
                bouton.bind("<Button-3>", lambda event, x=i, y=j: self.click_bouton_right(x, y))
                bouton.grid(row=i, column=j, padx=1, pady=1)
                bouton_row.append(bouton)
            self.boutons.append(bouton_row)

    def set_click_handlers(self, on_left_click=None, on_right_click=None):
        self.on_left_click = on_left_click
        self.on_right_click = on_right_click

    def click_bouton_left(self, i, j):
        if self.on_left_click is not None:
            self.on_left_click(i, j)

    def click_bouton_right(self, i, j):
        if self.on_right_click is not None:
            self.on_right_click(i, j)

    def update_grid(self, tab):
        for i, row in enumerate(self.tableau.tab):
            for j, _ in enumerate(row):
                case = tab[i][j]
                if case.discover:
                    if case.num > 0:
                        self.boutons[i][j].config(
                            text=str(case.num),
                            bg="white",
                            relief="sunken",
                            state="disabled",
                        )
                    else:
                        self.boutons[i][j].config(
                            text="",
                            bg="white",
                            relief="sunken",
                            state="disabled",
                        )
                else:
                    if case.marker == 1:
                        self.boutons[i][j].config(
                            text="F",
                            bg="yellow",
                            state="normal",
                            relief="raised",
                        )
                    elif case.marker == 2:
                        self.boutons[i][j].config(
                            text="?",
                            bg="orange",
                            state="normal",
                            relief="raised",
                        )
                    else:
                        self.boutons[i][j].config(
                            text="",
                            bg="lightgray",
                            state="normal",
                            relief="raised",
                        )

    def afficher_defaite(self, tab):
        for i, row in enumerate(tab):
            for j, case in enumerate(row):
                if case.is_bombe:
                    self.boutons[i][j].config(text="B", bg="red")

    def set_title_state(self, state):
        self.root.title(f"Démineur - {self.tableau.difficulté} - {state}")

    def disable_all_buttons(self):
        for row in self.boutons:
            for bouton in row:
                bouton.config(state="disabled")

    def run(self):
        self.root.mainloop()
       
            
    
               
