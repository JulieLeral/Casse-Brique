# Julie LE RAL / Nour TRABELSI - CPE - TP4 Casse brique

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
    # Entrée : le canvas, nombre de ligne et la couleur
    # Sortie : briques
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
    # Entrée : self
    # Sortie : la brique disparait
        self.canvas.delete(self.id)
        if self in brique.briques :
            brique.briques.remove(self)
