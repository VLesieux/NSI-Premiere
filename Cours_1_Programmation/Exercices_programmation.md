# Exercices de programmation en Python

Il est demandé d'écrire les docstring pour toutes les fonctions en utilisant les résultats escomptés en sortie lorsque ceux-ci sont donnés (à partir de l'exercice 3).

```Python
if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)
```

## Exercice 1

Soit le code suivant. Déterminer la valeur finale de x. Utiliser un papier et un stylo. 

```Python
x=1
n=5
while n>1:
    x=x*n
    n=n-1
```
Vérifier avec Thonny en ajoutant :

```Python
print("La valeur de n est : ",n,", et la valeur de x est : ",x,".")
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
Vérifier avec Thonny en ajoutant l'instruction  ```print(x)``` pour afficher la valeur de x.  
Utilisez le **debugger** de Thonny pour exécuter le programme pas-à-pas.

## Exercice 3

Écrire une fonction `somme_premiers_carre` qui prend en paramètre un entier strictement positif k et renvoie la somme des k premiers carrés non nuls : `1+2**2+3**3+.....k*k`.

```Python
>>> print(somme_premiers_carre(3))
14
```

## Exercice 4

1. Écrire une fonction _somme_diviseurs_ qui prend en paramètre un entier naturel non nul et renvoie la somme de ses diviseurs. Un diviseur d'un entier n est un entier dont n est un multiple. Par exemple les diviseurs de 9 sont : 1, 3, 9.

```Python
>>> print(somme_diviseurs(9))
13
```

2. Un entier naturel n est parfait si la somme de ses diviseurs est égale à son double 2*n. Écrire une fonction _est_parfait_ qui prend en argument un entier naturel non nul et renvoie True s'il est parfait et False sinon.

```Python
>>> est_parfait(6)
True
```

3. Déterminer les nombres parfaits inférieurs à 100 puis le premier nombre parfait supérieur à 100.


## Exercice 5

1. Écrire une fonction _est_premier_ qui prend en paramètre un nombre entier et renvoie True si ce nombre est premier et False sinon. Un nombre premier est un nombre qui ne peut être divisé que par 1 et par lui-même. 

```Python
>>> est_premier(13)
True
>>> est_premier(6)
False
```

2. Écrire une fonction _premiers_ qui prend en paramètre un nombre entier et renvoie la liste de tous les nombres premiers inférieurs strictement à ce nombre. 1 n'est pas considéré comme premier.

```Python
>>> premiers(10)
[2, 3, 5, 7]
```


## Exercice 6

Écrire un fonction qui détermine le pourcentage de 6 après n lancers de dés. Utiliser la fonction randint du module random (voir deux manières d'importer la fonction) après avoir recherché sa documentation.

## Exercice 7

Écrire une fonction _double_ qui prend en argument un mot et renvoie le mot obtenu en doublant les unes après les autres chaque lettre du mot. 

```Python
>>> double('bon')
'bboonn'
```

On envisagera deux écritures possibles pour la fonction ; soit en parcourant les lettres constitutives du mot, soit en repérant les lettres par leur indice de position dans le mot.

## Exercice 8

1. Écrire une fonction qui prend en argument un mot et renvoie True si le mot commence ou se termine par la même lettre et False sinon.

```Python
>>> a_meme_debut_et_fin("tout")
True
```

2. Écrire une fonction qui prend en argument deux mots et renvoie True si les deux mots commencent par la même lettre et se terminent également par la même lettre et False sinon.

```Python
>>> meme_debut_et_fin("tomba","tonna")
True
>>> meme_debut_et_fin("tombai","tonna")
False
```


## Exercice 9

On utilise le module Turtle que l'on importera dans sa totalité, on utilise les fonctions forward, left après avoir lu leur documentation.
1. Construire vingt carrés de côté variant de 10 à 200 pixels par pas de 10. Les carrés sont inclus les uns dans les autres et ont un sommet commun. On définira une fonction _carre_ admettant le paramètre _n_ chargée de représenter un carré de côté _n_.

<img width="400" height="400" src="assets/turtle1.png">

2. Construire vingt carrés de côté variant de 10 à 200 pixels par pas de 10. Chaque carré est incliné de 18 degrés par rapport au précédent et les carrés ont un sommet commun.

<img width="400" height="400" src="assets/turtle2.png">

## Exercice 10

Écrire une fonction qui trace, à l'aide de la bibliothèque Matplotlib, la courbe représentative de la fonction f(x) sur un intervalle [a;b] en utilisant n points. On importe au préalable le module pyplot de Matplotlib. Écrire une fonction _trace_ qui prend en arguments deux nombres a et b, une fonction f et un entier n. L'appel _trace(a,b,f,n)_ permet d'obtenir le tracé de la courbe.

```Python
import matplotlib.pyplot as plt
def f(x):
    return x**2 
trace(-5,5,f,100)
```

<img width="400" height="400" src="assets/graphe.png">

```Python
plt.plot(x,y)#représente y en fonction de x
plt.grid()
plt.show()
```