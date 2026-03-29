def calculate_window_size(difficulte):
    """Calcule la taille optimale de la fenetre selon la difficulte."""
    if difficulte == "Facile":
        return "550x550"
    elif difficulte == "Moyen":
        return "550x480"
    return "740x400"
