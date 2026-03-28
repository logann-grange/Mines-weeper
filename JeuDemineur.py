from affichage_tableau import AffichageTableau
import menu_retry
from choix_difficulté import ChoixDifficulte
from pygame import mixer


class JeuDemineur:
	def __init__(self, difficulte, root=None):
		self.difficulte = difficulte
		self.vue = AffichageTableau(difficulte, root=root)
		self.tableau = self.vue.tableau
		self.bombes_generees = False
		self.game_is_over = False
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

		from main import calculate_window_size
		geometry = calculate_window_size(difficulte)
		self.vue.root.geometry(geometry)
		JeuDemineur(difficulte, root=self.vue.root)

	def check_win(self):
		for row in self.tableau.tab:
			for case in row:
				if not case.is_bombe and not case.discover:
					return False
		return True

	def finir_partie(self, is_win):
		self.game_is_over = True
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
		self.retry_overlay = menu_retry.MenuRetry(
			self.vue.root,
			on_retry=self.reinitialiser_partie,
			on_quit=self.vue.root.destroy,
			message=message,
		)

	def reinitialiser_partie(self):
		self.vue.reset_tableau(self.difficulte)
		self.tableau = self.vue.tableau
		self.bombes_generees = False
		self.game_is_over = False
		self.retry_overlay = None
		self.timer_started = False

	def demarrer_timer_si_necessaire(self):
		if not self.timer_started:
			self.vue.start_timer()
			self.timer_started = True

	def click_gauche(self, i, j):
		mixer.Sound.play(mixer.Sound("assets/sons/left_clic.mp3"))
		if self.game_is_over:
			return
		self.demarrer_timer_si_necessaire()

		if not self.bombes_generees:
			self.tableau.generate_bombes(first_click=(i, j))
			self.bombes_generees = True

		case = self.tableau.tab[i][j]
		if case.discover or case.marker == 1:
			return

		if case.is_bombe:
			self.finir_partie(False)
			return

		if case.verif_num(self.tableau.tab):
			case.discover = True
		else:
			case.discovering(self.tableau.tab)
		self.vue.update_grid(self.tableau.tab)

		if self.check_win():
			self.finir_partie(True)

	def click_droit(self, i, j):
		if self.game_is_over:
			return

		self.demarrer_timer_si_necessaire()

		case = self.tableau.tab[i][j]
		if case.discover:
			return

		case.right_clic_on()
		if case.marker == 1 :
			mixer.Sound.play(mixer.Sound("assets/sons/flag.mp3"))
		if case.marker == 2 :
			mixer.Sound.play(mixer.Sound("assets/sons/interogation.mp3"))
		self.vue.update_grid(self.tableau.tab)

	def run(self):
		self.vue.run()