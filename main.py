import tkinter as tk
from JeuDemineur import JeuDemineur
from choix_difficulté import ChoixDifficulte
from playsound import playsound


def calculate_window_size(difficulte):
	"""Calcule la taille optimale de la fenêtre selon la difficulté"""
	# Tailles fixes générales selon la difficulté
	if difficulte == "Facile":
		return "550x550"
	elif difficulte == "Moyen":
		return "650x650"
	else:  # Difficile
		return "940x380"


def lancer_jeu(menu_frame, difficulte, root):
	"""Lance le jeu quand la difficulté est choisie"""
	menu_frame.destroy()
	geometry = calculate_window_size(difficulte)
	root.geometry(geometry)
	root.resizable(False, False)
	jeu = JeuDemineur(difficulte, root=root)


if __name__ == "__main__":
	root = tk.Tk()
	root.title("Démineur")
	root.geometry("400x300")
	root.resizable(False, False)
	playsound("assets/sons/musique_fond.mp3", block=False)
	menu = ChoixDifficulte(root, on_difficulte_chosen=lambda d: lancer_jeu(menu, d, root))
	root.mainloop()
