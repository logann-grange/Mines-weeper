from affichage_tableau import AffichageTableau
import menu_retry
from playsound import playsound

class JeuDemineur:
	def __init__(self, difficulte, root=None):
		self.difficulte = difficulte
		self.vue = AffichageTableau(difficulte, root=root)
		self.tableau = self.vue.tableau
		self.bombes_generees = False
		self.game_is_over = False
		self.retry_overlay = None

		self.vue.set_click_handlers(
			on_left_click=self.click_gauche,
			on_right_click=self.click_droit,
		)

	def check_win(self):
		for row in self.tableau.tab:
			for case in row:
				if not case.is_bombe and not case.discover:
					return False
		return True

	def finir_partie(self, is_win):
		self.game_is_over = True
		if not is_win:
			playsound("assets/sons/boom.wav", block=False)
			self.vue.afficher_defaite(self.tableau.tab)
			self.vue.set_title_state("Perdu")
			message = "Perdu. Voulez-vous rejouer ?"
		else:
			self.vue.set_title_state("Gagne")
			message = "Gagne. Voulez-vous rejouer ?"
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

	def click_gauche(self, i, j):
		playsound("assets/sons/left_clic.mp3", block=False) # changerle son (bloc mc ?)
		if self.game_is_over:
			return

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

		case = self.tableau.tab[i][j]
		if case.discover:
			return

		case.right_clic_on()
		if case.marker == 1 :
			playsound("assets/sons/flag.mp3", block=False)
		if case.marker == 2 :
			playsound("assets/sons/interogation.mp3", block=False)  #a changer
		self.vue.update_grid(self.tableau.tab)

	def run(self):
		self.vue.run()