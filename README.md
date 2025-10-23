# Casse-Brique

# Règles du jeu : 
1. Déplacez la raquette avec les flèches < et >,
2. Appuyez sur 'Lancer' pour actionner la balle,
3. Faites rebondir la balle pour casser toutes les briques,
4. Chaque brique détruite rapporte 10 points,
5. Vous avez 3 vies : la balle perdue réduit vos vies de 1,
6. Le jeu est terminé quand toutes les vies sont perdues,
7. Vous gagnez si vous cassez toutes les briques.

# Spécificités :
- le bouton 'Lancer' pour démarrer la balle,
- le bouton 'Quitter' pour quitter le jeu,
- le bouton 'Règles' pour afficher les règles du jeu dans une fenêtre,
- le fond du canvas est une image,
- le score est affiché en temps réel (+10 points par brique cassée),
- il y a une image de fond de jeu pour le canvas,
- les vies sont représentées par trois images de coeur, 


- Tu peux utiliser une pile pour mémoriser les derniers scores obtenus, par exemple après chaque partie.
Quand tu rejoues, tu peux afficher les 3 dernières parties.

- Imagine que tu veux afficher plusieurs petits messages à l’écran (par exemple, “+10 points”, “Combo !”, “Super tir !”) sans les montrer tous d’un coup.
Tu peux les empiler dans une file et les afficher l’un après l’autre.
- Tu peux stocker dans une file toutes les briques à créer, et les afficher progressivement pour une animation d’apparition.
