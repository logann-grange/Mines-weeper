class GameLogic:
    #Logique metier du Demineur, independante de l'affichage.

    def __init__(self, tableau):
        self.tableau = tableau
        self.bombes_generees = False
        self.game_is_over = False

    def set_tableau(self, tableau):
        self.tableau = tableau
        self.bombes_generees = False
        self.game_is_over = False

    def _check_win(self):
        for row in self.tableau.tab:
            for case in row:
                if not case.is_bombe and not case.discover:
                    return False
        return True

    def handle_left_click(self, i, j):
        if self.game_is_over:
            return {"status": "ignored", "grid_changed": False}

        if not self.bombes_generees:
            self.tableau.generate_bombes(first_click=(i, j))
            self.bombes_generees = True

        case = self.tableau.tab[i][j]
        if case.discover or case.marker == 1:
            return {"status": "ignored", "grid_changed": False}

        if case.is_bombe:
            self.game_is_over = True
            return {"status": "lose", "grid_changed": False}

        if case.verif_num(self.tableau.tab):
            case.discover = True
        else:
            case.discovering(self.tableau.tab)

        if self._check_win():
            self.game_is_over = True
            return {"status": "win", "grid_changed": True}

        return {"status": "continue", "grid_changed": True}

    def handle_right_click(self, i, j):
        if self.game_is_over:
            return {"status": "ignored", "grid_changed": False, "marker": None}

        case = self.tableau.tab[i][j]
        if case.discover:
            return {"status": "ignored", "grid_changed": False, "marker": None}

        case.right_clic_on()
        return {
            "status": "continue",
            "grid_changed": True,
            "marker": case.marker,
        }