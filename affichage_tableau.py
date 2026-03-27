import tkinter as tk
import os
from generation_tableau import Tableau
from PIL import Image, ImageDraw, ImageTk
from timer import Timer


class AffichageTableau:
    def __init__(self, difficulté, root=None):
        self.tableau = Tableau(difficulté)
        if root:
            self.root = root
        else:
            self.root = tk.Tk()
        self.root.title(f"Démineur - {self.tableau.difficulté}")
        self.boutons = []
        self.grid_frame = None
        self.on_left_click = None
        self.on_right_click = None
        self.on_menu_click = None
        self.font_size = 10  # Default, will be set in create_grid
        self.timer = Timer(0)
        self.timer_running = False
        self.timer_job = None
        self.header_frame = None
        self.timer_label = None
        self._bomb_photo_images = []
        image_dir = os.path.join(os.path.dirname(__file__), "asset", "image")
        self.bomb_image_path = os.path.join(image_dir, "bombe_clean.png")
        self.bomb_image_fallback_path = os.path.join(image_dir, "bombe.png")
        self._bomb_source_image = None
        self.show_bombs = False
        self.create_header()
        self.create_grid()

    def create_header(self):
        if self.header_frame is not None:
            self.header_frame.destroy()

        self.header_frame = tk.Frame(self.root)
        self.header_frame.pack(padx=10, pady=(10, 0), fill=tk.X)

        self.timer_label = tk.Label(
            self.header_frame,
            text="Temps: 0.00 s",
            font=("Arial", 12, "bold"),
            anchor="w",
        )
        self.timer_label.pack(side=tk.LEFT)

        self.menu_button = tk.Button(
            self.header_frame,
            text="Retour au menu",
            font=("Arial", 10, "bold"),
            command=self.click_menu,
        )
        self.menu_button.pack(side=tk.RIGHT)

    def click_menu(self):
        if self.on_menu_click is not None:
            self.on_menu_click()

    def _load_bomb_source_image(self):
        if self._bomb_source_image is not None:
            return self._bomb_source_image

        image_path = self.bomb_image_path
        if not os.path.exists(image_path):
            image_path = self.bomb_image_fallback_path
        if not os.path.exists(image_path):
            return None

        try:
            image = Image.open(image_path).convert("RGBA")
            alpha_bbox = image.split()[-1].getbbox()
            if alpha_bbox:
                image = image.crop(alpha_bbox)
            self._bomb_source_image = image
            return self._bomb_source_image
        except Exception:
            return None

    def _create_bomb_canvas(self, parent, width, height):
        width = max(12, int(width))
        height = max(12, int(height))

        canvas = tk.Canvas(
            parent,
            width=width,
            height=height,
            bg="#ffb3b3",
            highlightthickness=0,
            bd=0,
            relief="sunken",
        )

        source = self._load_bomb_source_image()
        if source is not None:
            target_w = max(8, width - 2)
            target_h = max(8, height - 2)
            if hasattr(Image, "Resampling"):
                resample = Image.Resampling.LANCZOS
            else:
                resample = Image.LANCZOS
            resized = source.resize((target_w, target_h), resample)
            photo = ImageTk.PhotoImage(resized)
            canvas.create_image(width // 2, height // 2, image=photo, anchor="center")
            canvas.image_ref = photo
            self._bomb_photo_images.append(photo)
        else:
            # Fallback visuel si l'image n'est pas trouvée.
            margin_x = max(1, width // 14)
            margin_y = max(1, height // 14)
            left = margin_x
            right = width - margin_x
            top = margin_y + max(1, height // 10)
            bottom = height - margin_y
            canvas.create_oval(left, top, right, bottom, fill="#1c1c20", outline="")

        return canvas

    def create_grid(self):
        if self.grid_frame is not None:
            self.grid_frame.destroy()

        self.show_bombs = False
        self.boutons = []
        self.grid_frame = tk.Frame(self.root)
        self.grid_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Calculer la taille des boutons selon le nombre de cases
        nb_rows = len(self.tableau.tab)
        nb_cols = len(self.tableau.tab[0]) if nb_rows > 0 else 1
        
        # Adapter la taille des boutons et espacement
        # Plus la grille est grande, plus les boutons sont petits
        if nb_cols > 20:  # Difficile (30 colonnes)
            btn_width, btn_height = 2, 1
            self.font_size = 7
            btn_padx, btn_pady = 1, 1
        elif nb_cols > 10:  # Moyen (16 colonnes)
            btn_width, btn_height = 3, 1
            self.font_size = 8
            btn_padx, btn_pady = 1, 0
        else:  # Facile (9 colonnes)
            btn_width, btn_height = 5, 2
            self.font_size = 11
            btn_padx, btn_pady = 1, 1

        for i, row in enumerate(self.tableau.tab):
            bouton_row = []
            for j, _ in enumerate(row):
                bouton = tk.Button(
                    self.grid_frame,
                    width=btn_width,
                    height=btn_height,
                    relief="raised",
                    bg="lightgray",
                    font=("Arial", self.font_size, "bold"),
                    command=lambda x=i, y=j: self.click_bouton_left(x, y),
                )
                bouton.bind("<Button-3>", lambda event, x=i, y=j: self.click_bouton_right(x, y))
                bouton.grid(row=i, column=j, padx=btn_padx, pady=btn_pady)
                bouton_row.append(bouton)
            self.boutons.append(bouton_row)


    def reset_tableau(self, difficulté):
        self.tableau = Tableau(difficulté)
        self.root.title(f"Démineur - {self.tableau.difficulté}")
        self.reset_timer()
        self.root.unbind("<Configure>")
        if hasattr(self, '_bomb_photo_images'):
            self._bomb_photo_images.clear()
        self.create_grid()

    def set_click_handlers(self, on_left_click=None, on_right_click=None):
        self.on_left_click = on_left_click
        self.on_right_click = on_right_click

    def set_menu_handler(self, on_menu_click=None):
        self.on_menu_click = on_menu_click

    def click_bouton_left(self, i, j):
        if self.on_left_click is not None:
            #if not first_click:
            #    self.timer.start()
            self.on_left_click(i, j)

    def click_bouton_right(self, i, j):
        if self.on_right_click is not None:
            self.on_right_click(i, j)

    def update_grid(self, tab):
        # Quand la partie est perdue, l'affichage est fige par afficher_defaite.
        if self.show_bombs:
            return

        number_colors = {
            1: "blue",
            2: "green",
            3: "red",
            4: "darkblue",
            5: "darkred",
            6: "cyan",
            7: "black",
            8: "gray",
        }

        for i, row in enumerate(self.tableau.tab):
            for j, _ in enumerate(row):
                case = tab[i][j]
                if case.discover:
                    if case.num is not None and case.num > 0:
                        number_color = number_colors.get(case.num, "black")
                        self.boutons[i][j].config(
                            text=str(case.num),
                            bg="white",
                            relief="sunken",
                            state="disabled",
                            font=("Arial", self.font_size, "bold"),
                            fg=number_color,
                            disabledforeground=number_color,
                        )
                    else:
                        self.boutons[i][j].config(
                            text="",
                            bg="white",
                            relief="sunken",
                            state="disabled",
                            font=("Arial", self.font_size, "bold"),
                            fg="black",
                            disabledforeground="black",
                        )
                else:
                    if case.marker == 1:
                        self.boutons[i][j].config(
                            text="F",
                            bg="yellow",
                            state="normal",
                            relief="raised",
                            font=("Arial", self.font_size, "bold"),
                        )
                    elif case.marker == 2:
                        self.boutons[i][j].config(
                            text="?",
                            bg="orange",
                            state="normal",
                            relief="raised",
                            font=("Arial", self.font_size, "bold"),
                        )

                    else:
                        self.boutons[i][j].config(
                            text="",
                            bg="lightgray",
                            state="normal",
                            relief="raised",
                            font=("Arial", self.font_size, "bold"),
                        )

    def afficher_defaite(self, tab):
        self.show_bombs = True

        # Marquer toutes les bombes comme découvertes
        for i, row in enumerate(tab):
            for j, case in enumerate(row):
                if case.is_bombe:
                    case.discover = True

        # Mettre a jour les tailles reelles des boutons avant le rendu final.
        self.root.update_idletasks()

        # Rendu final fige: bombes visibles, autres cases desactivees.
        self._bomb_photo_images = []
        for i, row in enumerate(tab):
            for j, case in enumerate(row):
                if case.is_bombe:
                    btn = self.boutons[i][j]
                    btn_w = btn.winfo_width()
                    btn_h = btn.winfo_height()

                    # Si Tk n'a pas encore finalise la taille, utiliser la taille requise.
                    if btn_w <= 2 or btn_h <= 2:
                        btn_w = btn.winfo_reqwidth()
                        btn_h = btn.winfo_reqheight()

                    info = btn.grid_info()
                    padx = info.get("padx", 0)
                    pady = info.get("pady", 0)
                    btn.destroy()

                    bomb_canvas = self._create_bomb_canvas(self.grid_frame, btn_w, btn_h)
                    bomb_canvas.grid(row=i, column=j, padx=padx, pady=pady)
                    self.boutons[i][j] = bomb_canvas
                else:
                    self.boutons[i][j].config(state="disabled")
    
    def set_title_state(self, state):
        self.root.title(f"Démineur - {self.tableau.difficulté} - {state}")

    def disable_all_buttons(self):
        for row in self.boutons:
            for bouton in row:
                bouton.config(state="disabled")

    def disable_non_bomb_buttons(self, tab):
        for i, row in enumerate(tab):
            for j, case in enumerate(row):
                if not case.is_bombe:
                    self.boutons[i][j].config(state="disabled")

    def run(self):
        self.root.mainloop()

    def _update_timer_label(self):
        if not self.timer_running:
            return

        elapsed = self.timer.ecoulement()
        self.timer_label.config(text=f"Temps: {elapsed:.2f} s")
        self.timer_job = self.root.after(100, self._update_timer_label)

    def start_timer(self):
        if self.timer_running:
            return
        self.timer.start()
        self.timer_running = True
        self._update_timer_label()

    def stop_timer(self):
        if self.timer_job is not None:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None

        self.timer_running = False
        elapsed = self.timer.stop()
        self.timer_label.config(text=f"Temps: {elapsed:.2f} s")
        return elapsed

    def reset_timer(self):
        if self.timer_job is not None:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None

        self.timer_running = False
        self.timer = Timer(0)
        if self.timer_label is not None:
            self.timer_label.config(text="Temps: 0.00 s")
            