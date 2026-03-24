from affichage_tableau import AffichageTableau


class JeuDemineur:
	def __init__(self, difficulte):
		self.vue = AffichageTableau(difficulte)
		self.tableau = self.vue.tableau
		self.bombes_generees = False
		self.game_is_over = False

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
			self.vue.afficher_defaite(self.tableau.tab)
			self.vue.set_title_state("Perdu")
		else:
			self.vue.set_title_state("Gagne")
		self.vue.disable_all_buttons()

	def click_gauche(self, i, j):
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

		if case.vérif_num(self.tableau.tab):
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
		self.vue.update_grid(self.tableau.tab)

	def run(self):
		self.vue.run()


if __name__ == "__main__":
	jeu = JeuDemineur("Difficile")
	jeu.run()
