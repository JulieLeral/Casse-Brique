# Julie LE RAL / Nour TRABELSI - CPE - TP4 Casse brique - 09/10/2025
# DO TO : ameliorer le programme

# Classe Raquette
class Raquette() : 

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
    # Entrée : self, event 
    # Sortie : la raquette va à gauche
            coords = self.canvas.coords(self.id)
            if coords[0] > 0 :  
                self.canvas.move(self.id, -self.dx, 0)
    def droite(self, event) : 
    # déplacer la raquette vers la droite
    # Entrée : self, event 
    # Sortie : la raquette va à droite  
        coords = self.canvas.coords(self.id)
        if coords[0] < 800 :   
            self.canvas.move(self.id, self.dx, 0)