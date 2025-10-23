# Julie LE RAL / Nour TRABELSI - CPE - TP4 Casse brique
# DO TO : ameliorer le programme

from tkinter import Button, Label, StringVar, Frame
import tkinter as tk
import random as rd
import math as mat
from PIL import Image, ImageTk 
from collections import deque

# Création de la fenetre
mafenetre = tk.Tk()
mafenetre.title("Casse Brique")
mafenetre.geometry('1800x900')
frame_haut = Frame(mafenetre)
frame_haut.pack(side = 'top', fill = 'x')

# Affichage du titre du jeu
labeltitre = Label(frame_haut, text = "CASSE BRIQUE", fg = "black", font = ("Britannic Bold", 30))
labeltitre.place(x = 650, y = 40)

# Score et Vies
score_val = 0
vie_val = 3
score = StringVar()
vie = Image.open(r"C:\Users\jlera\Documents\CPE\3A\Développement_logiciel_en_python\casse-brique\Casse-Brique\coeur.jpg")
vie = vie.resize((40, 40), Image.LANCZOS)
vie_tk = ImageTk.PhotoImage(vie) 
vie_frame = Frame(frame_haut, bg = "white")
vie_frame.pack(side = "left", padx = 70 ,pady = 30)
def affichage() :
    global vie_val
    score.set(f"SCORE : {score_val}")
    for image in vie_frame.winfo_children() : 
        image.destroy()
    for _ in range(vie_val) : 
        label_vie = Label(vie_frame, image = vie_tk, bg = "white")
        label_vie.image = vie_tk
        label_vie.pack(side = "left", padx = 2)
affichage()
labelscore = Label(frame_haut, textvariable = score, height = 2, width = 10, font = ("Britannic Bold", 20))
labelscore.pack(side = 'right', padx = 70, pady = 10)

def fin() : 
    canvas.create_text(450, 350, text = "GAME OVER", fill = "white", font = ("Britannic Bold", 30))
def victoire() :
    canvas.create_text(450, 350, text = "WINNER", fill = "white", font = ("Britannic Bold", 30))

# Canvas du jeu
canvas = tk.Canvas(mafenetre, width = 900, height = 700, highlightthickness = 0)
canvas.pack(pady = 20)     
fond = Image.open(r"C:\Users\jlera\Documents\CPE\3A\Développement_logiciel_en_python\casse-brique\Casse-Brique\image.png")
fond_tk = ImageTk.PhotoImage(fond)
canvas.create_image(0, 0, anchor = "nw", image = fond_tk)
canvas.fond = fond_tk

# Classe Brique
class brique() : 
    briques = []
    def __init__(self, canvas, x, y, largeur, hauteur, couleur) :
        self.canvas = canvas
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur
        self.id = self.canvas.create_rectangle(x, y, x + largeur, y + hauteur, fill = couleur)
        brique.briques.append(self)
    def creation_briques(canvas, lignes, couleur) :
    # création des briques
    # entrée : le canvas, nombre de ligne et la couleur
    # sortie : briques
        nb_briques_par_ligne = 7
        larg_brique = 110
        haut_brique = 50
        marge = 5 # nombre de pixels avant la première ligne
        for x in range(lignes) : 
            row = marge + (haut_brique + 20) * x
            for y in range(nb_briques_par_ligne) :
                col = marge + y * (larg_brique + 20)
                brique(canvas, col, row, larg_brique - 5, haut_brique, couleur)
    def detruire(self) :
    # détruction des briques
    # entrée : self
    # sortie : la brique disparait
        self.canvas.delete(self.id)
        if self in brique.briques :
            brique.briques.remove(self)

brique.creation_briques(canvas, 5, "medium orchid")

# Classe Raquette
class raquette() : 
    def __init__(self,canvas) :
        self.canvas = canvas
        self.dx = 20
        posx = 650
        posy = 653
        self.id = canvas.create_rectangle(posx - 50, posy - 10, posx + 50, posy + 10, width = 2, fill = "royalblue2")
        self.canvas.focus_set() # permet de capter les touches
        self.canvas.bind_all('<Left>', self.gauche)
        self.canvas.bind_all('<Right>', self.droite)
    def gauche(self, event) :
    # déplacer la raquette vers la gauche
    # entrée : self, event 
    # sortie : la raquette va à gauche
            coords = self.canvas.coords(self.id)
            if coords[0] > 0 :  
                self.canvas.move(self.id, -self.dx, 0)
    def droite(self, event) : 
    # déplacer la raquette vers la droite
    # entrée : self, event 
    # sortie : la raquette va à droite  
        coords = self.canvas.coords(self.id)
        if coords[0] < 800 :   
            self.canvas.move(self.id, self.dx, 0)

