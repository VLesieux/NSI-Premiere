# Exercices de programmation en Python

## Exercice 1

Soit le code suivant. Déterminer la valeur finale de x. Utiliser un papier et un stylo.

```Python
x=1
n=5
while n>1:
    x=x*n
    n=n-1
```

## Exercice 2

Soit le code suivant. Déterminer la valeur finale de x. Utiliser un papier et un stylo.

```Python
x=0
for i in range(2):
    x=x+i
    for j in range(3):
        x=x+j
```

## Exercice 3

Écrire une fonction qui prend en paramètre un entier strictement positif k et renvoie la somme des k premiers carrés non nuls.


## Exercice 4

1. Écrire une fonction _somme_diviseur_ qui prend en paramètre un entier naturel non nul et renvoie la somme de ses diviseurs. Un diviseur d'un entier n est un entier dont n est un multiple.
2. Un entier naturel n est parfait si la somme de ses diviseurs est égale à 2n. Écrire une fonction _est_parfait_ qui prend en argument un entier naturel non nul et renvoie True s'il est parfait et False sinon.
3. Déterminer les nombres parfaits inférieurs à 100 puis les trois premiers nombres parfaits.


## Exercice 5

1. Écrire une fonction _est_premier_ qui prend en paramètre un nombre entier et renvoie True si ce nombre est premier et False sinon. Un nombre premier est un nombre qui ne peut être divisé que par 1 et par lui-même.
2. Écrire une fonction _premiers_ qui prend en parmètre un nombre entier et renvoie la liste de tous les nombres premiers inférieurs strictement à ce nombre.

## Exercice 6

Écrire un fonction qui détermine le pourcentage de 6 après n lancers de dés. Utiliser la fonction randint du module random après avoir recherché sa documentation.

## Exercice 7

Écrire une fonction _double_ qui prend en argument un mot et renvoie le mot obtenu en doublant chaque lettre du mot. Par exemple double("bon") donne "bboonn".

## Exercice 8

1. Écrire une fonction qui prend en argument un mot et renvoie True si le mot commence ou se termine par la même lettre et False sinon.
2. Écrire une fonction qui prend en argument deux mots et renvoie True si les deux mots commencent par la même lettre et se terminent par la même lettre et False sinon.
