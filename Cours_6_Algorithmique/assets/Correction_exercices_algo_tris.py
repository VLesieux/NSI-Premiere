def tri(tab):
    """
    Tri la liste tab formée de 0 et de 1 en mettant les 0 en premier, les 1 à la fin
    param : tab : list
    return : list
    >>> tri([0,1,0,1,0,1,0,1,0])
    [0, 0, 0, 0, 0, 1, 1, 1, 1]
    """
    # i est le premier indice de la zone non triée, j le dernier indice
    # au début, la zone non triée est le tableau entier
    i=0
    j=len(tab)-1
    while i!=j:
        if tab[i]==0:
            i=i+1
        else:
            valeur=tab[j]
            tab[j]=1
            tab[i]=valeur
            j=j-1
    return tab

def tri_bulles(T):
    """
    Renvoie une liste triée par ordre croissant
    param : T : list
    return : list
    >>> tri_bulles([4,8,2,13,5])
    [2, 4, 5, 8, 13]
    """
    n=len(T)
    for i in range(n-1,0,-1):
        for j in range(i):
            if T[j]>T[j+1]:
                temp=T[j]
                T[j]=T[j+1]
                T[j+1]=temp
    return T

def tri_insertion(L):
    """
    Renvoie la liste triée grâce au tri par insertion
    param : L : list
    return : list
    >>> tri_insertion([2,5,-1,7,0,28])
    [-1, 0, 2, 5, 7, 28]
    >>> tri_insertion([10,9,8,7,6,5,4,3,2,1,0])
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    n=len(L)
    if n==0:
        return L
    for j in range(1,n):
        e=L[j]
        i=j
        while i>0 and L[i-1]>e:
            i=i-1
        if i!=j:
            for k in range(j,i,-1):
                L[k]=L[k-1]
            L[i]=e
    return L


def tri_selection(tab):
    """
    Renvoie un tableau trié
    param : tab : list
    return : list
    >>> tri_selection([1,52,6,-9,12])
    [-9, 1, 6, 12, 52]
    """
    for i in range(len(tab)):
        minimum=i
        for j in range(i,len(tab)):            
            if tab[j]<tab[minimum]:
                minimum=j
        tab[i],tab[minimum]=tab[minimum],tab[i]
    return tab



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
    if alphabet.index(c1)>alphabet.index(c2):
        return 1
    elif alphabet.index(c1)<alphabet.index(c2):
        return -1
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
    for i in range(len(m1)):
        if ordre_alphabet(m1[i],m2[i])==1:
            return 1
        elif ordre_alphabet(m1[i],m2[i])==-1:
            return -1
    return 0

def tri_lexicographique(t):
    """
    Renvoie une liste de mots triée dans l'ordre lexicographique
    :param : t : list
    :return: list
    :Exemple:
    >>> tri_lexicographique(['chameau', 'ange', 'pipeau', 'pomme', 'enfer'])
    ['ange', 'chameau', 'enfer', 'pipeau', 'pomme']
    """
    for i in range(len(t)):
        minimum=i
        for j in range(i,len(t)):            
            if ordre_lexicographique(t[j],t[minimum])==-1:
                minimum=j
        t[i],t[minimum]=t[minimum],t[i]
    return t    

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
    if  distance(p1[0],p1[1])>distance(p2[0],p2[1]):
        return 1
    elif distance(p1[0],p1[1])<distance(p2[0],p2[1]):
        return -1
    else:
        return 0


def tri_points(t):
    """
    tri la liste des points par distance croissante à l'origine
    :param : t : list
    :return: list
    :Exemple:
    >>> tri_points([(2,0), (1,0), (0,3)])
    [(1, 0), (2, 0), (0, 3)]
    """
    n=len(t)
    for j in range(1,n):
        e=t[j]
        i=j
        while i>0 and compare(t[i-1],e)==1:
            i=i-1
        if i!=j:
            for k in range(j,i,-1):
                t[k]=t[k-1]
            t[i]=e
    return t

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
