# Julie LE RAL - CPE - TP4 Casse brique - Interface
# DO TO : finir programme
# - la balle bouge lorsqu'on appuie sur Lancer
# - attention format brique
# - probleme au niveau du bouton lancer


from tkinter import Button, Label, StringVar, Frame
import tkinter as tk
import random as rd
import math as mat


# Création de la fenetre
mafenetre = tk.Tk()
mafenetre.title('Casse brique')
mafenetre.geometry('1800x900')

# Création des boutons quitter et lancer
boutonquitter = Button(mafenetre, text = 'Quitter', bg = 'chocolate2', fg = 'white', width = 6, font = ("Britannic Bold", 16), command = mafenetre.destroy)
boutonquitter.pack(side = 'right', padx = 10)
boutonlancer = Button(mafenetre, text = 'Lancer', bg = 'royalblue2', fg = 'white', width = 6, font = ("Britannic Bold", 16))
boutonlancer.pack(side = 'left', padx = 10)

frame_haut = Frame(mafenetre)
frame_haut.pack(side = 'top', fill = 'x')

# Affichage du titre du jeu
labeltitre = Label(frame_haut, text = 'CASSE BRIQUE', fg = 'Black', font = ("Britannic Bold", 30))
labeltitre.pack(padx = 3, pady = 3)
labeltitre.place(x = 500, y = 40)

# Affichage du score et du nombre de vie
score = StringVar()
score.set("Score ->")
labelscore = Label(frame_haut, textvariable = score, height = 2, width = 10, font = ("Calibri", 20))
labelscore.pack(side = 'right', padx = 10, pady = 10)
vie = StringVar()
vie.set("Vie ->")
labelvie = Label(frame_haut, textvariable = vie, height = 2, width = 10, font = ("Calibri", 20))
labelvie.pack(side = 'left', padx = 10, pady = 10)

# Création du cadre du jeu
canvas = tk.Canvas(mafenetre, bg = 'black', width = 1200, height = 700)
canvas.pack(fill = 'both')


class Brique() : 
    def __init__(self, canvas, x, y, largeur, hauteur, couleur) :
    # fonction qui permet d'initialiser les brique
    # entrée : le canvas, la taille du cadre et la couleur
    # sortie : les briques
        self.canvas = canvas
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur
        self.id = self.canvas.create_rectangle(x, y, x + largeur, y + hauteur, fill = couleur, outline = 'black')

    def CreationBriques(canvas, lignes, couleur) :
    # fonction qui permet de créée les briques du jeux
    # entrée : le canvas, le nombre de ligne et la couleur
    # sortie : création des briques
        nb_briques_par_ligne = 8
        larg_brique = 170 #canvas_width // nb_briques_par_ligne
        haut_brique = 50
        debligne = 3 # nombre de pixels avant la première ligne
        for x in range(lignes): 
            row = debligne + (haut_brique * x)
            for y in range(nb_briques_par_ligne) :
                col = y * larg_brique
                canvas.create_rectangle(col, row, col + larg_brique, row + haut_brique, fill = couleur, outline = 'black')

Brique.CreationBriques(canvas, 7, "darkorchid4")


class raquette() : 
    def __init__(self,canvas) :
    # fonction qui permet d'initialiser la raquette
    # entrée : le canvas
    # sortie : la raquette
        self.canvas = canvas
        self.dx = 20
        posx = 650
        posy = 653
        self.raquette = canvas.create_rectangle(posx - 50, posy - 10, posx + 50, posy + 10, width = 2, fill='white')
        self.canvas.focus_set() # permet de capter les touches
        self.canvas.bind_all('<Left>', self.gauche)
        self.canvas.bind_all('<Right>', self.droite)

    def gauche(self, event) :
        # fonction qui permet de déplacer la raquette vers la gauche en utilisant le clavier
        # entrée : 
        # sortie : la raquette bouge
            coords = self.canvas.coords(self.raquette)
            if coords[0] > 0:  
                self.canvas.move(self.raquette, -self.dx, 0)

    def droite(self, event) : 
    # fonction qui permet de déplacer la raquette vers la droite en utilisant le clavier
    # entrée : 
    # sortie : la raquette bouge    
        coords = self.canvas.coords(self.raquette)
        if coords[0] < 1250 :   
            self.canvas.move(self.raquette, self.dx, 0)

maraquette = raquette(canvas)


largeur = 1340
hauteur = 700
rayon = 15
x = largeur/2
y = hauteur/2
vitesse = rd.uniform (2, 2) * 5
angle = rd.uniform(0 , 2 * mat.pi)
dx = vitesse * mat.cos(angle)
dy = vitesse * mat.sin(angle)

class ball() :
    def __init__(self, canvas, couleur) :
        self.canvas = canvas
        self.rayon = rayon
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur 
        self.id = self.canvas.create_oval(x - rayon, y - rayon, x + rayon, y + rayon, width = 1, outline = 'white', fill = 'white')

balle = canvas.create_oval(x - rayon , y - rayon , x + rayon , y + rayon , width = 1, outline = 'white', fill = 'white')


def collision() : 
    a1x, a1y, a2x, a2y = canvas.bbox(maraquette)
    b1x, b1y, b2x, b2y = canvas.bbox(balle)
    if a1x <= b1x <= a2x and a1y <= b1y <= a2y :

    if a1x <= b2x <= a2x and a1y <= b2y <= a2y :

    if a1y <= b1y <= a2y and a1y <= b1x <= a2x :

    if a1y <= b1y <= a2y and a1y <= b1x <= a2x :




def  deplacement() :
# fonction qui permet que la balle se déplace
# entrée : aucune
# sortie : la balle se déplace
    global x, y, dx, dy, rayon, largeur, hauteur
    if x + rayon + dx > largeur :
        x = 2 * (largeur - rayon ) - x
        dx = - dx
    if  x - rayon + dx < 0 :
        x = 2 * rayon - x
        dx = - dx
    if  y + rayon + dy > hauteur :
        y = 2 * (hauteur - rayon ) - y
        dy = - dy 
    if  y - rayon + dy < 0 :
        y = 2 * rayon - y
        dy = - dy
    x = x + dx
    y = y + dy
    canvas.coords(balle, x - rayon, y - rayon, x + rayon, y + rayon)
    mafenetre.after(20, deplacement)

deplacement()








mafenetre.mainloop()