Projet Icewalker
================

## Préalable

Consulter le cours suivant sur la 
[programmation objet](assets/Le_modele_objet.md)

## I. Présentation du jeu

Marcher sur la glace est un exercice périlleux :

-   on ne peut pas changer de direction
-   il est difficile de s'arrêter.

Dans ce projet, nous allons nous intéresser à la programmation d'un jeu dans lequel
le joueur incarnera un personnage se déplaçant sur la glace.

Le terrain est :

-   rectangulaire
-   entièrement constitué de cases gelées, à l'exception d'une seule case appelée **case finale**.
-   entouré de murs placés sur un segment adjacent à deux cases.

Notre joueur est aidé dans sa quête par une équipe d'autres personnages pouvant se déplacer de la même manière sur la grille.

Par convention, le joueur principal sera numéroté 0 et les autres joueur 1, 2, 3, &#x2026;

À chaque étape du jeu, le joueur choisit un personnage et une direction parmi quatre (Nord, Sud, Est, Ouest) pour le personnage choisi. 

Ce dernier se déplace alors dans la direction choisie en ligne droite **jusqu'à rencontrer un obstacle**.
La case finale est considérée comme un obstacle pour les joueurs autres que le joueur principal.

Le jeu se finit lorsque :

-   le joueur **principal** est arrivé sur la case finale 
-   il abandonne la partie (il n'est parfois plus possible de rejoindre la case finale si une 
    mauvaise direction a été prise)


## II. Travail à effectuer


1) Modélisation du jeu

a) Dans un fichier grid.py, créez une classe `grid` permettant de modéliser le plateau du jeu.

Voici les fonctionnalités de cette classe : 

-   Créer une grille vide grâce à sa largeur et à sa hauteur ;

-   Ajouter (et peut-être supprimer) la case finale ;

-   Ajouter (supprimer) des murs ;

-   Créer une grille à partir d'un fichier. Des exemples de tels fichiers sont fournis dans le dossier data.
    
-   Placer des joueurs dans le plateau du jeu ;

    ```python
    >>> g.set_config(((3,4),(1,5),(6,2)))
    ```
    
-   Récupérer la position d'un joueur et de tous les joueurs sous la forme d'un tuple de coordonnées :
    
    ```python
    >>> g.get_config()
    ((3,4),(1,5),(3,2))
    ```
    
-   Déplacer un joueur dans une direction selon les règles du jeu ;

-   Implémenter la méthode `__str__`, qui permettra d'afficher le plateau du jeu.

b) Dans un fichier grid_square.py, on définit maintenant une classe `case` pour modéliser les cases du plateau. 
Une case peut posséder ou non des murs dans différentes directions, contenir ou non un joueur et être ou non la case finale.

c) Dans un fichier main.py, on définit maintenant la classe `IceWalker` permettant de modéliser le jeu. Un jeu est paramétré par un plateau de jeu.
Les fonctionalités principales de cette classe sont :

-	Permettre de jouer au jeu de manière interactive.

- Permettre des retours en arrière (undo) : parfois, on s'aperçoit qu'un mouvement nous a été fatal : on est certain de ne plus pouvoir atteindre la sortie. En utilisant une structure de données adaptée, faites en sorte que l'on puisse revenir en arrière dans l'historique des coups joués. On doit éventuellement pouvoir revenir plusieurs coups en arrière, jusqu'à la configuration initiale. On pourra appliquer une pénalité au score pour chaque retour en arrière effectué.


2) Faire jouer un humain (résolution <q>à la main</q>)

Réalisez un programme qui permet à un joueur humain de jouer au jeu `IceWalker`. 
Vous pouvez, par exemple, vous inspirez de la trace d'exécution fournie dans l'exemple ci-dessous.

3) Attribution des scores

Votre programme, d'une manière ou d'une autre, sera paramétré par 

-   le nom du joueur ;
-   l'emplacement de la grille.

