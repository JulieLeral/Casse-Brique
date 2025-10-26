# Julie LE RAL / Nour TRABELSI - CPE - TP4 Casse brique - 09/10/2025

from tkinter import Button, Label, StringVar, Frame
import tkinter as tk
from PIL import Image, ImageTk 
import os
from collections import deque
import classe_raquette as R
import classe_balle as B
import classe_briques as Br

# Classe du canvas et des boutons
class Principale() :

    def __init__(self, jeu, Brique_classe, Raquette_classe, Balle_classe) :
        self.jeu = jeu 
        self.Brique_classe = Brique_classe
        self.Raquette_classe = Raquette_classe
        self.Balle_classe = Balle_classe
        self.hauteur_jeu = 650
        self.largeur_jeu = 900
        self.score_valeur = 0
        self.vie_valeur = 3

        self.pile_scores = []
        self.texte_meilleur_score = StringVar()
        self.id_texte_fin = None
        self.en_pause = False

        fichier = os.path.dirname(__file__)
        image_coeur = os.path.join(fichier, "coeur.jpg")
        image_fond = os.path.join(fichier,"image.png")

        frame_haut = Frame(jeu)
        frame_haut.pack(side = "top", fill = "x")

        labeltitre = Label(frame_haut, text = "CASSE BRIQUE", fg = "black", font = ("Britannic Bold", 30))
        labeltitre.place(x = 650, y = 40)

        self.score = StringVar()
        self.labelscore = Label(frame_haut, textvariable = self.score, height = 2, width = 10, font = ("Britannic Bold", 16))
        self.labelscore.pack(side = 'right', padx = 70, pady = 10)

        self.texte_meilleur_score.set(f"Meilleur score : {self.meilleur_score()}")
        self.meilleur_score_label = Label(frame_haut, textvariable = self.texte_meilleur_score, fg = "black", font = ("Britannic Bold", 16))
        self.meilleur_score_label.pack(side = "right", padx = 10, pady = 10)

        self.vie = Image.open(image_coeur)
        self.vie = self.vie.resize((40, 40), Image.LANCZOS)
        self.vie_tk = ImageTk.PhotoImage(self.vie) 
        self.vie_frame = Frame(frame_haut)
        self.vie_frame.pack(side = "left", padx = 70 ,pady = 30)

        self.canvas = tk.Canvas(self.jeu, width = self.largeur_jeu, height = self.hauteur_jeu, highlightthickness = 0)
        self.canvas.pack(pady = 20)

        fond = Image.open(image_fond)
        self.fond_tk = ImageTk.PhotoImage(fond)
        self.canvas.create_image(0, 0, anchor = "nw", image = self.fond_tk)

        self.raquette = self.Raquette_classe(self.canvas)
        self.creation_briques(5, "medium orchid")
        self.balle = self.Balle_classe(self.canvas, self.raquette, self.Brique_classe, self)

        self.affichage()

        self.creation_boutons()

        self.file_messages = deque()
        self.mettre_a_jour_messages()

    def meilleur_score(self) :
    # Récupérer le meilleur score de la pile
    # Entrée : aucune
    # Sortie : le score maximum de la pile
        if self.pile_scores :
            return max(self.pile_scores) 
        else:
            return 0
    
    def ajouter_score(self, score_val) :
    # Ajouter un score à la pile des scores
    # Entrée : le score à ajouter
    # Sortie : le score est ajouté à la pile et l'affichage est mis à jour
        self.pile_scores.append(score_val)
        self.mettre_a_jour_affichage_meilleur_score()

    def mettre_a_jour_affichage_meilleur_score(self) :
    # Mettre à jour l'affichage du meilleur score
    # Entrée : aucune
    # Sortie : le meilleur score obtenu dans la pile est affiché
        score = self.meilleur_score()
        self.texte_meilleur_score.set(f"Meilleur Score : {score}")

    def creation_briques(self, lignes, couleur) :
    # Création des briques
    # Entrée : le canvas, nombre de ligne et la couleur
    # Sortie : briques
        nb_briques_par_ligne = 7
        larg_brique = 110
        haut_brique = 50
        marge = 5   # nombre de pixels avant la première ligne
        for x in range(lignes) : 
            pos_haut = marge + (haut_brique + 20) * x
            for y in range(nb_briques_par_ligne) :
                pos_gauche = marge + y * (larg_brique + 20)
                b = self.Brique_classe(self.canvas, pos_gauche, pos_haut, larg_brique - 5, haut_brique, couleur)
        
    def affichage(self) :
    # Afficher le score
    # Entrée : aucune
    # Sortie : Score
        self.score.set(f"SCORE : {self.score_valeur}")
        for image in self.vie_frame.winfo_children() : 
            image.destroy()
        for _ in range(self.vie_valeur) : 
            label_vie = Label(self.vie_frame, image = self.vie_tk, bg = "white")
            label_vie.image = self.vie_tk
            label_vie.pack(side = "left", padx = 2)

    # Règles du jeu
    def afficher_regles(self) :
    # Création du widget des règles
    # Entrée : aucune
    # Sortie : règles du jeu
        regles_fenetre = tk.Toplevel(self.jeu)
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
    # Création des boutons
    # Entrée : aucune
    # Sortie : boutons lancer, reglès, quitter
        self.boutons = Frame(self.jeu)
        self.boutons.pack(side = "bottom", pady = 30)
        # Bouton Lancer
        bouton_lancer = Button(self.boutons, text = "Lancer", bg = "royalblue2", fg = "white", font = ("Britannic Bold", 16), height = 2, width = 10, command = self.balle.lancer)
        bouton_lancer.pack(side = "left", padx = 30)
        # Bouton Règles
        bouton_regles = Button(self.boutons, text = "Règles", bg = "cadet blue", fg = "white", font = ("Britannic Bold", 16), height = 2, width = 10, command = self.afficher_regles)
        bouton_regles.pack(side = "left", padx = 30)
        # Bouton Rejouer
        self.bouton_rejouer = Button(self.boutons, text = "Rejouer", bg = "chocolate2", fg = "white", font = ("Britannic Bold", 16), height = 2, width = 10, command = self.reinitialiser_jeu)
        self.bouton_rejouer.pack(side = "left", padx = 30)
        # self.bouton_rejouer.config(state = tk.DISABLED)
        # Bouton Quitter
        bouton_quitter = Button(self.boutons, text = "Quitter", bg = "firebrick2", fg = "white", font = ("Britannic Bold", 16), height = 2, width = 10, command = self.jeu.destroy)
        bouton_quitter.pack(side = "left", padx = 30)

    def reinitialiser_jeu(self) :
    # Réinitialise la partie pour rejouer
    # Entrée : aucune
    # Sortie : nouvelle partie
        if self.id_texte_fin:
            self.canvas.delete(self.id_texte_fin)

        self.score_valeur = 0   
        self.vie_valeur = 3
        
        for brique in self.Brique_classe.liste_briques[:] :
            brique.detruire()
        self.creation_briques(5, "medium orchid")
        
        self.balle.reset()
        self.raquette.repositionner()
        
        self.affichage()

        self.bouton_rejouer.config(state = tk.DISABLED)
        self.bouton_lancer.config(state = tk.NORMAL)

    def fin(self) : 
    # Affichage pour une partie perdue
    # Entrée : aucune
    # Sortie : game over
        if not self.en_pause:
            self.id_texte_fin = self.canvas.create_text(450, 300, text = "GAME OVER", fill = "yellow", font = ("Britannic Bold", 30))
            self.ajouter_score(self.score_valeur) # 4. ENREGISTRE LE MEILLEUR SCORE
            self.bouton_rejouer.config(state=tk.NORMAL)
            self.bouton_lancer.config(state=tk.DISABLED)
            self.en_pause = True
    
    def victoire(self) :
    # Affichage pour une victoire
    # Entrée : aucune
    # Sortie : winner
        if not self.en_pause:
            self.id_texte_fin = self.canvas.create_text(450, 300, text = "WINNER", fill = "yellow", font = ("Britannic Bold", 30))
            self.ajouter_score(self.score_valeur) # 4. ENREGISTRE LE MEILLEUR SCORE
            self.bouton_rejouer.config(state=tk.NORMAL)
            self.bouton_lancer.config(state=tk.DISABLED)
            self.en_pause = True

    def ajouter_message(self, x, y, texte, duree = 1500) :
    # Ajouter un message
    # Entrée : x, y, texte, duree
    # Sortie : message
        message_id = self.canvas.create_text(x, y, text = texte, font = ("Britannic Bold", 16, "bold"), fill = "chocolate2")
        self.file_messages.append({'id': message_id, 'duree': duree, 'y': y})   # Stocker id et durée restante

    def mettre_a_jour_messages(self) :
    # Mettre à jour les messages
    # Entrée : aucune
    # Sortie : nouveau message
        for message in list(self.file_messages) :
            self.canvas.move(message['id'], 0, -1)
            message['y'] -= 1
            message['duree'] -= 50
            if message['duree'] <= 0 :
                self.canvas.delete(message['id'])
                if message in self.file_messages:
                    self.file_messages.remove(message)
        self.jeu.after(50, self.mettre_a_jour_messages) # Rappel toutes les 50 ms

    

        