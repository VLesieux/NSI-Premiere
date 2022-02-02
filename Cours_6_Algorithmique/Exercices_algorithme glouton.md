## Exercices sur l'algorithme glouton

Pour les doctests :

```python
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
```

1. Le rendu de monnaie

Contexte du problème : on suppose que l'on dispose d'un nombre illimité de pièces de 2cts, 5cts, 10cts, 50cts et 1 euro(100 cts).
Le problème est le suivant : " comment rendre la monnaie en un minimum de pièces ? ".

On peut proposer une méthode de résolution dite " gloutonienne " qui consiste à rendre en premier lieu des pièces de plus grande valeur avec toujours la condition que cette pièce de plus grande valeur ait une valeur inférieure à la somme à rendre et cela jusqu'à ce que la somme à rendre soit égale à zéro.

Exemple : supposons que l'on ait 1 € 77 cts ou 177 cts à rendre ; le rendu des pièces de manière gloutonne sera le suivant : une pièce de 1 €, 1 pièce de 50 cts, 1 pièce de 10 cts, 1 pièce de 10 cts, 1 pièce de 5 cts, 1 pièce de 2 cts ; soit un total de 6 pièces.

On peut proposer l'implémentation suivante en python : 

```python
def rendu_monnaie_glouton(somme,pieces):
    """
    Renvoie les pièces à rendre selon un algorithme glouton
    param : somme : int
    param : pieces : list
    return : list
    >>> rendu_monnaie_glouton(177,[100,50,10,5,2])
    [100, 50, 10, 10, 5, 2]
    """
```
Indication : créer une liste vide `rendu` puis réaliser, par compréhension, une liste `difference` contenant les valeurs `somme-valeur` pour toutes les `valeur` dans `pièces` et prendre la valeur minimale parmi les valeurs positives ou nulles. Prendre l'opposé de cette valeur minimale ajouté de la valeur de `somme`, pour récupérer la valeur de la pièce choisie et ajouter cette valeur à la liste `rendu`. Retrancher à somme la valeur de cette pièce et poursuivre le processus aussi longtemps que somme>0.

L'algorithme glouton propose une solution mais attention, celle-ci n'est pas toujours optimale !
Pour s'en rendre compte, travailler avec le système impérial qui est l'ancien système monétaire britannique : [30,24,12,6,3,1] et observer ce que donne l'algorithme :

```python
>>> rendu_monnaie_glouton(48,[30,24,12,6,3,1])
[30, 12, 6]
```

L'algorithme glouton propose un rendu de 3 pièces alors que la solution optimale serait bien évidemment le rendu de 2 pièces : [24,24].


2. Le problème du sac à dos

Contexte du problème : on imagine que l'on cherche à remplir un sac à dos avec des objets de valeur en maximisant la valeur totale du contenu du sac. Chaque objet ne peut être pris qu'une seule fois et possède un poids particulier. La contrainte est de ne pas dépasser un poids maximal P pour le sac.

Dans le tableau ci-dessous, on suppose que les objets ont été triés initialement par poids croissants.

<table>
<tr>
<td>objet</td><td>o1</td><td>o2</td><td>o3</td><td>o4</td><td>o5</td>
</tr>
<tr>
<td>poids</td><td>1</td><td>2</td><td>5</td><td>6</td><td>7</td>
</tr>
<tr>
<td>valeur</td><td>1</td><td>6</td><td>22</td><td>18</td><td>28</td>
</tr>
</table>

```python
lpoids=[1,2,5,6,7]
lvaleurs=[1,6,22,18,28]
```

Rappel de l'algorithme glouton : cet algorithme ne donne pas forcèment le résultat optimal mais il a le mérite de proposer une solution ; il consiste à placer d'abord l'objet de plus grande valeur de poids P1 inférieur à P, puis à prendre parmi les objets restants celui de plus grande valeur dont le poids est inférieur à P-P1, etc....

On peut donc réaliser une fonction `ks_glouton(lvaleurs, lpoids,P)` capable de nous donner la liste des indices des objets en suivant l'algortithme glouton.

Au préalable, on réalise une fonction `choix_glouton(lpoids,lvaleurs,P)` qui retourne l'indice de l'objet que l'on prend en premier.


```python
def choix_glouton(lpoids,lvaleurs,P):
    """
    : return : renvoie l'indice de l'objet
    * de poids < limite P
    * de plus grande valeur
    * qui n'est pas encore dans le sac
    s'il existe
    sinon renvoyez none
    :CU: 
    - len(lvaleurs) == len(lpoids) 
    - lpoids est triée par ordre croissant
    >>> choix_glouton(lpoids,lvaleurs,15)
    4
    >>> choix_glouton(lpoids,lvaleurs,6)
    2
    """ 
```

On crée maintenant une copie de la liste des poids, car celle-ci sera modifiée, et on réalise autant que possible des  `choix_glouton` ; pour ne pas reprendre le même poids, on donne la valeur infinie au poids qui a été sélectionné en lui donnant la valeur `math.inf` après avoir importé le module math.


```python            
from copy import deepcopy
import math 

def ks_glouton(lvaleurs, lpoids,P) :
    """
    renvoie un ensemble d'objet (indices dans lvaleurs et lpoids) pour lesquels
    un choix glouton a été effectué    
    :CU: 
    - len(lvaleurs) == len(lpoids) 
    - lpoids est triée par ordre croissant
    >>> ks_glouton(lvaleurs, lpoids,15)
    [4, 2, 1, 0]
    >>> ks_glouton(lvaleurs, lpoids,6)
    [2, 0]
    """ 
```

On définira également une fonction `interet_glouton` pour calculer le gain remporté dans le sac lorqu'on utilise cet algorithme glouton.

```python
def interet_glouton(lvaleurs, lpoids,P) :
    """
    renvoie l'interet obtenu par application de l'algorithme glouton
    >>> interet_glouton(lvaleurs, lpoids,15)
    57
    """
```