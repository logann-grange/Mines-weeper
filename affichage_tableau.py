import tkinter as tk
from generation_tableau import Tableau


class AffichageTableau:
    def __init__(self, difficulté, root=None):
        self.tableau = Tableau(difficulté)
        if root:
            self.root = root
        else:
            self.root = tk.Tk()
        self.root.title(f"Démineur - {self.tableau.difficulté}")
        self.boutons = []
        self.grid_frame = None
        self.on_left_click = None
        self.on_right_click = None
        self.font_size = 10  # Default, will be set in create_grid
        self.create_grid()

    def create_grid(self):
        if self.grid_frame is not None:
            self.grid_frame.destroy()

        self.boutons = []
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Calculer la taille des boutons selon le nombre de cases
        nb_rows = len(self.tableau.tab)
        nb_cols = len(self.tableau.tab[0]) if nb_rows > 0 else 1
        
        # Adapter la taille des boutons et espacement
        # Plus la grille est grande, plus les boutons sont petits
        if nb_cols > 20:  # Difficile (30 colonnes)
            btn_width, btn_height = 3, 1
            self.font_size = 7
            btn_padx, btn_pady = 1, 0
        elif nb_cols > 10:  # Moyen (16 colonnes)
            btn_width, btn_height = 3, 1
            self.font_size = 8
            btn_padx, btn_pady = 1, 0
        else:  # Facile (9 colonnes)
            btn_width, btn_height = 5, 2
            self.font_size = 11
            btn_padx, btn_pady = 1, 1
        
        for i, row in enumerate(self.tableau.tab):
            bouton_row = []
            for j, _ in enumerate(row):
                bouton = tk.Button(
                    self.grid_frame,
                    width=btn_width,
                    height=btn_height,
                    relief="raised",
                    bg="lightgray",
                    font=("Arial", self.font_size, "bold"),
                    command=lambda x=i, y=j: self.click_bouton_left(x, y),
                )
                bouton.bind("<Button-3>", lambda event, x=i, y=j: self.click_bouton_right(x, y))
                bouton.grid(row=i, column=j, padx=btn_padx, pady=btn_pady)
                bouton_row.append(bouton)
            self.boutons.append(bouton_row)

    def reset_tableau(self, difficulté):
        self.tableau = Tableau(difficulté)
        self.root.title(f"Démineur - {self.tableau.difficulté}")
        self.create_grid()

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
        number_colors = {
            1: "blue",
            2: "green",
            3: "red",
            4: "darkblue",
            5: "darkred",
            6: "cyan",
            7: "black",
            8: "gray",
        }

        for i, row in enumerate(self.tableau.tab):
            for j, _ in enumerate(row):
                case = tab[i][j]
                if case.discover:
                    if case.num > 0:
                        number_color = number_colors.get(case.num, "black")
                        self.boutons[i][j].config(
                            text=str(case.num),
                            bg="white",
                            relief="sunken",
                            state="disabled",
                            font=("Arial", self.font_size, "bold"),
                            fg=number_color,
                            disabledforeground=number_color,
                        )
                    else:
                        self.boutons[i][j].config(
                            text="",
                            bg="white",
                            relief="sunken",
                            state="disabled",
                            font=("Arial", self.font_size, "bold"),
                            fg="black",
                            disabledforeground="black",
                        )
                else:
                    if case.marker == 1:
                        self.boutons[i][j].config(
                            text="F",
                            bg="yellow",
                            state="normal",
                            relief="raised",
                            font=("Arial", self.font_size, "bold"),
                        )
                    elif case.marker == 2:
                        self.boutons[i][j].config(
                            text="?",
                            bg="orange",
                            state="normal",
                            relief="raised",
                            font=("Arial", self.font_size, "bold"),
                        )

                    else:
                        self.boutons[i][j].config(
                            text="",
                            bg="lightgray",
                            state="normal",
                            relief="raised",
                            font=("Arial", self.font_size, "bold"),
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
            