Il aura pour résultat le score du joueur : il s'agit du nombre de coups joués par
le joueur pour amener le joueur principal sur la case finale, avec application d'une pénalité pour chaque retour en arrière. Plus le score est bas, meilleur il est.


### Exemple

Voici un exemple de déroulement de jeu possible :

    >>> g = Grid.from_file("datas/grid01.txt")
    >>> game = IceWalker(g)
    >>> game.play("Timoleon")
    
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 
    |1      |           |           |
    +                               + 
    |                           |   |
    +                          -+  -+ 
    |  2        |                   |
    +          -+     +-            + 
    |                 |             |
    +    -+                      -+ + 
    |     |        3              | |
    +-                              + 
    |             |          0      |
    + +-          +-                + 
    | |                     |       |
    +             +-+-+     +-      + 
    |             |   |             |
    +             +   +             + 
    |             |   |             |
    +             +-+-+             + 
    |       |                 |     |
    +       +-  +-            +-    + 
    |           |                   |
    +-                              + 
    |                   |           |
    +              -+  -+          -+ 
    |               |               |
    +  -+                        -+ + 
    |   |                         | |
    +                   +-          + 
    |      ⬜|           |           |
    +      -+                       + 
    |         |             |       |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 
    Timoleon, entrez votre mouvement 'num,direction' ou 'q' (quit) : 0,W
    
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 
    |1      |           |           |
    +                               + 
    |                           |   |
    +                          -+  -+ 
    |  2        |                   |
    +          -+     +-            + 
    |                 |             |
    +    -+                      -+ + 
    |     |        3              | |
    +-                              + 
    |             |0                |
    + +-          +-                + 
    | |                     |       |
    +             +-+-+     +-      + 
    |             |   |             |
    +             +   +             + 
    |             |   |             |
    +             +-+-+             + 
    |       |                 |     |
    +       +-  +-            +-    + 
    |           |                   |
    +-                              + 
    |                   |           |
    +              -+  -+          -+ 
    |               |               |
    +  -+                        -+ + 
    |   |                         | |
    +                   +-          + 
    |      ⬜|           |           |
    +      -+                       + 
    |         |             |       |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 
    Timoleon, entrez votre mouvement 'num,direction', 'undo' ou 'q' (quit) : 3,N
    
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 
    |1      |      3    |           |
    +                               + 
    |                           |   |
    +                          -+  -+ 
    |  2        |                   |
    +          -+     +-            + 
    |                 |             |
    +    -+                      -+ + 
    |     |                       | |
    +-                              + 
    |             |0                |
    + +-          +-                + 
    | |                     |       |
    +             +-+-+     +-      + 
    |             |   |             |
    +             +   +             + 
    |             |   |             |
    +             +-+-+             + 
    |       |                 |     |
    +       +-  +-            +-    + 
    |           |                   |
    +-                              + 
    |                   |           |
    +              -+  -+          -+ 
    |               |               |
    +  -+                        -+ + 
    |   |                         | |
    +                   +-          + 
    |      ⬜|           |           |
    +      -+                       + 
    |         |             |       |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 
    Timoleon, entrez votre mouvement 'num,direction', 'undo' ou 'q' (quit) : 1,S
    
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 
    |       |      3    |           |
    +                               + 
    |                           |   |
    +                          -+  -+ 
    |  2        |                   |
    +          -+     +-            + 
    |                 |             |
    +    -+                      -+ + 
    |1    |                       | |
    +-                              + 
    |             |0                |
    + +-          +-                + 
    | |                     |       |
    +             +-+-+     +-      + 
    |             |   |             |
    +             +   +             + 
    |             |   |             |
    +             +-+-+             + 
    |       |                 |     |
    +       +-  +-            +-    + 
    |           |                   |
    +-                              + 
    |                   |           |
    +              -+  -+          -+ 
    |               |               |
    +  -+                        -+ + 
    |   |                         | |
    +                   +-          + 
    |      ⬜|           |           |
    +      -+                       + 
    |         |             |       |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 
    Timoleon, entrez votre mouvement 'num,direction', 'undo' ou 'q' (quit) : 3,E
    
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 
    |       |          3|           |
    +                               + 
    |                           |   |
    +                          -+  -+ 
    |  2        |                   |
    +          -+     +-            + 
    |                 |             |
    +    -+                      -+ + 
    |1    |                       | |
    +-                              + 
    |             |0                |
    + +-          +-                + 
    | |                     |       |
    +             +-+-+     +-      + 
    |             |   |             |
    +             +   +             + 
    |             |   |             |
    +             +-+-+             + 
    |       |                 |     |
    +       +-  +-            +-    + 
    |           |                   |
    +-                              + 
    |                   |           |
    +              -+  -+          -+ 
    |               |               |
    +  -+                        -+ + 
    |   |                         | |
    +                   +-          + 
    |      ⬜|           |           |
    +      -+                       + 
    |         |             |       |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 
    Timoleon, entrez votre mouvement 'num,direction', 'undo' ou 'q' (quit) : undo
    
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 
    |       |      3    |           |
    +                               + 
    |                           |   |
    +                          -+  -+ 
    |  2        |                   |
    +          -+     +-            + 
    |                 |             |
    +    -+                      -+ + 
    |1    |                       | |
    +-                              + 
    |             |0                |
    + +-          +-                + 
    | |                     |       |
    +             +-+-+     +-      + 
    |             |   |             |
    +             +   +             + 
    |             |   |             |
    +             +-+-+             + 
    |       |                 |     |
    +       +-  +-            +-    + 
    |           |                   |
    +-                              + 
    |                   |           |
    +              -+  -+          -+ 
    |               |               |
    +  -+                        -+ + 
    |   |                         | |
    +                   +-          + 
    |      ⬜|           |           |
    +      -+                       + 
    |         |             |       |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 	
    Timoleon, entrez votre mouvement 'num,direction', 'undo' ou 'q' (quit) : 0,N
    
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 
    |       |      3    |           |
    +                               + 
    |              0            |   |
    +                          -+  -+ 
    |  2        |                   |
    +          -+     +-            + 
    |                 |             |
    +    -+                      -+ + 
    |1    |                       | |
    +-                              + 
    |             |                 |
    + +-          +-                + 
    | |                     |       |
    +             +-+-+     +-      + 
    |             |   |             |
    +             +   +             + 
    |             |   |             |
    +             +-+-+             + 
    |       |                 |     |
    +       +-  +-            +-    + 
    |           |                   |
    +-                              + 
    |                   |           |
    +              -+  -+          -+ 
    |               |               |
    +  -+                        -+ + 
    |   |                         | |
    +                   +-          + 
    |      ⬜|           |           |
    +      -+                       + 
    |         |             |       |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 
    Timoleon, entrez votre mouvement 'num,direction', 'undo' ou 'q' (quit) : 0,W
    
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 
    |       |      3    |           |
    +                               + 
    |0                          |   |
    +                          -+  -+ 
    |  2        |                   |
    +          -+     +-            + 
    |                 |             |
    +    -+                      -+ + 
    |1    |                       | |
    +-                              + 
    |             |                 |
    + +-          +-                + 
    | |                     |       |
    +             +-+-+     +-      + 
    |             |   |             |
    +             +   +             + 
    |             |   |             |
    +             +-+-+             + 
    |       |                 |     |
    +       +-  +-            +-    + 
    |           |                   |
    +-                              + 
    |                   |           |
    +              -+  -+          -+ 
    |               |               |
    +  -+                        -+ + 
    |   |                         | |
    +                   +-          + 
    |      ⬜|           |           |
    +      -+                       + 
    |         |             |       |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 
    Timoleon, entrez votre mouvement 'num,direction', 'undo' : ou 'q' (quit)0,N
    
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 
    |0      |      3    |           |
    +                               + 
    |                           |   |
    +                          -+  -+ 
    |  2        |                   |
    +          -+     +-            + 
    |                 |             |
    +    -+                      -+ + 
    |1    |                       | |
    +-                              + 
    |             |                 |
    + +-          +-                + 
    | |                     |       |
    +             +-+-+     +-      + 
    |             |   |             |
    +             +   +             + 
    |             |   |             |
    +             +-+-+             + 
    |       |                 |     |
    +       +-  +-            +-    + 
    |           |                   |
    +-                              + 
    |                   |           |
    +              -+  -+          -+ 
    |               |               |
    +  -+                        -+ + 
    |   |                         | |
    +                   +-          + 
    |      ⬜|           |           |
    +      -+                       + 
    |         |             |       |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 
    Timoleon, entrez votre mouvement 'num,direction', 'undo' ou 'q' (quit) : 0,E
    
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 
    |      0|      3    |           |
    +                               + 
    |                           |   |
    +                          -+  -+ 
    |  2        |                   |
    +          -+     +-            + 
    |                 |             |
    +    -+                      -+ + 
    |1    |                       | |
    +-                              + 
    |             |                 |
    + +-          +-                + 
    | |                     |       |
    +             +-+-+     +-      + 
    |             |   |             |
    +             +   +             + 
    |             |   |             |
    +             +-+-+             + 
    |       |                 |     |
    +       +-  +-            +-    + 
    |           |                   |
    +-                              + 
    |                   |           |
    +              -+  -+          -+ 
    |               |               |
    +  -+                        -+ + 
    |   |                         | |
    +                   +-          + 
    |      ⬜|           |           |
    +      -+                       + 
    |         |             |       |
    +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+ 
    Timoleon, entrez votre mouvement 'num,direction', 'undo' ou 'q' (quit) : 0,S
    
    Gagné !!
    
    Bravo Timoleon, vous avez réussi en 8 coups et 1 retour en arrière.
    
    >>> 


