import tkinter as tk
from JeuDemineur import JeuDemineur
from graphic.choix_difficulté import ChoixDifficulte
from logic.window_config import calculate_window_size


def lancer_jeu(menu_frame, difficulte, root):
	#Lance le jeu quand la difficulté est choisie
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
	menu = ChoixDifficulte(root, on_difficulte_chosen=lambda d: lancer_jeu(menu, d, root))
	root.mainloop()
