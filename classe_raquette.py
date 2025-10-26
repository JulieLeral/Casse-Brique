# Julie LE RAL / Nour TRABELSI - CPE - TP4 Casse brique - 09/10/2025
# DO TO : ameliorer le programme

# Classe Raquette
class Raquette() : 

    def __init__(self,canvas) :
        self.canvas = canvas
        self.dx = 20
        posx = 650
        posy = 600
        self.id = canvas.create_rectangle(posx - 50, posy - 10, posx + 50, posy + 10, width = 2, fill = "royalblue2")
        self.canvas.focus_set() # permet de capter les touches
        self.canvas.bind_all('<Left>', self.gauche)
        self.canvas.bind_all('<Right>', self.droite)

    def repositionner(self) :
    # Ramène la raquette à sa position initiale
    # Entrée : aucune
    # Sortie : raquette est repositionnée
        x1 = self.posx - 50
        y1 = self.posy - 10
        x2 = self.posx + 50
        y2 = self.posy + 10
        self.canvas.coords(self.id, x1, y1, x2, y2)

    def gauche(self, event) :
    # Déplacer la raquette vers la gauche
    # Entrée : event 
    # Sortie : la raquette va à gauche
            coords = self.canvas.coords(self.id)
            if coords[0] > 0 :  
                self.canvas.move(self.id, -self.dx, 0)
    def droite(self, event) : 
    # Déplacer la raquette vers la droite
    # Entrée : event 
    # Sortie : la raquette va à droite  
        coords = self.canvas.coords(self.id)
        if coords[0] < 800 :   
            self.canvas.move(self.id, self.dx, 0)