## III. Résolution automatique du jeu

Dans cette partie, on s'intéresse à la résolution automatique du jeu `IceWalker` : 
à partir des positions initiales du joueur, il faut fournir une suite de mouvements 
permettant d'arriver à la case finale.

Voici un exemple de résolution (ici la case d'arrivée est représentée par le caractère "X", situé aux coordonnées \((8,9)\).

    +-+-+-+-+-+-+-+-+-+-+ ┌────────────────────────────────────────────────┐
    |                   | │objectif : (8, 9), solution :                   │
    +                   + │1 : (9, 3) -> (9, 0)                            │
    |                   | |0 : (3, 2) -> (9, 2)                            │
    +                   + │0 : (9, 2) -> (9, 9)                            │
    |      0            | │0 : (9, 9) -> (8, 9)                            │
    +                   + │                                                │
    | |               |1| │                                                │
    +-+-   -+-+-+-+-+-+ + │                                                │
    |                   | │                                                │
    +                   + │                                                │
    |                   | │                                                │
    +                   + │                                                │
    |                   | │                                                │
    +                   + │                                                │
    |                   | │                                                │
    +                   + │                                                │
    |                   | │                                                │
    +                   + │                                                │
    |                X  | └────────────────────────────────────────────────┘
    +-+-+-+-+-+-+-+-+-+-+

Ajoutez à la classe modélisant le jeu les méthodes nécessaires à cette résolution automatique.

## IV. Extensions envisagées

### Gérer les scores

On veut proposer une gestion des scores des utilisateurs. 

Les grilles sont plus ou moins difficiles : on peut définir la difficulté d'une grille comme le nombre minimum de coups à effectuer pour la résoudre.

Lorsqu'un utilisateur joue (on se contentera d'identifier un joueur par son nom), son résultat est enregistré dans une base de données. Ce résultat peut prendre la forme du nombre de coups et de retours en arrière qui ont été nécessaires pour atteindre la case finale.

