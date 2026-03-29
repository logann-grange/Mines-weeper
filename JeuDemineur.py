from graphic.affichage_tableau import AffichageTableau
from graphic.menu_retry import MenuRetry
from graphic.choix_difficulté import ChoixDifficulte
from pygame import mixer
from logic.game_logic import GameLogic
from logic.window_config import calculate_window_size


class JeuDemineur:
	def __init__(self, difficulte, root=None):
		self.difficulte = difficulte
		self.vue = AffichageTableau(difficulte, root=root)
		self.tableau = self.vue.tableau
		self.logic = GameLogic(self.tableau)
		self.retry_overlay = None
		self.timer_started = False

		self.vue.set_click_handlers(
			on_left_click=self.click_gauche,
			on_right_click=self.click_droit,
		)
		self.vue.set_menu_handler(self.retour_au_menu)

	def retour_au_menu(self):
		if self.retry_overlay is not None:
			self.retry_overlay.destroy()
			self.retry_overlay = None

		if self.timer_started:
			self.vue.stop_timer()
			self.timer_started = False

		for widget in self.vue.root.winfo_children():
			widget.destroy()

		self.vue.root.geometry("400x300")
		self.vue.root.title("Démineur")
		self.vue.root.resizable(False, False)

		ChoixDifficulte(
			self.vue.root,
			on_difficulte_chosen=lambda d: self.relancer_depuis_menu(d),
		)

	def relancer_depuis_menu(self, difficulte):
		for widget in self.vue.root.winfo_children():
			widget.destroy()

		geometry = calculate_window_size(difficulte)
		self.vue.root.geometry(geometry)
		JeuDemineur(difficulte, root=self.vue.root)

	def finir_partie(self, is_win):
		self.logic.game_is_over = True
		temps_final = self.vue.stop_timer() if self.timer_started else 0
		if not is_win:
			mixer.Sound.play(mixer.Sound("assets/sons/boom.wav"))
			self.vue.afficher_defaite(self.tableau.tab)
			self.vue.set_title_state("Perdu")
			message = f"Perdu en {temps_final:.2f} s. Voulez-vous rejouer ?"
		else:
			self.vue.set_title_state("Gagne")
			message = f"Gagne en {temps_final:.2f} s. Voulez-vous rejouer ?"
		self.vue.disable_all_buttons()
		self.retry_overlay = MenuRetry(
			self.vue.root,
			on_retry=self.reinitialiser_partie,
			on_quit=self.vue.root.destroy,
			message=message,
		)

	def reinitialiser_partie(self):
		self.vue.reset_tableau(self.difficulte)
		self.tableau = self.vue.tableau
		self.logic.set_tableau(self.tableau)
		self.retry_overlay = None
		self.timer_started = False

	def demarrer_timer_si_necessaire(self):
		if not self.timer_started:
			self.vue.start_timer()
			self.timer_started = True

	def click_gauche(self, i, j):
		mixer.Sound.play(mixer.Sound("assets/sons/left_clic.mp3"))
		self.demarrer_timer_si_necessaire()

		result = self.logic.handle_left_click(i, j)
		if result["status"] == "lose":
			self.finir_partie(False)
			return

		if result["grid_changed"]:
			self.vue.update_grid(self.tableau.tab)

		if result["status"] == "win":
			self.finir_partie(True)

	def click_droit(self, i, j):
		self.demarrer_timer_si_necessaire()

		result = self.logic.handle_right_click(i, j)
		if not result["grid_changed"]:
			return

		if result["marker"] == 1:
			mixer.Sound.play(mixer.Sound("assets/sons/flag.mp3"))
		if result["marker"] == 2:
			mixer.Sound.play(mixer.Sound("assets/sons/interogation.mp3"))
		self.vue.update_grid(self.tableau.tab)

	def run(self):
		self.vue.run()