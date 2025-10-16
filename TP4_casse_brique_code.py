# Julie LE RAL / Nour TRABELSI - CPE - TP4 Casse brique
# DO TO : finir programme
# - collisition brique et balle
# - faire les vies et le score


from tkinter import Button, Label, StringVar, Frame
import tkinter as tk
import random as rd
import math as mat


# Création de la fenetre
mafenetre = tk.Tk()
mafenetre.title('Casse brique')
mafenetre.geometry('1800x900')

frame_haut = Frame(mafenetre)
frame_haut.pack(side = 'top', fill = 'x')

# Affichage du titre du jeu
labeltitre = Label(frame_haut, text = 'CASSE BRIQUE', fg = 'Black', font = ("Britannic Bold", 30))
labeltitre.place(x = 650, y = 40)

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
canvas = tk.Canvas(mafenetre, bg = 'black', width = 900, height = 700)
canvas.pack(pady=20)


class brique() : 
    briques = []
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
        brique.briques.append(self)

    def CreationBriques(canvas, lignes, couleur) :
    # fonction qui permet de créée les briques du jeux
    # entrée : le canvas, le nombre de ligne et la couleur
    # sortie : création des briques
        nb_briques_par_ligne = 7
        larg_brique = 120 #canvas_width // nb_briques_par_ligne
        haut_brique = 50
        debligne = 5 # nombre de pixels avant la première ligne
        for x in range(lignes): 
            row = debligne + (haut_brique + 5) * x
            for y in range(nb_briques_par_ligne) :
                col = y * (larg_brique + 10)
                brique(canvas, col, row, larg_brique - 5, haut_brique, couleur)

brique.CreationBriques(canvas, 7, "darkorchid4")


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
        # entrée : le canvas
        # sortie : la raquette bouge
            coords = self.canvas.coords(self.raquette)
            if coords[0] > 0:  
                self.canvas.move(self.raquette, -self.dx, 0)

    def droite(self, event) : 
    # fonction qui permet de déplacer la raquette vers la droite en utilisant le clavier
    # entrée : 
    # sortie : la raquette bouge    
        coords = self.canvas.coords(self.raquette)
        if coords[0] < 900 :   
            self.canvas.move(self.raquette, self.dx, 0)

maraquette = raquette(canvas)


largeur = 900
hauteur = 700
rayon = 10
x = largeur / 2
y = hauteur / 2
vitesse = 5
angle = rd.uniform(0.3 , 2.8)
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
    # fonction qui permet la collision entre widgets
    # entrée : aucune
    # sortie : la balle rebond
    global dx, dy, x, y, rayon
    a1x, a1y, a2x, a2y = canvas.bbox(maraquette.raquette) 
    b1x, b1y, b2x, b2y = canvas.bbox(balle)
    if (b2x >= a1x and b1x <= a2x) and (b2y >= a1y and b1y <= a2y) and dy > 0:
        dy = -abs(dy)
        y = a1y - rayon
        canvas.coords(balle, x - rayon, y - rayon, x + rayon, y + rayon)

def  deplacement() :
    # fonction qui permet que la balle se déplace
    # entrée : aucune
    # sortie : la balle se déplace
    global x, y, dx, dy, rayon, largeur, hauteur
    collision()
    if x + rayon + dx > largeur :
        x = 2 * (largeur - rayon ) - x
        dx = - dx
    if  x - rayon + dx < 0 :
        x = 2 * rayon - x
        dx = - dx
    if  y + rayon + dy > hauteur :
        x, y = largeur / 2, hauteur / 2
        dx, dy = 5 * mat.cos(angle), -abs(5 * mat.sin(angle))
    if  y - rayon + dy < 0 :
        y = 2 * rayon - y
        dy = - dy
    x = x + dx
    y = y + dy
    canvas.coords(balle, x - rayon, y - rayon, x + rayon, y + rayon)
    mafenetre.after(20, deplacement)


# Création des boutons quitter et lancer
boutonquitter = Button(mafenetre, text = 'Quitter', bg = 'chocolate2', fg = 'white', height = 4, width = 7, font = ("Britannic Bold", 16), command = mafenetre.destroy)
boutonquitter.pack(side = 'right', padx = 100)
boutonlancer = Button(mafenetre, text = 'Lancer', bg = 'royalblue2', fg = 'white', height = 4, width = 7, font = ("Britannic Bold", 16), command = lambda : deplacement())
boutonlancer.pack(side = 'left', padx = 100)


mafenetre.mainloop()