On veut pouvoir déterminer :

-   pour une grille donnée, le meilleur joueur ;
-   pour un joueur donné, la grille qui est la plus ou la moins réussie ;
-   le meilleur joueur (les scores seront pondérés par la difficulté de la grille).

Définissez une ou plusieurs tables pour mettre en &oelig;uvre cette extension.
Vous fournirez alors les scripts sql de création de cette base.


### Représentation graphique

Sans modifier la classe de base, écrire des fonctions permettant la représentation graphique du plateau de jeu.

Vous pourrez utiliser :

-   tkinter
-   pygame


### Des trous dans la grille

Sur le lac gelé certaines cases ont dégelé : dès qu'on marche dessus on a perdu.


## V. Indications

On crée un fichier `grid.py` pour définir la classe  `grid`  dans lequel on importe le module `grid_square` qui définit la classe `case`  que l'on définira dans un deuxième temps.

La classe grid possédera les attributs suivants :

- width : la largeur de la grille ;
- height : la hauteur de la grille ;
- grid : la grille formée des instances case() définies dans le module grid_square ; 
- nb_players qui représente le nombre de joueurs
- all_players qui est un dictionnaire dont les clés seront les numéros de joueurs et les valeurs, les coordonnées de ceux-ci.

On se donne également une série de méthodes à compléter.

