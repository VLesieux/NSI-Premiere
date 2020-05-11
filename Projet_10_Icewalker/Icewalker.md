Projet Icewalker
================

## I. Présentation du jeu

Marcher sur la glace est un exercice périlleux :

-   on ne peut pas changer de direction
-   il est difficile de s'arrêter.

Dans ce projet, nous allons nous intéresser à la programmation d'un jeu dans lequel
le joueur incarnera un personnage se déplaçant sur la glace.

Le terrain est :

-   rectangulaire
-   entièrement constitué de cases gelées, à l'exception d'une seule case appelée **case finale**. Toutefois un mur peut être placé sur un segment adjacent à deux cases.
-   entouré de murs.

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

Créez une classe permettant de modéliser le plateau du jeu. Voici les fonctionnalités de 
cette classe : 

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

La définition d'une classe pour modéliser les cases du plateau peut s'avérer pertinent. 
Une case peut posséder ou non des murs dans différentes directions, contenir ou non un joueur et être ou non la case finale.

Il vous faudra également une classe pour modéliser le jeu. Un jeu est paramétré par un plateau de jeu.
La fonctionalité principale de cette classe pourrait être :

-	Permettre de jouer au jeu de manière interactive.

- Retours en arrière (undo) : parfois, on s'aperçoit qu'un mouvement nous a été fatal : on est certain de ne plus pouvoir atteindre la sortie. En utilisant une structure de données adaptée, faites en sorte que l'on puisse revenir en arrière dans l'historique des coups joués. On doit éventuellement pouvoir revenir plusieurs coups en arrière, jusqu'à la configuration initiale. On pourra appliquer une pénalité au score pour chaque retour en arrière effectué.

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

