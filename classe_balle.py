# Julie LE RAL / Nour TRABELSI - CPE - TP4 Casse brique

import random as rd
import math as mat

# Classe Balle
class balle() :

    def __init__(self, canvas, raquette, brique, principale ) :
        self.canvas = canvas
        self.raquette = raquette
        self.brique = brique
        self.principale = principale 
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
    # Entrée : self
    # Sortie : la balle bouge
        if not self.en_mouv :
            self.en_mouv = True
            self.deplacement() 

    def reset(self) :
    # remettre la balle au centre
    # Entrée : self
    # Sortie : reset de la balle
        self.en_mouv = False
        self.x, self.y = self.largeur / 2, 450
        self.dx = rd.choice([-5, 5])
        self.dy = -5
        self.canvas.coords(self.id, self.x - self.rayon, self.y - self.rayon, self.x + self.rayon, self.y + self.rayon)

    def collision_raquette(self) :
    # collision entre widgets
    # Entrée : self
    # Sortie : la balle rebondit
        a1x, a1y, a2x, a2y = self.canvas.bbox(self.raquette.id) 
        b1x, b1y, b2x, b2y = self.canvas.bbox(self.id)
        if (b2x >= a1x and b1x <= a2x) and (b2y >= a1y and b1y <= a2y) and self.dy > 0 :
            self.dy = -abs(self.dy)
            self. y = a1y - self.rayon
            self.canvas.coords(self.id, self.x - self.rayon, self.y - self.rayon, self.x + self.rayon, self.y + self.rayon)

    def collision_brique(self) :
    # collision entre widgets
    # Entrée : self
    # Sortie : brique disparait si la balle la touche
        global score_val
        a1x, a1y, a2x, a2y = self.canvas.coords(self.id)
        for b in self.brique.briques[:] :
            b1x, b1y, b2x, b2y = self.canvas.coords(b.id)
            if (a2x >= b1x and a1x <= b2x) and (a2y >= b1y and a1y <= b2y) :
                b.detruire()
                score_val += 10
                self.principale.affichage()
                self.dy = -self.dy
                if not self.brique.briques : 
                    self.principale.victoire()
                    self.en_mouv = False
                break

    def  deplacement(self) :
    # la balle se déplace et rebondit sur les murs
    # Entrée : self
    # Sortie : la balle se déplace
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
            self.principale.affichage()
            if vie_val <= 0 :
                self.principale.fin()
                self.en_mouv = False
                return
            else:
                self.reset()
                return   
        self.x -= self.dx
        self.y += self.dy
        self.canvas.coords(self.id, self.x - self.rayon, self.y - self.rayon, self.x + self.rayon, self.y + self.rayon)
        self.canvas.after(20, self.deplacement)