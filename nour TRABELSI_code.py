# Julie LE RAL, nour TRABELSI - CPE - TP4 Casse brique - Interface
# DO TO : finir programme
# - menu avec les boutons lancer/ quitter/ les vies/ le score
# - bouton avec les rÃ¨gles du jeu


from tkinter import Button, Label, StringVar, Frame
import tkinter as tk
import random as rd
import math as mat

import tkinter as tk
import random

# crÃ©ation de la fenÃªtre
mafenetre = tk.Tk()
mafenetre.title('Casse brique')
mafenetre.geometry('1800x900')

# vie et score
score_val = 0
vie_val = 3
en_mouvement = False

score = tk.StringVar()
vie = tk.StringVar()

#fonction qui met Ã  jour l'affichage du score et des vies
#entrÃ©e:
#sortie : mise Ã  jour de l'affichage avec le nouveau score et le nombre de vies
def maj_affichage():
    score.set(f"Score : {score_val}")
    vie.set(f"Vies : {vie_val}")
maj_affichage()

frame_haut = tk.Frame(mafenetre, bg='black', height=100)
frame_haut.pack(side='top', fill='x')

# Titre
labeltitre = tk.Label(frame_haut, text='CASSE BRIQUE', fg='black', font=("Britannic Bold", 30))
labeltitre.pack(pady=5)

# Score et vies
frame_score = tk.Frame(frame_haut, bg='black')
frame_score.pack(side='top', pady=2)
labelscore = tk.Label(frame_score, textvariable=score, font=("Calibri", 20), fg='white', bg='black')
labelscore.pack(side='right', padx=20)
labelvie = tk.Label(frame_score, textvariable=vie, font=("Calibri", 20), fg='white', bg='black')
labelvie.pack(side='left', padx=20)

# Canvas du jeu 
canvas = tk.Canvas(mafenetre, bg='black', width=1000, height=700)
canvas.pack(side='top', fill='both', expand=True, pady=20)


#classe raquette
class Raquette:
    #fonction qui initialise la raquette
    #entÃ©e:  le canvas oÃ¹ la raquette va Ãªtre dessinÃ©e
    #sortie : crÃ©ation de la raquette sur le canvas
    def __init__(self, canvas, largeur=150, hauteur=20, x=None, y=500, couleur="white"):
        self.canvas = canvas
        self.largeur = largeur
        self.hauteur = hauteur
        if x is None:
            x = (1000 - largeur) / 2
        self.coords = [x, y, x + largeur, y + hauteur]
        self.id = canvas.create_rectangle(*self.coords, fill=couleur)
    
    def gauche(self, event=None):
        #Fonction qui permet de dÃ©placer la raquette Ã  gauche 
        #entrÃ©e : touche appuyÃ©e
        #sortie : dÃ©placement de la raquette Ã  gauche
        rx1, ry1, rx2, ry2 = self.canvas.coords(self.id)
        deplacement = 40
        if rx1 - deplacement >= 0:
            self.canvas.move(self.id, -deplacement, 0)
        else:
            self.canvas.coords(self.id, 0, ry1, self.largeur, ry2)

    def droite(self, event=None):
    #Fonction qui permet de dÃ©placer la raquette Ã  droite 
    #entrÃ©e : touche appuyÃ©e
    #sortie : dÃ©placement de la raquette Ã  dorite
        rx1, ry1, rx2, ry2 = self.canvas.coords(self.id)
        deplacement = 40
        if rx2 + deplacement <= 1300:
            self.canvas.move(self.id, deplacement, 0)
        else:
            self.canvas.coords(self.id, 1300 - self.largeur, ry1, 1300, ry2)