**grid.py**

```python
#importation des modules
import random

from grid_square import case

class grid:#nouvelle class pour la grille de jeu
    
    def __init__(self, width, height):
        """
        constructeur de la classe
        """
            
    def get_case(self, x, y):
        """
        retourne le contenu de la case de coordonnées x y dans la grille
        """
        pass
    
    def get_grid(self):
        """
        retourne la grille
        """
        pass
    
    def get_width(self):
        """
        retourne la largeur de la grille
        """
        pass

    def get_height(self):
        """
        retourne la hauteur de la grille
        """
        pass
    
    # players management
    
    def get_nb_players(self):
        """
        retourne le nombre de joueurs présents sur la grille
        """
        pass
    
    def incr_nb_players(self):
        """
        incrémente (augmente de 1) le nombre de joueurs présents sur la grille
        """
        pass        
     
    def get_all_players(self):
        """
        retourne le dictionnaire contenant les positions de tous les joueurs présents sur la grille
        """
        pass
        
    def add_player(self, x,y):
        """
        ajoute/place un joueur sur la grille
        """
        #on enregistre la position du nouveau joueur dans le dictionnaire
        #on ajoute le numéro du nouveau joueur dans la grille
        #on incrémente le nombre de joueurs
        
    def add_all_players(self, dictionnary):
        """
        #place sur la grille tous les joueurs dont les positions sont enregistrées dans le dictionnaire passé en paramètre
        """
				pass
    
    def add_win(self, x,y):#pour ajouter une case victoire
        """
        place la case à atteindre (objectif) codée par un carré sur la grille
        """
        #symbole en forme de carré chr(9633)
    
    def add_wall(self, x,y,direction):
        """
        place le mur (Est ou Sud) sur la grille dans la case de coordonnées x,y
        """
				pass
    
    def get_player_position(self, player):
        """
        retourne la position (tuple de coordonnées) du joueur dont le numéro est passé en paramètre
        """
        #récupérer la position d'un joueur
    
    #effacement de tous les joueurs de la grille
    
    def delete_all_players(self):
        """
        efface tous les joueurs de la grille
        """
        #pour chaque joueur (numéro du joueur <=> clé du dico)
        #on récupère la position du joueur x,y
        #on vide la case de la grille
        #le nombre de joueur devient nul 
        #le dictionnaire qui stocke la position de chaque joueur se vide
    
    def move_player(self,player,direction):
        """
        gestion du déplacement d'un joueur dont le numéro (int) est passé en paramètre
        dans la direction ("E","W","S" ou "N") passée en paramètre
        """
        #on récupére la position du joueur
        #déplacement vers l'EST
        #désigne la case considérée
				#tant que le joueur passé en paramètre peut se déplacer sans rencontrer d'obstacle (limite, mur) pour aller dans une case libre 
						#on enlève le joueur de sa case
            #déplacement horizontal vers la droite
            #on modifie les coordonnées du joueur dans le dictionnaire
						#on place le joueur dans la case              
      	#déplacement vers le SUD
				#déplacement vers l'OUEST
				#déplacement vers le NORD    
               
    def create_grid_from_file(filename):
        """
        créer une grille à partir d'un fichier texte
        g = grid.create_grid_from_file("...")     
        """
        pass
        
    def __str__(self):
        '''
        construit une représentation de la grille sous forme d'une chaine de caractère
        retourne la chaine de caractères construite
        '''
				# a first line of '-+ '
        
				#mur vertical "|" si mur EST présent
   			#mur horizontal "---" si mur SUD présent
				#retourne la chaine de caractères construite (représentation graphique de la grille)
    
#tests:
"""
G=grid(5,8)
G.add_player(5,5)
#G.add_player(3,3)
#G.add_player(4,3)
#G.add_player(4,2)

G.add_wall(1,1,'E')
G.add_wall(4,3,'S')
G.add_wall(2,7,'S')
G.add_win(2,5)
print(str(G))

G.move_player(0,'W')
print(str(G))
#G.move_player(2,'N')
#print(str(G))
#G.move_player(1,'W')
#print(str(G))
#G.move_player(2,'W')
#print(str(G))
"""

```

