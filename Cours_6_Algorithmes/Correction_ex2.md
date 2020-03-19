
## Rappels

### 1. Tri par sélection

Soit une liste de longueur n.  
On considère que jusqu'à l'indice i-1 la liste est déjà triée et qu'il nous reste encore à trier de i à n.

L'algorithme consiste à sélectionner le minimum de la partie non triée situé admettons à l'indice m et de placer ce minimum à la suite de la partie triée en position i en faisant une permutation des éléments situés en positions i et m.

L'algorithme nécessite donc la recherche du minimum et l'écriture d'une permutation ou échange.

On rappelle l'algorithme du recherche de minimum qui est présent dans la fonction tri_selection

```python
def minimal(liste):
    minimum=liste[0]
    for i in range(len(liste)):
        if liste[i]<minimum:
            minimum=liste[i]
    return minimum
```
D'où l'algorithme complet :

```python
def echange(t,i,j):
    temp=t[i]
    t[i]=t[j]
    t[j]=temp

def tri_selection(t):
    for i in range(len(t)-1):
        m=i#on suppose que jusque i la liste est triée
        for j in range(i+1,len(t)):#recherche du minimum entre i+1 et n
            if t[j]<t[m]:#si on trouve en j un élément plus petit qu'en i
                m=j
        echange(t,i,m)
    return t
```
```python   
>>> tri_selection([3,12,9,1,7])
[1, 3, 7, 9, 12]
```

### 2. Tri par insertion

Soit une liste de longueur n. 
On considère que jusqu'à l'indice i-1 la liste est triée et qu'il nous reste encore à trier de i à n.

L'algorithme consiste à insérer correctement l'élément i dans la partie triée en décalant vers la droite tous les éléments qui le suivent.

L'algorithme nécessite l'écriture de l'insertion et du décalage vers la droite.

```python
def insere(t,i,v):
#insertion dans la liste t supposée triée de l'élément de valeur v en position i
    j=i
#on mémorise la variable i à travers la variable j pour ne pas modifier i
    while j>0 and t[j-1]>v:
        t[j]=t[j-1]
#on décale vers la droite tous les éléments de valeur supérieure à v en faisant décroître j
        j=j-1
#on parcourt pour cela de droite à gauche pour trouver le bon emplacement où insérer la valeur v
    t[j]=v
    
def tri_insertion(t):
    for i in range(1,len(t)):
        insere(t,i,t[i])
    return t
```
```   
>>> tri_insertion([3,12,9,1,7])
[1, 3, 7, 9, 12]
```

## Application 1 : Ordre lexicographique

```python
def echange(t,i,j):
    temp=t[i]
    t[i]=t[j]
    t[j]=temp
    
def insere(t,i,v):
    j=i
    while j>0 and compare(t[j-1],v)==1:
        t[j]=t[j-1]
        j=j-1
    t[j]=v
    
alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

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
    if alphabet.index(c1)<alphabet.index(c2):
        return -1
    elif alphabet.index(c1)>alphabet.index(c2):
        return 1
    else:
        return 0

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
    n=min(len(m1),len(m2))
    i=0
    while i<n:
        if ordre_alphabet(m1[i],m2[i])==1:
            return 1
        elif ordre_alphabet(m1[i],m2[i])==-1:
            return -1
        else:
            i=i+1
    return 0

def tri_lexicographique(liste):#adaptation de l'algorithme de tri par sélection
    """
    Renvoie une liste de mots triée dans l'ordre lexicographique
    :param : (list)
    :return: (list) 
    :Exemple:
    >>> tri_lexicographique(['chameau', 'ange', 'pipeau', 'pomme', 'enfer'])
    ['ange', 'chameau', 'enfer', 'pipeau', 'pomme']
    """
    for i in range(len(liste)-1):
        m=i#on suppose que jusque i la liste est triée
        for j in range(i+1,len(liste)):#recherche du minimum entre i+1 et n
            if ordre_lexicographique(liste[j],liste[m])==-1:#si on trouve en j un élément plus petit qu'en i
                m=j
        echange(liste,i,m)
    return liste 
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)

```

## Application 2 : Trier des points

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
    return (x**2+y**2)**0.5

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
    if distance(p1[0],p1[1])<distance(p2[0],p2[1]):
        return -1
    elif distance(p1[0],p1[1])>distance(p2[0],p2[1]):
        return 1
    else:
        return 0

def tri_points(liste):#adaptation de l'algorithme de tri par insertion
    """
    tri la liste des points par distance croissante à l'origine
    :param : (list)
    :return: (int)
    :Exemple:
    >>> tri_points([(2,0), (1,0), (0,3)])
    [(1, 0), (2, 0), (0, 3)]
    """
    for i in range(1,len(liste)):
        insere(liste,i,liste[i])
    return liste    
        
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)

```