#classe balle
class Balle:
    #fonction qui initialise la balle
    #entrÃ©e : le canvas oÃ¹ la balle va Ãªtre dessinÃ©e, la raquette, les briques, la position initiale, le rayon, la vitesse et la couleur
    #sortie : crÃ©ation de la balle sur le canvas
    def __init__(self, canvas, raquette, briques, x=450, y=640, r=12, dx=5, dy=-5, couleur="white"):
        self.canvas = canvas
        self.raquette = raquette
        self.briques = briques
        self.x = x
        self.y = y
        self.r = r
        self.dx = dx
        self.dy = dy
        self.id = canvas.create_oval(x - r, y - r, x + r, y + r, fill=couleur)
        self.en_mouvement = False

    def reset(self):
        #fonction qui rÃ©initialise la balle Ã  sa position de dÃ©part
        #entrÃ©e:
        #sortie : la balle est replacÃ©e Ã  sa position initiale
        global vie_val
        if vie_val > 0:
            self.en_mouvement = False
            self.x = 450
            self.y = 640
            self.dx = random.choice([-5, 5])
            self.dy = -5
            self.canvas.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        else:
            # Plus de vies â†’ GAME OVER
            self.en_mouvement = False
            self.canvas.create_text(500, 350, text="ðŸ’€ GAME OVER ðŸ’€", fill="red", font=("Britannic Bold", 40))

    def deplacement(self):
        #fonction qui gÃ¨re le dÃ©placement de la balle, les collisions avec les murs, la raquette et les briques
        #entÃ©e:
        #sortie : la balle se dÃ©place et gÃ¨re les collisions
        global score_val, vie_val
        if not self.en_mouvement:
            return

        self.x += self.dx
        self.y += self.dy

        # rebonds murs
        if self.x - self.r < 0 or self.x + self.r > 1000:
            self.dx = -self.dx
        if self.y - self.r < 0:
            self.dy = -self.dy

        # rebond raquette
        rx1, ry1, rx2, ry2 = self.canvas.coords(self.raquette.id)
        bx1, by1, bx2, by2 = self.canvas.coords(self.id)
        if by2 >= ry1 and bx2 >= rx1 and bx1 <= rx2 and self.dy > 0:
            # Modification de l'angle selon le point d'impact
            centre_raquette = (rx1 + rx2) / 2
            distance = (self.x - centre_raquette) / (self.raquette.largeur / 2)
            self.dx = 5 * distance  # angle proportionnel Ã  l'endroit touchÃ©
            self.dy = -abs(self.dy)

        # collision briques
        for brique in list(self.briques):
            bx1_b, by1_b, bx2_b, by2_b = self.canvas.coords(brique.id)
            if bx2_b >= self.x - self.r and bx1_b <= self.x + self.r and by2_b >= self.y - self.r and by1_b <= self.y + self.r:
                self.canvas.delete(brique.id)
                self.briques.remove(brique)
                self.dy = -self.dy
                score_val += 10
                maj_affichage()
                break

        # victoire
        if not self.briques:
            self.canvas.create_text(500, 350, text="ðŸ† WINNER !", fill="yellow", font=("Britannic Bold", 40))
            self.en_mouvement = False
            return

        # balle tombe vers le bas du canvas
        if self.y + self.r > 700:
            vie_val -= 1
            maj_affichage()
            if vie_val > 0:
                self.reset()
            else:
                self.en_mouvement = False
                self.canvas.create_text(500, 350, text="ðŸ’€ GAME OVER ðŸ’€", fill="red", font=("Britannic Bold", 40))
            return

        self.canvas.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        self.canvas.after(20, self.deplacement)

#classe brique
class Brique:
    #fonction qui initialise une brique
    #entrÃ©e : le canvas oÃ¹ la brique va Ãªtre dessinÃ©e, les coordonnÃ©es, la couleur
    #sortie : crÃ©ation de la brique sur le canvas
    def __init__(self, canvas, x1, y1, x2, y2, couleur="red"):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x1, y1, x2, y2, fill=couleur, outline="black")


#CrÃ©ation raquette
ma_raquette = Raquette(canvas)