# Classe Balle
class balle() :
    def __init__(self, canvas, raquette) :
        self.canvas = canvas
        self.raquette = raquette
        self.rayon = 10
        self.largeur = 900
        self.hauteur = 700
        self.vitesse = 8 
        self.x = self.largeur / 2
        self.y = 450
        self.angle = rd.uniform(0.3 , 2.8)
        self.dx = self.vitesse * mat.cos(self.angle)
        self.dy = self.vitesse * mat.sin(self.angle)
        self.id = self.canvas.create_oval(self.x - self.rayon, self.y - self.rayon, self.x + self.rayon, self.y + self.rayon, width = 1, fill = "turquoise3")
        self.en_mouv = False
    def lancer(self) :
    # mettre la balle en mouvement
    # entrée : self
    # sortie : la balle bouge
        if not self.en_mouv :
            self.en_mouv = True
            self.deplacement() 
    def reset(self) :
    # remettre la balle au centre
    # entrée : self
    # sortie : reset de la balle
        self.en_mouv = False
        self.x, self.y = self.largeur / 2, 450
        self.dx = rd.choice([-5, 5])
        self.dy = -5
        self.canvas.coords(self.id, self.x - self.rayon, self.y - self.rayon, self.x + self.rayon, self.y + self.rayon)
    def collision_raquette(self) :
    # collision entre widgets
    # entrée : self
    # sortie : la balle rebondit
        a1x, a1y, a2x, a2y = self.canvas.bbox(self.raquette.id) 
        b1x, b1y, b2x, b2y = self.canvas.bbox(self.id)
        if (b2x >= a1x and b1x <= a2x) and (b2y >= a1y and b1y <= a2y) and self.dy > 0 :
            self.dy = -abs(self.dy)
            self. y = a1y - self.rayon
            self.canvas.coords(self.id, self.x - self.rayon, self.y - self.rayon, self.x + self.rayon, self.y + self.rayon)
    def collision_brique(self) :
    # collision entre widgets
    # entrée : self
    # sortie : brique disparait si la balle la touche
        global score_val
        a1x, a1y, a2x, a2y = self.canvas.coords(self.id)
        for b in brique.briques[:] :
            b1x, b1y, b2x, b2y = self.canvas.coords(b.id)
            if (a2x >= b1x and a1x <= b2x) and (a2y >= b1y and a1y <= b2y) :
                b.detruire()
                score_val += 10
                affichage()
                self.dy = -self.dy
                if not brique.briques : 
                    victoire()
                    self.en_mouv = False
                break
    def  deplacement(self) :
    # la balle se déplace et rebondit sur les murs
    # entrée : self
    # sortie : la balle se déplace
        global vie_val
        if not self.en_mouv :
            return 
        self.collision_raquette()
        self.collision_brique()
        x = self.x + self.dx
        y = self.y + self.dy
        if x + self.rayon > self.largeur : # droite
            x = 2 * (self.largeur - self.rayon) - x
            self.dx = abs(self.dx)
        if  x - self.rayon < 0 : # gauche
            x = 2 * self.rayon - x
            self.dx = - abs(self.dx)
        if  y - self.rayon < 0 : # haut
            y = 2 * self.rayon - y
            self.dy = abs(self.dy)
        if  y + self.rayon > self.hauteur : # bas
            vie_val -= 1 
            affichage()
            if vie_val <= 0 :
                fin()
                self.en_mouv = False
                return
            else:
                self.reset()
                return   
        self.x -= self.dx
        self.y += self.dy
        self.canvas.coords(self.id, self.x - self.rayon, self.y - self.rayon, self.x + self.rayon, self.y + self.rayon)
        self.canvas.after(20, self.deplacement)

ma_raquette = raquette(canvas)
ma_balle = balle(canvas, ma_raquette)



# Règles du jeu
def afficher_regles() :
# création du widget des règles
# entrée : aucune
# sortie : règles du jeu
    regles_fenetre = tk.Toplevel(mafenetre)
    regles_fenetre.title("Règles du jeu")
    regles_fenetre.geometry("500x400")
    texte_regles = (
        " CASSE BRIQUE - Règles du jeu \n\n"
        "1. Déplacez la raquette avec les flèches < et >,\n"
        "2. Appuyez sur 'Lancer' pour actionner la balle,\n"
        "3. Faites rebondir la balle pour casser toutes les briques,\n"
        "4. Chaque brique détruite rapporte 10 points,\n"
        "5. Vous avez 3 vies : la balle perdue réduit vos vies de 1,\n"
        "6. Le jeu est terminé quand toutes les vies sont perdues,\n"
        "7. Vous gagnez si vous cassez toutes les briques.\n")
    label_regles = tk.Label(regles_fenetre, text = texte_regles, justify = "left", font = ("Calibri", 14), padx = 10, pady = 10)
    label_regles.pack(fill = "both", expand = True)
    btn_fermer = tk.Button(regles_fenetre, text = "Fermer", command = regles_fenetre.destroy, font = ("Britannic Bold", 14), bg = "cadet blue", fg = "white")
    btn_fermer.pack(pady = 10)

# Création des boutons
frame_droite = Frame(mafenetre)
frame_droite.pack(side = 'left', fill = 'x')
frame_boutons = tk.Frame(frame_droite, bg = 'black')
frame_boutons.pack(side='top', padx = 50)
boutonquitter = Button(mafenetre, text = "Quitter", bg = "firebrick2", fg = "white", height = 4, width = 7, font = ("Britannic Bold", 16), command = mafenetre.destroy)
boutonquitter.pack(side = 'right', padx = 100)
boutonlancer = Button(mafenetre, text = "Lancer", bg = "royalblue2", fg = "white", height = 4, width = 7, font = ("Britannic Bold", 16), command = ma_balle.lancer)
boutonlancer.pack(side = 'left', padx = 30)
boutonregles = tk.Button(frame_boutons, text = "Règles", bg = "cadet blue", fg = "white", height = 4, width = 7, font = ("Britannic Bold", 16), command = afficher_regles)
boutonregles.pack(side = 'right')

mafenetre.mainloop()