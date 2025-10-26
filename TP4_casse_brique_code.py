# Julie LE RAL / Nour TRABELSI - CPE - TP4 Casse brique - 09/10/2025

import tkinter as tk
from classe_principale import Principale
from classe_briques import Brique
from classe_raquette import Raquette
from classe_balle import Balle

# Programme principal
mafenetre = tk.Tk()
mafenetre.title("Casse Brique")
mafenetre.geometry('1800x900')
jeu = Principale(mafenetre, Brique, Raquette, Balle)

mafenetre.mainloop()