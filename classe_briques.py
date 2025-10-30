# Julie LE RAL / Nour TRABELSI - CPE - TP4 Casse brique - 09/10/2025

''' 
CLASSE DES BRIQUES
Elle contient :
- La création d'une brique, 
- La destruction d'une brique. 
'''

class Brique() : 

    liste_briques = []

    def __init__(self, canvas, x, y, largeur, hauteur, couleur) :
        self.canvas = canvas
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur = couleur
        self.id = self.canvas.create_rectangle(x, y, x + largeur, y + hauteur, fill = couleur)
        self.points = 10
        Brique.liste_briques.append(self)

    def detruire(self) :
    # Détruction des briques
    # Entrée : aucune
    # Sortie : la brique disparait
        self.canvas.delete(self.id)
        if self in Brique.liste_briques :
            Brique.liste_briques.remove(self)
