# Exercices types construits : tuples, listes et dictionnaires

## Exercice 1

Écrire une fonction _separe_ qui prend en argument un n-uplet _t_ composé d'entiers et renvoie deux listes : la première liste _pairs_ contient les nombres pairs et la seconde _impairs_ les nombres impairs.

## Exercice 2

Écrire une fonction _produit_ qui prend en paramètres une liste de nombres _nombres_ et un entier naturel _n_ non nul et qui renvoie une liste obtenue en multipliant chaque élément de la liste _nombres_ par _n_. On proposera différentes écritures et notamment une écriture en compréhension.

## Exercice 3

Voici une fonction mystère :
```Python
def mystere(liste1,liste2):
    liste=[]
    i,j=0,0
    while i<len(liste1) and j<len(liste2):
        if liste1[i]<liste2[j]:
            liste.append(liste1[i])
            i=i+1
        else:
            liste.append(liste2[j])
            j=j+1
    return liste
```
On appelle cette fonction avec l'instruction mystere([2,5,6,8],[1,4,7,8,9]). Quel est le résultat renvoyé ?   
Le trouver avant de tester sur machine.

## Exercice 5

1. Écrire une fonction _est_premier_ qui prend en paramètre un nombre entier et renvoie True si ce nombre est premier et False sinon. Un nombre premier est un nombre qui ne peut être divisé que par 1 et par lui-même.
2. Écrire une fonction _premiers_ qui prend en parmètre un nombre entier et renvoie la liste de tous les nombres premiers inférieurs strictement à ce nombre.

## Exercice 6

L'instruction tuple(sorted((a,b,c))) renvoie un triplet contenant les valeurs des nombres a,b,c rangées dans l'ordre croissant. Compléter la fonction maxi qui renvoie le plus grand des trois nombres a,b,c.

```Python
def maxi(a,b,c):
    ...=tuple(sorted((a,b,c)))
    return ...
```

## Exercice 7

On construit un dictionnaire ayant pour clés des couples contenant les coordonnées GPS de villes (Latitude et Longitude) et pour valeur les noms des villes correspondantes. On trouve les coordonnées sur Internet par exemple. Les données sont sous forme décimale en degré.      

```Python
positions={}
positions[(48.853585,2.301490)]="Paris"
positions[(11.611358,43.147752)]="Djibouti"
positions[(43.70000,7.250000)]="Nice"
```
On suppose avoir reçu une photo prise sur un smartphone par une personne en vacances. On regarde dans les propriétés les coordonnées GPS au moment de la prise de vue. Écrire une fonction prenant en paramètres un couple de coordonnées GPS et le dictionnaire construit, et renvoyant le nom du lieu correspondant. On tolère une précision au dix-millième de degré.
Par exemple si les coordonnées sont [(11.61135,43.14775)], la fonction doit nous renvoyer "Djibouti".

## Exercice 8

Écrire une fonction _stat_ qui prend en paramètre un texte et renvoie un dictionnaire dont les clés sont les différentes lettres du texte et les valeurs le nombre d'occurences de chaque lettre. On suppose le texte écrit en lettres capitales non accentuées. Le texte peut contenir des espaces ou des caractères de ponctuation qu'il ne faudra pas comptabiliser.

## Exercice 9

Réaliser un jeu de tests (une batterie de 100 tests) sur la fonction sample du module random utilisée sur une liste de 4 éléments. Vérifier que les éléments de chaque échantillon appartiennent à la liste d'origine pour des échantillons de différentes tailles.


## Exercice 10

On utilise le module Turtle que l'on importera dans sa totalité, on utilise les fonctions forward, left après avoir lu leur documentation.
1. Construire vingt carrés de côté variant de 10 à 200 pixels par pas de 10. Les carrés sont inclus les uns dans les autres et ont un sommet commun. On définira une fonction _carre_ admettant le paramètre _n_ chargée de représenter un carré de côté _n_.
2. Construire vingt carrés de côté variant de 10 à 200 pixels par pas de 10. Chaque carré est incliné de 18 degrés par rapport au précédent et les carrés ont un sommet commun.


## Exercice 11

Écrire une fonction qui trace, à l'aide de la bibliothèque Matplotlib, la courbe représentative de la fonction f sur un intervalle [a;b] en utilisant n points. On importe au préalable le module pyplot de Matplotlib. Écrire une fonction _trace_ qui prend en arguments deux nombres a et b, une fonction f et un entier n. L'appel _trace(a,b,f,n)_ permet d'obtenir le tracé de la courbe.



