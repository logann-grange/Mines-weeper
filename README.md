# Projet Demineur (Python / Tkinter)

Jeu Demineur realise en equipe de 3 personnes.

## Apercu

Ce projet est une implementation du Demineur en Python avec interface graphique Tkinter.
Le jeu propose 3 niveaux de difficulte, un timer, des effets sonores, une musique de fond, et une interface de relance en fin de partie.

## Fonctionnalites

- Menu de choix de difficulte (Facile, Moyen, Difficile)
- Grille dynamique selon la difficulte choisie
- Generation aleatoire des bombes
- Premier clic protege (la premiere case ne peut pas etre une bombe)
- Decouverte recursive des zones vides
- Marquage des cases: vide -> drapeau -> interrogation
- Detection de victoire / defaite
- Affichage du temps de partie
- Sons d'action (clic, drapeau, explosion) et musique
- Retour au menu principal et relance rapide

## Technologies utilisees

- Python 3.x
- Tkinter (interface graphique)
- Pillow (PIL) pour le rendu d'images
- Pygame (mixer) pour les sons et musiques

## Arborescence du projet

```text
Projet_demineur/
|- main.py                     # Point d'entree
|- JeuDemineur.py              # Orchestration principale du jeu
|- graphic/
|  |- affichage_tableau.py     # Vue Tkinter, grille, timer, rendu
|  |- choix_difficulté.py      # Ecran de selection de difficulte
|  |- menu_retry.py            # Overlay de fin de partie (rejouer/quitter)
|- logic/
|  |- game_logic.py            # Regles metier (clics, victoire, defaite)
|  |- generation_tableau.py    # Creation de grille et pose des bombes
|  |- case.py                  # Modele d'une case et decouverte recursive
|  |- timer.py                 # Gestion du temps
|  |- window_config.py         # Taille de fenetre selon difficulte
|  |- bomb_generation.py       # Ancien module de generation (non central)
|- assets/
|  |- images/                  # Logo, bombes, icones
|  |- sons/                    # Effets sonores et musiques
```

## Installation

### 1) Cloner le projet

```bash
git clone <url-du-repo>
cd Projet_demineur
```

### 2) Creer et activer un environnement virtuel (recommande)

Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3) Installer les dependances

```bash
pip install pillow pygame
```

## Lancement du jeu

Depuis la racine du projet:

```bash
python main.py
```

## Regles de jeu implementees

- Clic gauche: decouvre une case
- Clic droit: alterne les marqueurs (drapeau puis interrogation puis vide)
- Si une bombe est cliquee: defaite
- Si toutes les cases non-bombes sont decouvertes: victoire
- Le timer demarre au premier clic sur la grille

## Niveaux de difficulte

- Facile: grille 9x9, nombre de bombes aleatoire entre 5 et 10
- Moyen: grille 16x16, nombre de bombes aleatoire entre 10 et 20
- Difficile: grille 16x30, nombre de bombes aleatoire entre 70 et 99

## Equipe projet (3 personnes)

Projet realise en collaboration par 3 etudiants.

Vous pouvez remplacer cette section par:

- Logann Grange
- Clement koch
- Mohamed Mahamoud

## Points d'amelioration possibles

- Ajouter un mode personnalise (taille de grille + nombre de bombes)
- Sauvegarder les meilleurs scores (temps)
- Ajouter des tests unitaires sur la logique metier
- Emballer le jeu en executable (Windows) via PyInstaller

## Notes

- Tkinter est inclus avec la plupart des distributions Python.
- Le projet depend des fichiers presents dans `assets/images` et `assets/sons`.
- Si aucun son ne se lance, verifier la disponibilite du peripherique audio et de `pygame`.