Étape 1 : créer et afficher la grille

Une grille est caractérisée par sa largeur width et sa hauteur height. 

Ce seront deux attributs d'instance donnés en paramètre.

On se donne également comme attributs de la classe Grid 

- la grille elle-même : grid, une liste définie par compréhension.

- le nombre de joueurs : nb_players, un entier

- tous les joueurs sous la forme d'une bibliothèque : all_players

  **grid_square.py**

```python

class case:#nouvelle classe pour une case de la grille
    
    EMPTY = ' '
    
    def __init__(self):
        """
        initialise la case
        """
        self.__contents = None
        self.__Swall=False
        self.__Ewall=False
            
    def is_empty(self):
        """
        test si la case est libre
        retourne un booléen
        """
        pass
    
    def is_player(self):
        """
        teste si la case contient un joueur (int)
        retourne un booléen
        """
        pass
    
    def is_win(self):
        """
        teste si la case contient l'objectif (codé par un "carré")
        retourne un booléen
        """
        pass
    
    def get_contents(self):
        """
        retourne le contenu de la case
        """
        pass
    
    def have_Swall(self):
        """
        teste si la case possède un mur au Sud
        retourne un booléen
        """
        pass
    
    def have_Ewall(self):
        """
        teste si la case possède un mur à l'EST
        retourne un booléen
        """
        pass
           
    def set_contents(self, truc):#truc is None, "win", player(int)
        """
        définit le contenu (passé en paramètre) de la case : None, "win" , player (int)
        """
        pass
    
    def build_Swall(self):
        """
        définit si la case possède un mur au Sud (booléen)
        """
        pass
        
    def build_Ewall(self):
        """
        définit si la case possède un mur à l'EST (booléen)
        """
        pass    
    
    def empty(self):
        """
        pour vider une case de son contenu (joueur ou win)
        """
        pass
            
    def __str__(self):
        if not self.is_empty() :
            return str(self.__contents)
        else:
            return case.EMPTY

```

**main.py**

