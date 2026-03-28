import tkinter as tk
from pygame import mixer


class ChoixDifficulte(tk.Frame):
    def __init__(self, master, on_difficulte_chosen=None):
        super().__init__(master, bg="#f0f0f0")
        self.master = master
        self.on_difficulte_chosen = on_difficulte_chosen

        self.master.title("Choix de la difficulte")
        self.master.geometry("400x300")
        self.master.resizable(False, False)

        self.place(relx=0.5, rely=0.5, anchor="center")
        self.create_widgets()
        self.play_musique("menu")

    def create_widgets(self):
        self.canvas = tk.Canvas(self, width=400, height=75, bg="#f0f0f0", highlightthickness=0)
        self.canvas.pack(pady=10)
        self.canvas.create_oval(100, 5, 300, 70, fill="black", outline="black")

        self.image = tk.PhotoImage(file="assets/images/logo.png")
        self.canvas.create_image(200, 40, image=self.image, anchor="center")

        self.label = tk.Label(self, text="Choisissez la difficulte", font=("Arial", 12, "bold"), bg="#f0f0f0")
        self.label.pack(pady=20)

        self.button_facile = tk.Button(
            self,
            text="Facile",
            width=15,
            height=1,
            background="#68d43e",
            command=self.facile,
        )
        self.button_facile.pack(pady=10)

        self.button_moyen = tk.Button(
            self,
            text="Moyen",
            width=15,
            height=1,
            background="#3e89d4",
            command=self.moyen,
        )
        self.button_moyen.pack(pady=10)

        self.button_difficile = tk.Button(
            self,
            text="Difficile",
            width=15,
            height=1,
            background="#d4703e",
            command=self.difficile,
        )
        self.button_difficile.pack(pady=10)

    def facile(self):
        if self.on_difficulte_chosen:
            self.on_difficulte_chosen("Facile")
            mixer.Sound.play(mixer.Sound("assets/sons/bouton.mp3"))
            self.play_musique("game")

    def moyen(self):
        if self.on_difficulte_chosen:
            self.on_difficulte_chosen("Moyen")
            mixer.Sound.play(mixer.Sound("assets/sons/bouton.mp3"))
            self.play_musique("game")

    def difficile(self):
        if self.on_difficulte_chosen:
            self.on_difficulte_chosen("Difficile")
            mixer.Sound.play(mixer.Sound("assets/sons/bouton.mp3"))
            self.play_musique("game")

    def play_musique(self, state):
        mixer.init()
        if state == "menu":
            mixer.music.load("assets/sons/menu.mp3")
        elif state == "game":
            mixer.music.load("assets/sons/musique_fond.mp3")
        mixer.music.play(-1)
