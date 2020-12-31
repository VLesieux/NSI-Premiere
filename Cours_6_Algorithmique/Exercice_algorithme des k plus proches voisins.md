## Exercice sur l'algorithme des k plus proches voisins

Pour les doctests :

```python
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
```

On se propose d'écrire un algorithme pour un espace à une seule dimension.

<img src="Assets/plus_proche_voisins.png">

On dispose d'une liste des positions des éléments ainsi qu'une liste des classes des éléments ('T' pour triangle, 'C' pour carré), le rond vert étant exclus des listes.

```python
L=[0.5,1.0,2.0,3.7,5.0,6.0,7.0]
Classes=['T','C','C','T','T','C','C']
```

1. Recherche des k plus proches voisins

On cherche les k plus proches voisins de l'élément rond vert de coordonnée x=3.
Écrire une fonction `Kvoisins` qui prend en arguments une liste L de coordonnées, un entier k, et x la position d'un nouvel élément tel que le rond vert et qui renvoie la liste des indices dans L des k plus proches voisins de x.

Algorithme : créer une liste `ListeDistanceIndice` qui contient les couples [di,i] des distances di de tous les éléments par rapport à x et leur indice i dans la liste L. Puis ordonnez cette liste selon le critère de distance (en utilisant `sorted`, `key`, et une fonction `critere` qui renvoie la deuxième valeur d'un doublet) et ne garder que les k premiers éléments. On sera amené à créer une fonction intermédaire `distance` pour le calcul des distances en utilisant la fonction `abs` qui renvoie la valeur absolue d'un nombre.

```python
def distance(a,b):
    """
    renvoie la distance qui sépare deux points d'abscisse a et b
    param : a, b : float
    return : float
    >>> distance(2,5)
    3
    """
```

```python
def critere(a):
    """
    renvoie la deuxième valeur du doublet
    >>> critere([3,8])
    8
    """
```
```python 
>>> liste=[[3,5],[1,2],[7,9]]
>>> liste=sorted(liste,key=critere)
>>> liste
[[1, 2], [3, 5], [7, 9]]
```
```python
def Kvoisins(liste,k,x):
    """
    renvoie la liste des indices des k objets les plus proches de l'élément d'abscisse x
    param : liste : list
    param : k : int
    param : x : float
    return : list
    >>> Kvoisins(L,3,3.0)
    [3, 2, 1]
    """
```


2. Attribution de la classe

On attribue à l'élément la classe qui est la plus rencontrée parmi les k plus proches voisins.
<img src="Assets/plus_proche_voisins_classe.png">

Dans le cas où k=3, la classe attribuée est le carré car les plus proches voisins sont deux carrés et un triangle,  tandis que dans le cas où k=5, la classe attribuée est le triangle car les plus proches voisins sont deux carrés et trois triangles.


On réalise pour cela une fonction `predire_classe` qui admet comme paramètres la liste des positions, la liste des classes, la valeur de k et la valeur de x.

```python
def predire_classe(liste_positions,liste_classes,k,x):
    """
    renvoie la classe correspondant à l'élement x
    param : liste_positions : list
    param : liste_classes : list
    param : k : int
    param : x : float
    return : string
    >>> predire_classe(L,Classes,3,3.0)
    'C'
    >>> predire_classe(L,Classes,5,3.0)
    'T'    
    """
```