```python
#importation
from grid import grid
from grid_square import case

def answer_is_correct(ans,cas_undo):
    """
    fonction permettant de vérifier si la réponse (ans) passée en paramètre est "correcte"
    cad si l'utilisateur répond
    - q pour quitter
    - undo (s'il a le droit de répondre undo)
    - un déplacement convenablement codé comme la consigne le précise
    retourne un booleen
    
    """
		pass

def difference_between_dictionnaries(dico1,dico2):
    """
    fonction retournant une chaine de caractère codant le déplacement pour passer d'une situation à une autre
    ces 2 situations étant codées chacune par un dictionnaire
    on recherche la différence (unique) entre les valeurs (=coordonnées) des 2 dictionnaires pour une même clé (joueur)
    on code le déplacement par la clé (joueur se déplaçant), suivie de la direction (N,S,E,W) suivie des coordonnées initiales (dico1), suivie des coordonnées atteintes (dico2) 

    >>>difference_between_dictionnaries({0:(9,4),1:(4,5),2:(8,9),3:(9,7)},{0:(9,1),1:(4,5),2:(8,9),3:(9,7)})
    '0,N: (9, 4) -> (9, 1)'
    
    >>> difference_between_dictionnaries({0:(9,4),1:(4,5),2:(8,9),3:(9,7)},{0:(9,4),1:(4,5),2:(8,3),3:(9,7)})
    '2,N: (8, 9) -> (8, 3)'
    """
    pass

def print_move_list_solution(dico_list):
    """
    procédure permettant d'afficher successivement les déplacements pour passer d'une situation à la suivante
    prenant en paramètre la liste des situations (codées chacune par un dictionnaire : clé(joueur) valeur(position))
    >>> print_move_list_solution([{0:(9,4),1:(4,5),2:(8,9),3:(9,7)}, {0:(9,1),1:(4,5),2:(8,9),3:(9,7)}, {0:(9,1),1:(4,5),2:(8,9),3:(9,3)},{0:(9,1),1:(4,5),2:(4,9),3:(9,3)}])
    0,N: (9, 4) -> (9, 1)
    3,N: (9, 7) -> (9, 3)
    2,W: (8, 9) -> (4, 9)
    """
    pass

class IceWalker:#nouvelle classe du jeu
    
    def __init__(self,my_grid):
        self.__my_grid = my_grid
        self.__player_name=""
        self.__number_of_move=0
        self.__number_of_undo=0
        self.__list_of_undo=[]
        self.__final_case_location=()
        
    
    def set_final_case_location(self):
        """
        définit l'objectif ("case") à atteindre (tuple de coordonnées)
        """
				pass
                
    def get_final_case_location(self):
        """
        retourne l'objectif ("case") à atteindre (tuple de coordonnées)
        """
        pass
        
    def get_grid(self):
        """
        retourne la situation
        """
        pass
    
    def get_player_name(self):
        """
        retourne le nom de l'avatar de l'utilisateur
        """
        pass
            
    def set_player_name(self):
        """
        définit le nom de l'avateur de l'utilisateur (en lui posant la question)
        """
        pass
        
    def get_number_of_move(self):
        """
        retourne le nombre de déplacement
        """
        pass
    
    def get_number_of_undo(self):
        """
        retourne le nombre de "retour en arrière" (undo, annulation du dernier déplacement)
        """
        pass
    
    def incr_number_of_move(self):
        """
        augmente de 1 (incrémentation) le nombre de déplacement
        """
        pass
        
    def incr_number_of_undo(self):
        """
        augmente de 1 (incrémentation) le nombre d'annulation du dernier coup
        """
        pass
        
    def get_list_of_undo(self):
        """
        retourne la liste des situations atteintes pour pouvoir les annuler (undo)
        """
        pass
        
    def save_undo(self,all_players):
        """
        enregistre la situation pour pourvoir revenir en arrière (undo)
        """
        #all_players est un dictionnaire dont les clés sont le numéro des joueurs, et les valeurs leurs coordonnées (x,y)
        
    #gestion du jeu
        
    def play(self):
        """
        procédure de gestion du jeu en "manuel" par l'utilisateur
        pour tenter de réussir sa partie
        choix : quit, undo (s'il peut revenir en arrière) ou déplacement d'un joueur dans une direction choisie
        affichage de la situation
        affichage du nombre de coups (et de undo) lorsque le joueur 0 atteint l'objectif ("victoire")
        
        """
        
        #tant que le joueur 0 n'a pas atteint l'objectif
        #si l'utilisateur n'a pas le droit d'annuler son dernier coup (il a fait autant de déplacement que de undo : position de départ)
        #on demande à l'utilisteur ce qu'il veut faire
				#on repose la question jusqu'à ce que la réponse soit correcte
				#si l'utilisateur a le droit d'annuler son dernier coup
        #on demande à l'utilisateur ce qu'il veut faire
				#on repose la question jusqu'à ce que la réponse soit correcte
				#L'utilisateur quite la partie : bye bye
				#Annulation du dernier coup
				#on efface tous les joueurs
				#on efface la position actuelle de la liste des undo
				#on recharge les joueurs de la position précédente (qui a été enregistrée)
				#on incrémente le nombre de undo (pour le score)
        #on affiche la situation
        #on vérifie que le coup annulé (situation) a été supprimé de la liste des undo
				 #Analyse du déplacement codé par l'utilisateur
         #on découpe sa réponse
         #identification du joueur déplacé
         #identification de la direction choisie
				 #déplacement du joueur
				 #incrémentation du nombre de déplacement (pour le score)
				#on sauvegarde la situation atteinte dans la liste des undo (pour pouvoir éventuellement l'annuler)
				#affichage de la situation sous forme de grille
				#si en se déplaçant le joueur 0 atteint l'objectif
				#affichage des félicitations + nb de coups + nb de undo

  
    def neighbours_list(self,dictionnary):
        """
        fonction qui retourne la liste des voisins d'un sommet
        cad la liste des situations accessibles en 1 seul déplacement depuis une situation (sommet) passé en paramètre
        prenant en paramètre un dictionnaire : situation considérée (positions des joueurs)
        """
        #liste initialement vide
        
        #déplacements envisageables

        
        #pour chaque joueur de la situation considérée
            
        #on envisage tous les déplacements
        #on efface 
        #on repositionne les joueurs dans leur positions 
        #on effectue 1 seul déplacement
        #on enregistre la nouvelle situation (=voisin) accessible en 1 seul déplacement
                   
    
    def but_atteint(self,dico):
        """
        fonction prenant en paramètre un dictionnaire
        retournant un booleen:
        True si la clé 0 du dictionnaire (=position enregistrée du joueur 0 dans une situation donnée)
        correspond aux coordonnées de l'objectif (cad si le joueur 0 a atteint le but)
        False sinon
        """
        pass
    
    
    def solve(self):
        """
        procédure de résolution : parcourt en largeur du graphe 
        """
        #on détermine la position de l'objectif
        #on enregistre la situation de départ (=la position des joueurs en début de partie) dans un dico
        
        #recherche du plus court chemin (parcourt du graph en largeur)
        #liste des sommets déjà visités (=marqués) initialement vide
        #dictionnaire pour enregistrer les parents d'un sommet
        #liste des situations (dico) à traiter, contenant initialement la situation de départ
        
        #on "marque" la situation de départ
        #pas de parent
        
				#on "défile" le sommet de aTraiter (cad qu'on considère le premier élément qu'on enlève de la liste)
            
         #si on a atteint le but
				 #c'est gagné !
         #sinon
				#on définit la liste des voisins du sommet considéré
         #pour chaque voisin de la liste des voisins
         #si le voisin n'est déjà marqué
         #on marque le voisin
         #on enregistre son parent
         #on "enfile" le voisin
                        
        #the goal can be achieved
            
         #on construit le plus court chemin en remontant les parents
            
         #affichage du nombre de coups minimal     

        """
if __name__ == '__main__':
    main()
"""
        
#tests
g = grid.create_grid_from_file("grid01.txt")#création d'une grille à partir d'un fichier
print(g)#affichage de la situation initiale
game=IceWalker(g)
game.play() #Pour jouer manuellement en suivant les instructions de l'utilisateur
#game.solve() #Pour résoudre automatiquement et de façon optimale

```
