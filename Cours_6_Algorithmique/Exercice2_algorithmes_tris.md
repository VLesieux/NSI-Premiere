## Exercices sur les algorithmes de tri

Pour les doctests :

```python
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)

```
#### Exercice 1 : Un algorithme de tri

Traiter l'[exercice 2 du sujet n°2](https://github.com/VLesieux/NSI-Terminale/blob/master/Evaluation_pratique/21_NSI_02/21-NSI-02.pdf) de la banque des sujets de Terminale NSI.


```python
def tri(tab):
    """
    Renvoie une liste triée avec les 0 à gauche, les 1 à droite
    param : tab : list
    return : tab : list
    >>> tri([0,1,0,1,0,1,0,1,0])
     [0, 0, 0, 0, 0, 1, 1, 1, 1]
    """
	pass
```


#### Exercice 2 : tri bulles

Traiter l'[exercice 2 du sujet n°11](https://github.com/VLesieux/NSI-Terminale/blob/master/Evaluation_pratique/21_NSI_11/21_NSI_11.pdf) de la banque des sujets de Terminale NSI.


```python
def tri_bulles_v1(T):
    """
    Renvoie une liste triée par l'algorithme bulle
    param : T : list
    return : T : list
    >>> tri_bulles_v1([4,7,2,9,1])
    [1, 2, 4, 7, 9]
    """
	pass
```

```python
def tri_bulles_v2(T):
    """
    Renvoie une liste triée par l'algorithme bulle
    param : T : list
    return : T : list
    >>> tri_bulles_v2([4,7,2,9,1])
    [1, 2, 4, 7, 9]
    """
	pass
```

#### Exercice 3: tri par insertion

Traiter l'[exercice2 du sujet n°5](https://github.com/VLesieux/NSI-Terminale/blob/master/Evaluation_pratique/21_NSI_05/21_NSI_05.pdf) de la banque des sujets de Terminale NSI.

```python
def tri_insertion(L):
    """
    Renvoie la liste triée par l'algorithme d'insertion
    param : T : list
    return : T : list
    >>> tri_bulles_v2([4,7,2,9,1])
    [1, 2, 4, 7, 9]
    """
	pass
```

#### Exercice 4 : tri par sélection

```python
def tri_selection(L):
    """
    Renvoie la liste triée par l'algorithme de sélection
    param : T : list
    return : T : list
    >>> tri_bulles_v2([4,7,2,9,1])
    [1, 2, 4, 7, 9]
    """
	pass
```

Traiter l'[exercice1 du sujet n°13](https://github.com/VLesieux/NSI-Terminale/blob/master/Evaluation_pratique/21_NSI_13/21_NSI_13.pdf) de la banque des sujets de Terminale NSI.


#### Exercice 5 : Application pratique du tri par sélection : l'ordre lexicographique.

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


```python
def tri_lexicographique(tab):
    """
    Renvoie une liste de mots triée dans l'ordre lexicographique
    :param : tab : list
    :return: list
    :Exemple:
    >>> tri_lexicographique(['chameau', 'ange', 'pipeau', 'pomme', 'enfer'])
    ['ange', 'chameau', 'enfer', 'pipeau', 'pomme']
    """
```

#### Exercice 6 : Application pratique du tri par insertion : trier des points.

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

```python
def tri_points(tab):
    """
    tri la liste des points par distance croissante à l'origine
    :param : tab : list
    :return: list
    :Exemple:
    >>> tri_points([(2,0), (1,0), (0,3)])
    [(1, 0), (2, 0), (0, 3)]
    """
```