# Julie LE RAL / Nour TRABELSI - CPE - TP4 Casse brique - 09/10/2025

import random as rd
import math as mat

# Classe Balle
class Balle() :

    def __init__(self, canvas, raquette, Brique_classe, principale) :
        self.canvas = canvas
        self.raquette = raquette
        self.Brique_classe = Brique_classe
        self.principale = principale
        self.rayon = 10
        self.largeur = 900
        self.hauteur = 650
        self.vitesse = 8 
        self.x = self.largeur / 2
        self.y = 450
        self.angle = rd.uniform(0.3 , 2.8)
        self.dx = self.vitesse * mat.cos(self.angle)
        self.dy = self.vitesse * mat.sin(self.angle)
        if self.dy > 0:
            self.dy = - self.dy
        self.id = self.canvas.create_oval(self.x - self.rayon, self.y - self.rayon, self.x + self.rayon, self.y + self.rayon, width = 1, fill = "turquoise3")
        self.en_mouvement = False

    def lancer(self) :
    # Mettre la balle en mouvement
    # Entrée : aucune
    # Sortie : la balle bouge
        if not self.en_mouvement :
            self.en_mouvement = True
            self.deplacement() 

    def reset(self) :
    # Remettre la balle au centre
    # Entrée : aucune
    # Sortie : reset de la balle
        self.en_mouvement = False
        self.x, self.y = self.largeur / 2, 450
        self.angle = rd.uniform(0.3 , 2.8)
        self.dx = self.vitesse * mat.cos(self.angle)
        self.dy = self.vitesse * mat.sin(self.angle)
        if self.dy > 0 :
            self.dy = - self.dy
        self.canvas.coords(self.id, self.x - self.rayon, self.y - self.rayon, self.x + self.rayon, self.y + self.rayon)

    def collision_raquette(self) :
    # Collision entre widgets
    # Entrée : aucune
    # Sortie : la balle rebondit
        a1x, a1y, a2x, a2y = self.canvas.bbox(self.raquette.id) 
        b1x, b1y, b2x, b2y = self.canvas.bbox(self.id)
        if (b2x >= a1x and b1x <= a2x) and (b2y >= a1y and b1y <= a2y) and self.dy > 0 :
            self.dy = -abs(self.dy)
            self. y = a1y - self.rayon
            self.canvas.coords(self.id, self.x - self.rayon, self.y - self.rayon, self.x + self.rayon, self.y + self.rayon)

    def collision_brique(self) :
    # Collision entre widgets
    # Entrée : aucune
    # Sortie : brique disparait si la balle la touche
        a1x, a1y, a2x, a2y = self.canvas.coords(self.id)
        for brique in self.Brique_classe.liste_briques[:] :
            b1x, b1y, b2x, b2y = self.canvas.coords(brique.id)
            if (a2x >= b1x and a1x <= b2x) and (a2y >= b1y and a1y <= b2y) :
                centre_brique_x = (b1x + b2x) / 2
                centre_brique_y = (b1y + b2y) / 2
                centre_balle_x = (a1x + a2x) / 2
                centre_balle_y = (a1y + a2y) / 2
                dist_x = abs(centre_balle_x - centre_brique_x)
                dist_y = abs(centre_balle_y - centre_brique_y)
                if dist_x / ((b2x - b1x) / 2) > dist_y / ((b2y - b1y) / 2):
                    self.dx = -self.dx  # Rebond horizontal
                else:
                    self.dy = -self.dy
                brique.detruire()
                self.principale.score_valeur += 10 
                self.principale.ajouter_message(self.x, self.y, "+10 points") 
                self.principale.affichage()
                if not self.Brique_classe.liste_briques :
                    self.principale.victoire()
                    self.en_mouv = False
                break

    def  deplacement(self) :
    # La balle se déplace et rebondit sur les murs
    # Entrée : aucune
    # Sortie : la balle se déplace
        if not self.en_mouvement :
            return 
        self.collision_raquette()
        self.collision_brique()
        self.x += self.dx
        self.y += self.dy
        if self.x + self.rayon > self.largeur :
            self.x = 2 * (self.largeur - self.rayon) - self.x
            self.dx = - abs(self.dx)
        if  self.x - self.rayon < 0 : 
            self.x = 2 * self.rayon - self.x
            self.dx = abs(self.dx)
        if  self.y - self.rayon < 0 :
            self.y = 2 * self.rayon - self.y
            self.dy = abs(self.dy)
        if  self.y + self.rayon > self.hauteur : 
            self.principale.vie_valeur -= 1 
            self.principale.affichage()
            self.principale.ajouter_message(self.x, self.y, "Vie perdue !", 2000) 
            if self.principale.vie_valeur <= 0 :
                self.principale.fin()
                self.en_mouvement = False
                return
            else:
                self.reset()
                return 
        self.canvas.coords(self.id, self.x - self.rayon, self.y - self.rayon, self.x + self.rayon, self.y + self.rayon)
        self.canvas.after(20, self.deplacement)