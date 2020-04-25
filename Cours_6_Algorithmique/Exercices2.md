## Exercices sur les algorithmes de tri
### Rappels

1. Rappeler le principe du tri par sélection et essayer de retrouver par vous-même l'algorithme de ce tri .
2. De même pour le tri par insertion.

### Application 1 : Ordre lexicographique

L'objectif est d'écrire un programme qui trie une liste de mots et les range suivant l'ordre lexicographique (ordre des dictionnaires).

alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]


1. Écrire une fonction `ordre_alphabet` qui prend en arguments deux caractères alphabétiques c1 et c2 et renvoie -1 si c1 est avant c2, 1 si c2 est avant c1 et 0 si c1 = c2. On pourra utiliser la méthode index qui renvoie l'indice d'un élément dans une chaîne de caractères.
2. Écrire une fonction `ordre_lexicographique` qui prend en arguments deux mots m1 et m2 et renvoie -1 si m1 est avant m2, 0 si m1 et m2 sont identiques et 1 si m1 est après m2.
3. Écrire une fonction `tri_lexicographique` qui prend en argument une liste de mots et trie cette liste, en adaptant le tri par sélection.

<u>Algorithme du tri par sélection à adapter</u>

```python
def echange(t,i,j):
    temp=t[i]
    t[i]=t[j]
    t[j]=temp

def tri_selection(t):
    for i in range(len(t)-1):
        m=i
        for j in range(i+1,len(t)):
            if t[j]<t[m]:
                m=j
        echange(t,i,m)
    return t
```
On écrira les docstrings suivantes des fonctions à compléter ; la fonction doctest est rappelée ensuite pour vous permettre de vous auto-contrôler.

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
    pass
```
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
    pass
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
    pass
```
```python
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)

```



### Application 2 : Trier des points

On dispose de points dans un plan muni d'un repère orthonormé d'origine O. Ces points possèdent un couple de coordonnées représenté par la liste [x,y].  
On se propose de trier ces points en fonction de leur distance à O, de la plus petite à la plus grande.

Indications: 

- écrire une fonction `distance` qui prend en paramètre une liste de deux nombres, nommée point, qui représente les coordonnées d'un point du plan
- écrire une fonction `compare` qui prend en paramètre deux listes p1 et p2 représentant deux points P1 et P2 et qui renvoie -1 si P1 est plus proche de O que P2, 1 si P2 est plus proche de O que P1, et 0 si les deux points sont équidistants
- écrire une fonction `tri_points` qui prend en paramètre une liste de points et qui trie cette liste suivant la distance à O, en utilisant le tri par insertion.

<u>Algorithme du tri par insertion à adapter</u>

```python
def insere(t,i,v):
    j=i
    while j>0 and t[j-1]>v:
        t[j]=t[j-1]
        j=j-1
    t[j]=v
    
def tri_insertion(t):
    for i in range(1,len(t)):
        insere(t,i,t[i])
    return t
```

On écrira les docstrings suivantes.

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
    pass
```
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
    pass
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
    pass
```

