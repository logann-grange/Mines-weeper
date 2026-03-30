import tkinter as tk
from graphic.choix_difficulté import ChoixDifficulte
from logic.window_config import calculate_window_size

class MenuRetry:
    def __init__(self, parent, on_retry, on_quit=None, message="Voulez-vous rejouer ?", on_return_to_menu=None):
        self.parent = parent
        self.on_retry = on_retry
        self.on_quit = on_quit
        self.on_return_to_menu = on_return_to_menu
        self.overlay = None
        self.message = message
        self.create_menu()

    def create_menu(self):
        self.overlay = tk.Frame(self.parent, bg="#f5f5f5", bd=2, relief="ridge")
        self.overlay.place(relx=0.5, rely=0.5, anchor="center")

        label = tk.Label(self.overlay, text=self.message, font=("Arial", 14), bg="#f5f5f5")
        label.pack(padx=20, pady=(15, 10))

        button_frame = tk.Frame(self.overlay, bg="#f5f5f5")
        button_frame.pack(pady=(0, 15))

        yes_button = tk.Button(button_frame, text="Oui", width=10, command=self.replay)
        yes_button.grid(row=0, column=0, padx=10)

        no_button = tk.Button(button_frame, text="Retour au menu", width=13, command=self.quit_game)
        no_button.grid(row=0, column=1, padx=10)

    def replay(self):
        self.destroy()
        self.on_retry()

    def quit_game(self):
        self.destroy()
        # Nettoyer tous les widgets du jeu
        for widget in self.parent.winfo_children():
            widget.destroy()
        
        # Remettre la fenêtre aux dimensions du menu
        self.parent.geometry("400x300")
        self.parent.title("Démineur")
        
        # Réafficher le menu de difficulté
        menu = ChoixDifficulte(self.parent, on_difficulte_chosen=self.retourner_au_jeu)
    
    def retourner_au_jeu(self, difficulte):
        #Fonction de callback pour rejouer avec une nouvelle difficulté
        # Détruire le menu de difficulté
        for widget in self.parent.winfo_children():
            widget.destroy()
        
        from JeuDemineur import JeuDemineur
        geometry = calculate_window_size(difficulte)
        self.parent.geometry(geometry)
        jeu = JeuDemineur(difficulte, root=self.parent)

    def destroy(self):
        if self.overlay is not None:
            self.overlay.destroy()
            self.overlay = None