
**Projet : LABYRINTHE**










Le projet consiste à résoudre un labyrinthe. 10 tests sont à valider.

```Python
if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)
```

<img src="Assets/lab1.png">


La représentation du labyrinthe ci-dessus se fait sous la forme d'une liste à deux dimensions (matrice) 
de la manière suivante : 

0 pour un espace vide ; 
1 pour un mur ; 
2 pour l'entrée ; 
3 pour la sortie.

```Python
labyrinthe=[
[1,1,1,1,1,0,0,0,0,0,1],
[1,0,0,0,1,0,1,0,1,0,1],
[1,0,1,0,1,0,1,0,1,0,1],
[1,0,1,0,1,0,1,0,1,0,1],
[1,0,1,0,1,0,1,0,1,0,1],
[2,0,1,0,0,0,1,0,1,0,3],
[1,1,1,1,1,1,1,0,1,0,1],
[1,0,0,0,1,0,0,0,1,0,1],
[1,0,1,0,1,0,1,1,1,0,1],
[1,0,1,1,1,0,1,0,0,0,1],
[1,0,0,0,0,0,1,1,0,1,1]
      ]
```

On utilise également ce labyrinthe plus simple pour réaliser nos tests.

```Python
lab1=[
[1,1,1,1,1,1,1],
[2,0,0,0,0,0,1],
[1,1,1,1,1,0,1],
[1,0,1,0,0,0,1],
[1,0,1,0,1,0,1],
[1,0,0,0,1,0,1],
[1,1,1,1,1,3,1]
    ]

```
 <img src="Assets/lab2.png">


```Python
def representation(graphe):
    """
    Affiche une représentation du graphe
    param : graphe : list
    return : None
    >>> representation(lab1)
    ⬛⬛⬛⬛⬛⬛⬛
    ⬜⬜⬜⬜⬜⬜⬛
    ⬛⬛⬛⬛⬛⬜⬛
    ⬛⬜⬛⬜⬜⬜⬛
    ⬛⬜⬛⬜⬛⬜⬛
    ⬛⬜⬜⬜⬛⬜⬛
    ⬛⬛⬛⬛⬛⬜⬛
    """
	pass

```
indication : le passage à la ligne se fait avec `print("\n")`

pour supprimer le dernier passage à la ligne, on peut écrire : `texte=texte.strip("\n")`

    
```Python    
def est_valide(i,j,graphe):
    """
    Renvoie True si le couple (i,j) correspond à des coordonnées valides
    param : i : int
    param : j : int
    param : graphe : list
    return : bool
    >>> est_valide(5,2,lab1)
    True
    >>> est_valide(-3,4,lab1)
    False
    """
    pass

```
    
```Python
def entree(graphe):
    """
    Renvoie les coordonnées du point de départ
    param : graphe : list
    return : tuple
    >>> entree(lab1)
    (1, 0)
    """
	pass
```

```Python            
def arrivee(graphe):
    """
    Renvoie les coordonnées du point de départ
    param : graphe : list
    return : tuple
    >>> arrivee(lab1)
    (6, 5)
    """
	pass
```

```Python            
def nombre_cases_vides(graphe):
    """
    Renvoie le nombre de cases vides(0) du graphe, l'entrée(2), la sortie(3), les cases visitées (4) comprises.
    param : graphe : list
    return : int
    >>> nombre_cases_vides(lab1)
    19
    """
	pass
```
    
```Python
def voisines_valides(x,y,graphe):
    """
    Renvoie la liste des cases valides voisines, non visités (!=4) et qui ne sont pas des murs autour de la case (x,y)
    param : i : int
    param : j : int
    param : graphe : list
    return : list
    >>> voisines_valides(1,5,lab1)
    [(1, 4), (2, 5)]
    """
	pass
```

```Python
def marquer_case(i,j,graphe):
    """
    Place 4 dans la case (i,j) pour indiquer que celle-ci est visitée
    param : i : int
    param : j : int
    param : graphe : list
    return : list
    >>> marquer_case(1,4,lab1)
    [[1, 1, 1, 1, 1, 1, 1], [2, 0, 0, 0, 4, 0, 1], [1, 1, 1, 1, 1, 0, 1], [1, 0, 1, 0, 0, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 3, 1]]
    """
	pass
```
Indication : on sera amené à faire une copie du labyrinthe pour ne pas le modifier.

```Python
import copy
copie=copy.deepcopy(graphe)
```

```Python
def solution(graphe):
    """
    Renvoie la solution du labyrinthe
    param : lab :list
    return : list
    >>> solution(lab1)
    [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5)]
    """
	pass
```

**Indication** : on crée une liste `chemin` et on suit l'algorithme suivant : aussi longtemps que l'on a pas atteint la sortie, on prend parmi les cases voisines valides une case qui n'a pas déjà été marquée, celle-ci est ajoutée à `chemin` et marquée en plaçant un `4` dans la case ; lorsqu'il n'y a pas de telle case, on rebrousse chemin, en supprimant la dernière case de la liste `chemin`, en écrivant `chemin.pop()`. Il faut penser à sortir de la boucle while dès que le voisin sélectionné est la sortie. Utiliser le débugger en cas de difficulté.

       
```Python
def representation_solution(graphe):
    """
    Affiche une représentation du graphe
    param : graphe : list
    return : None
    >>> representation_solution(lab1)
    ⬛⬛⬛⬛⬛⬛⬛
    🔴🔴🔴🔴🔴🔴⬛
    ⬛⬛⬛⬛⬛🔴⬛
    ⬛⬜⬛⬜⬜🔴⬛
    ⬛⬜⬛⬜⬛🔴⬛
    ⬛⬜⬜⬜⬛🔴⬛
    ⬛⬛⬛⬛⬛🔴⬛
    """
	pass
```

Obtenir la solution de labyrinthe.