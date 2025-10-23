# Julie LE RAL / Nour TRABELSI - CPE - TP4 Casse brique

import tkinter as tk
from classe_principale import principale
from classe_brique import brique
from classe_raquette import raquette
from classe_balle import balle

# Création de la fenetre
mafenetre = tk.Tk()
mafenetre.title("Casse Brique")
mafenetre.geometry('1800x900')

mafenetre = principale(mafenetre, brique, raquette, balle)

mafenetre.mainloop()