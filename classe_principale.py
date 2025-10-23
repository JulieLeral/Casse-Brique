# Julie LE RAL / Nour TRABELSI - CPE - TP4 Casse brique - 09/10/2025

from tkinter import Button, Label, StringVar, Frame
import tkinter as tk
from PIL import Image, ImageTk 
import os
from collections import deque

# Classe du canvas et des boutons
class Principale() :
    briques = []

    def __init__(self, fenetre, Brique, Raquette, Balle) :
        self.fenetre = fenetre
        self.brique = Brique
        self.raquette = Raquette
        self.balle = Balle
        self.hauteur = 700
        self.largeur = 900
        self.score_val = 0
        self.vie_val = 3

        fichier = os.path.dirname(__file__)
        coeur_path = os.path.join(fichier, "coeur.jpg")
        fond_path = os.path.join(fichier,"image.png")

        frame_haut = Frame(fenetre)
        frame_haut.pack(side = "top", fill = "x")

        labeltitre = Label(frame_haut, text = "CASSE BRIQUE", fg = "black", font = ("Britannic Bold", 30))
        labeltitre.place(x = 650, y = 40)

        self.score = StringVar()
        self.labelscore = Label(frame_haut, textvariable = self.score, height = 2, width = 10, font = ("Britannic Bold", 20))
        self.labelscore.pack(side = 'right', padx = 70, pady = 10)

        self.vie = Image.open(coeur_path)
        self.vie = self.vie.resize((40, 40), Image.LANCZOS)
        self.vie_tk = ImageTk.PhotoImage(self.vie) 
        self.vie_frame = Frame(frame_haut)
        self.vie_frame.pack(side = "left", padx = 70 ,pady = 30)

        self.canvas = tk.Canvas(self.fenetre, width = self.largeur, height = self.hauteur, highlightthickness = 0)
        self.canvas.pack(pady = 20)

        fond = Image.open(fond_path)
        self.fond_tk = ImageTk.PhotoImage(fond)
        self.canvas.create_image(0, 0, anchor = "nw", image = self.fond_tk)

        self.brique.creation_briques(self.canvas, lignes = 5, couleur ="medium orchid")
        self.raquette = self.raquette(self.canvas)
        self.balle = self.balle(self.canvas, self.raquette, self)

        self.affichage()

        self.creation_boutons()

        # self.file_messages = deque()

    def creation_briques(self, canvas, lignes, couleur) :
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
                self.brique(canvas, col, row, larg_brique - 5, haut_brique, couleur)

    def affichage(self) :
        self.score.set(f"SCORE : {self.score_val}")
        for image in self.vie_frame.winfo_children() : 
            image.destroy()
        for _ in range(self.vie_val) : 
            label_vie = Label(self.vie_frame, image = self.vie_tk, bg = "white")
            label_vie.image = self.vie_tk
            label_vie.pack(side = "left", padx = 2)

    # Règles du jeu
    def afficher_regles(self) :
    # création du widget des règles
    # Entrée : self
    # Sortie : règles du jeu
        regles_fenetre = tk.Toplevel(self.fenetre)
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

    def creation_boutons(self) :
    # création des boutons
    # Entrée : self
    # Sortie : boutons lancer, reglès, quitter
        boutons = Frame(self.fenetre)
        boutons.pack(side = "bottom", pady = 30)
        # Bouton Lancer
        bouton_lancer = Button(boutons, text = "Lancer", bg = "royalblue2", fg = "white", font = ("Britannic Bold", 16), height = 2, width = 10, command = self.balle.lancer)
        bouton_lancer.pack(side = "left", padx = 30)
        # Bouton Règles
        bouton_regles = Button(boutons, text = "Règles", bg = "cadet blue", fg = "white", font = ("Britannic Bold", 16), height = 2, width = 10, command = self.afficher_regles)
        bouton_regles.pack(side = "left", padx = 30)
        # Bouton Quitter
        bouton_quitter = Button(boutons, text = "Quitter", bg = "firebrick2", fg = "white", font = ("Britannic Bold", 16), height = 2, width = 10, command = self.fenetre.destroy)
        bouton_quitter.pack(side = "left", padx = 30)

    def fin(self) : 
    # affichage pour une partie perdue
    # Entrée : self
    # Sortie : game over
        self.canvas.create_text(450, 350, text = "GAME OVER", fill = "white", font = ("Britannic Bold", 30))
    
    def victoire(self) :
    # affichage pour une victoire
    # Entrée : self
    # Sortie : winner
        self.canvas.create_text(450, 350, text = "WINNER", fill = "white", font = ("Britannic Bold", 30))

    def ajouter_message(self, x, y, texte, duree = 1500) :
    # ajouter un message
    # Entrée : self, x, y, texte, duree
    # Sortie : message
        msg_id = self.canvas.create_text(x, y, text = texte, font = ("Arial", 16, "bold"), fill = "yellow")
        # Stocker id et durée restante
        self.file_messages.append({'id': msg_id, 'duree': duree, 'y': y})

    '''def mettre_a_jour_messages(self) :
    # mettre à jour les messages
    # Entrée : self
    # Sortie : nouveau message
        for msg in list(self.file_messages) :
            # Monter légèrement le texte
            self.canvas.move(msg['id'], 0, -1)
            msg['y'] -= 1
            msg['duree'] -= 50
            if msg['duree'] <= 0 :
                self.canvas.delete(msg['id'])
                self.file_messages.popleft()  # retire de la file
        # Rappel toutes les 50 ms
        self.fenetre.after(50, self.mettre_a_jour_messages)
    mettre_a_jour_messages()'''

    

        