#CrÃ©ation briques
briques = []
nb_lignes = 5
nb_par_ligne = 17
largeur_brique = 90
hauteur_brique = 30
marge = 5
couleurs = ["purple4", "royalblue3", "darkorange3", "red3", "gold3", "green3"]

decalage_x = (1000 - (nb_par_ligne * largeur_brique + (nb_par_ligne - 1) * marge)) / 2

for i in range(nb_lignes):
    for j in range(nb_par_ligne):
        x1 = decalage_x + j * (largeur_brique + marge)
        y1 = 50 + i * (hauteur_brique + marge)
        x2 = x1 + largeur_brique
        y2 = y1 + hauteur_brique
        brique = Brique(canvas, x1, y1, x2, y2, couleur=couleurs[i % len(couleurs)])
        briques.append(brique)

#CrÃ©ation balle
ma_balle = Balle(canvas, ma_raquette, briques)

#lier les touches au dÃ©placement de la raquette
canvas.bind_all("<Left>", ma_raquette.gauche)
canvas.bind_all("<Right>", ma_raquette.droite)



# fonction qui affiche les rÃ¨gles du jeu dans une nouvelle fenÃªtre
#entrÃ©e : appui sur le bouton rÃ¨gles
#sortie : une nouvelle fenÃªtre s'ouvre avec les rÃ¨gles du jeu
def afficher_regles():
    regles_fenetre = tk.Toplevel(mafenetre)
    regles_fenetre.title("RÃ¨gles du jeu")
    regles_fenetre.geometry("500x400")

    texte_regles = (
        "ðŸ° CASSE BRIQUE - RÃ¨gles du jeu ðŸ°\n\n"
        "1. DÃ©placez la raquette avec les flÃ¨ches â† et â†’.\n"
        "2. Appuyez sur 'Lancer' pour lancer la balle.\n"
        "3. Faites rebondir la balle pour casser toutes les briques.\n"
        "4. Chaque brique dÃ©truite rapporte 10 points.\n"
        "5. Vous avez 3 vies. La balle perdue rÃ©duit vos vies de 1.\n"
        "6. Le jeu est terminÃ© quand toutes les vies sont perdues.\n"
        "7. Vous gagnez si vous cassez toutes les briques.\n")

    label_regles = tk.Label(regles_fenetre, text=texte_regles, justify="left",
                            font=("Calibri", 14), padx=10, pady=10)
    label_regles.pack(fill="both", expand=True)

    btn_fermer = tk.Button(regles_fenetre, text="Fermer", command=regles_fenetre.destroy,
                           font=("Britannic Bold", 14), bg="royalblue2", fg="white")
    btn_fermer.pack(pady=10)


def lancer():
    #fonction qui permet de lancer la balle
    #entrÃ©e : appui sur le bouton lancer
    #sortie : la balle se met en mouvement
    if not ma_balle.en_mouvement:
        ma_balle.en_mouvement = True
        ma_balle.deplacement()
        
#Boutons lancer et quitter
frame_boutons = tk.Frame(frame_haut, bg='black')
frame_boutons.pack(side='top', pady=5)

btn_lancer = tk.Button(frame_boutons, text="Lancer", bg="royalblue2", fg="white",
                       height=2, width=7, font=("Britannic Bold", 16),
                       command=lancer)
btn_lancer.pack(side='left', padx=10)

btn_quitter = tk.Button(frame_boutons, text="Quitter", bg="chocolate2", fg="white",
                        height=2, width=7, font=("Britannic Bold", 16),
                        command=mafenetre.destroy)
btn_quitter.pack(side='left', padx=10)

btn_regles = tk.Button(frame_boutons, text="RÃ¨gles", bg="green", fg="white",
                       height=2, width=7, font=("Britannic Bold", 16),
                       command=afficher_regles)
btn_regles.pack(side='left', padx=10)

#Boucle principale
mafenetre.mainloop()

