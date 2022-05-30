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
-   il abandonne la partie (il n'est parfois plus possible de rejoindre la case finale si une mauvaise direction a été prise)


