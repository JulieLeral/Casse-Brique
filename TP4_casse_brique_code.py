# Julie LE RAL - CPE - TP4 Casse brique - Interface

from tkinter import Button, Label, StringVar, Frame
import tkinter as tk
import random as rd
import TP4_casse_brique_briques as tp


def NouveauLance() :
    # fonction qui permet de mettre à jour le texte affiché dans l’interface graphique
    # entrée : aucune
    # sortie : mise a jour du résultat
    global Texte 
    nb = rd.randint(1,6)
    Texte.set('Résultat ->' + str(nb))

mafenetre = tk.Tk()
mafenetre.title('Casse brique')
mafenetre.geometry('1800x900')


boutonlancer = Button(mafenetre, text = 'Lancer', bg = 'blue', fg = 'white', width = 6, font = ("Arial", 24), command = NouveauLance)
boutonlancer.pack(side = 'left', padx = 10)

boutonquitter = Button(mafenetre, text = 'Quitter', bg = 'red', fg = 'white', width = 6, font = ("Arial", 24), command = mafenetre.destroy)
boutonquitter.pack(side = 'right', padx = 10)


frame_haut = Frame(mafenetre)
frame_haut.pack(side='top', fill='x')

Score = StringVar()
Score.set("Score ->")
LabelScore = Label(frame_haut, textvariable=Score, height=2, width=10, font=("Arial", 24))
LabelScore.pack(side='right', padx=10, pady=10)

Vie = StringVar()
Vie.set("Vie ->")
LabelVie = Label(frame_haut, textvariable=Vie, height=2, width=10, font=("Arial", 24))
LabelVie.pack(side='left', padx=10, pady=10)

canvas = tk.Canvas(mafenetre, bg='black', width=1200, height=700)
canvas.pack(fill='both', expand=True, padx=20, pady=20)

brique1 = tp.Brique(canvas, 100, 100, 80, 30, "red")
brique2 = tp.Brique(canvas, 200, 100, 80, 30, "blue")

mafenetre.mainloop()