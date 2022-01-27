## Exercices sur les algorithmes de tri

Pour les doctests :

```python
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)

```
#### Exercice 1 : Un algorithme de tri

Traiter l'[exercice 2 du sujet n°2](https://github.com/VLesieux/NSI-Terminale/blob/master/Evaluation_pratique/21_NSI_02/21-NSI-02.pdf) de la banque des sujets de Terminale NSI.


#### Exercice 2 : tri bulles

Traiter l'[exercice 2 du sujet n°11](https://github.com/VLesieux/NSI-Terminale/blob/master/Evaluation_pratique/21_NSI_11/21_NSI_11.pdf) de la banque des sujets de Terminale NSI.


#### Exercice 3: tri par insertion

Traiter l'[exercice2 du sujet n°5](https://github.com/VLesieux/NSI-Terminale/blob/master/Evaluation_pratique/21_NSI_05/21_NSI_05.pdf) de la banque des sujets de Terminale NSI.


#### Exercice 4 : tri par sélection

Traiter l'[exercice1 du sujet n°13](https://github.com/VLesieux/NSI-Terminale/blob/master/Evaluation_pratique/21_NSI_13/21_NSI_13.pdf) de la banque des sujets de Terminale NSI.


#### Exercice 5 : Application du tri par sélection : ordre lexicographique

L'objectif est d'écrire un programme qui trie une liste de mots et les range suivant l'ordre lexicographique (ordre des dictionnaires).

alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


1. Écrire une fonction `ordre_alphabet` qui prend en arguments deux caractères alphabétiques c1 et c2 et renvoie -1 si c1 est avant c2, 1 si c2 est avant c1 et 0 si c1 = c2.
On pourra utiliser la méthode index qui renvoie l'indice d'un élément dans une chaîne de caractères. 

Exemple :

```python
>>> liste=[3,5,7]
>>> liste.index(5)
1
```

```python
def ordre_alphabet(c1,c2):
    """
    Renvoie -1 si c1 est avant c2
    Renvoie 1 si c1 est après c2
    Renvoie 0 si c1 est égal à c2
    :param : (str)
    :return: (int) 
    :Exemple:
    >>> ordre_alphabet('a','m')
    -1
    >>> ordre_alphabet('p','m')
    1
    >>> ordre_alphabet('m','m')
    0
    """
 ```   
 
    
2. Écrire une fonction `ordre_lexicographique` qui prend en arguments deux mots m1 et m2 et renvoie -1 si m1 est avant m2, 0 si m1 et m2 sont identiques et 1 si m1 est après m2.

```python
def ordre_lexicographique(m1,m2):
    """
    Renvoie -1 si m1 est avant m2
    Renvoie 1 si m1 est après m2
    Renvoie 0 si m1 est égal à m2
    :param : (str)
    :return: (int) 
    :Exemple:
    >>> ordre_lexicographique('mari','matin')
    -1
    >>> ordre_lexicographique('mari','malin')
    1
    >>> ordre_lexicographique('mari','mari')
    0
    """
```

3. Écrire une fonction `tri_lexicographique` qui prend en argument une liste de mots et trie cette liste, en adaptant la fonction `tri_selection` ; ce sera l'occasion de retrouver son écriture par soi-même.

Rappel : on peut passer par l'écriture d'une fonction intermédiare

```python
def indice_minimum_a_partir_de_indice(t,i):
    """
    Renvoie l'indice de (minimum de la liste à partir de l'indice i)
    param : t : liste
    param : i : int
    >>> indice_minimum_a_partir_de_indice([3,6,2,9,1,12],2)
    4
    """
``` 

Puis réaliser une suite d'interversions pour obtenir la fonction `tri_selection` 

```python
def tri_selection(t):
    """
    param : t : list
    return : list
    >>> tri_selection([43,12,18,31,10])
    [10, 12, 18, 31, 43]
    """
```    

Adaptons ces fonctions à nos besoins :

```python
def indice_minimum_mot_a_partir_de_indice(t,i):
    """
    Renvoie l'indice de (minimum de la liste à partir de l'indice i)
    param : t : liste
    param : i : int
    >>> indice_minimum_mot_a_partir_de_indice(['chameau', 'ange', 'pipeau', 'pomme', 'enfer'],2)
    4
    """
``` 

```python
def tri_lexicographique(liste):
    """
    Renvoie une liste de mots triée dans l'ordre lexicographique
    :param : (list)
    :return: (list) 
    :Exemple:
    >>> tri_lexicographique(['chameau', 'ange', 'pipeau', 'pomme', 'enfer'])
    ['ange', 'chameau', 'enfer', 'pipeau', 'pomme']
    """
```

#### Exercice 6 : Application du tri par insertion : trier des points

On dispose de points dans un plan muni d'un repère orthonormé d'origine O. Ces points possèdent un couple de coordonnées représenté par la liste [x,y].  
On se propose de trier ces points en fonction de leur distance à O, de la plus petite à la plus grande.

Indications: 

- écrire une fonction `distance` qui prend en paramètre deux nombres `x` et `y` qui représentent les coordonnées abscisse et ordonnée d'un point du plan pour renvoyer la distance de ce point à l'origine O du repère

```python
def distance(x,y):
    """
    Renvoie la distance OM où M est le point de coordonnées [x,y]
    :param : (list)
    :return: (int)
    :Exemple:
    >>> distance(0,2)
    2.0
    >>> distance(4,3)
    5.0
    """
```

- écrire une fonction `compare` qui prend en paramètre deux tuples p1 et p2 représentant deux points P1 et P2 et qui renvoie -1 si P1 est plus proche de O que P2, 1 si P2 est plus proche de O que P1, et 0 si les deux points sont équidistants

```python
def compare(p1,p2):
    """
    Renvoie -1 si p1 est plus proche de O que p2
    Renvoie 1 si p1 est plus loin de O que p2
    Renvoie 0 si p1 et p2 sont à la même distance de O
    :param : (list)
    :return: (int)
    :Exemple:
    >>> compare((0,2),(1,0))
    1
    >>> compare((1,0),(0,2))
    -1
    >>> compare((1,0),(1,0))
    0
    """
```

- écrire une fonction `tri_points` qui prend en paramètre une liste de points et qui trie cette liste suivant la distance à O, en utilisant la fonction `tri_insertion`; ce sera l'occasion de la retrouver par soi-même.

Rappel : on peut passer par l'écriture d'une fonction intermédiare

```python
def emplacement(t,indice):
    """
    param : t : list
    return : list
    >>> emplacement([1, 4, 5, 6, 8],4)
    [1, 4, 5, 6, 8]
    """
```

```python
def tri_insertion(t):
    """
    param : t : list
    return : list
    >>> tri_insertion([43, 12, 18, 31, 10])
    [10, 12, 18, 31, 43]
    """
```

Adaptons ces fonctions à nos besoins :

```python
def emplacement_point(t,indice):
    """
    param : t : list
    return : list
    >>> emplacement([(1,0),(4,0),(6,0),(8,0),(5,0)],4)
    [(1, 0), (4, 0), (5, 0), (6, 0), (8, 0)]
    """
```

```python
def tri_points(liste):
    """
    tri la liste des points par distance croissante à l'origine
    :param : (list)
    :return: (int)
    :Exemple:
    >>> tri_points([(2,0), (1,0), (0,3)])
    [(1, 0), (2, 0), (0, 3)]
    """
```