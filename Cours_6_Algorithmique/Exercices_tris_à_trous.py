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
....................(1).............................
    elif alphabet.index(c1)>alphabet.index(c2):
....................(2).............................
    else:
....................(3).............................
        
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
....................(4).............................
        if ordre_alphabet(m1[i],m2[i])==-1:
            return -1
        elif ordre_alphabet(m1[i],m2[i])==1:
            return 1
....................(5).............................


def indice_minimum_a_partir_de_indice(t,i):
    """
    Renvoie l'indice de (minimum de la liste à partir de l'indice i)
    param : t : liste
    param : i : int
    >>> indice_minimum_a_partir_de_indice([3,6,2,9,1,12],2)
    4
    """
    indice=i
    minimum=t[i]
    for j in range(i, len(t)):
....................(6).............................
            minimum=t[j]
            indice=j
....................(7).............................
      
def tri_selection(t):
    """
    param : t : list
    return : list
    >>> tri_selection([43,12,18,31,10])
    [10, 12, 18, 31, 43]
    """
    for i in range(len(t)):
....................(8).............................
    return t


def indice_minimum_mot_a_partir_de_indice(t,i):
    """
    Renvoie l'indice de (minimum de la liste à partir de l'indice i)
    param : t : liste
    param : i : int
    >>> indice_minimum_mot_a_partir_de_indice(['chameau', 'ange', 'pipeau', 'pomme', 'enfer'],2)
    4
    """
    indice=i
    minimum=t[i]
    for j in range(i, len(t)):
....................(9).............................
            minimum=t[j]
            indice=j
....................(10).............................

    
def tri_lexicographique(liste):
    """
    Renvoie une liste de mots triée dans l'ordre lexicographique
    :param : (list)
    :return: (list) 
    :Exemple:
    >>> tri_lexicographique(['chameau', 'ange', 'pipeau', 'pomme', 'enfer'])
    ['ange', 'chameau', 'enfer', 'pipeau', 'pomme']
    """
    for i in range(len(liste)):
....................(11).............................
    return liste


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
....................(12).............................


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
....................(13).............................
        return -1
....................(14).............................
        return 1
    else:
        return 0


def emplacement(t,indice):
    """
    place correctement la valeur à l'indice i dans la liste en décalant les autres vers la droite
    param : t : list
    return : list
    >>> emplacement([1, 4, 8, 6, 5, 9],4)
    [1, 4, 5, 8, 6, 9]
    """
    cle=t[indice]
    j=indice-1
....................(15).............................
        t[j+1]=t[j]
        j-=1
....................(16).............................
    return t
        

def tri_insertion(t):
    """
    param : t : list
    return : list
    >>> tri_insertion([43, 12, 18, 31, 10])
    [10, 12, 18, 31, 43]
    """
    for i in range(len(t)):
....................(17).............................
    return t


def emplacement_point(t,indice):
    """
    param : t : list
    return : list
    >>> emplacement([(1,0),(4,0),(8,0),(6,0),(5,0),(0,9)],4)
    [(1, 0), (4, 0), (5, 0), (8, 0), (6, 0), (0, 9)]
    """
    cle=t[indice]
    j=indice-1
....................(18).............................
        t[j+1]=t[j]
        j-=1
....................(19).............................
    return t

def tri_points(liste):
    """
    tri la liste des points par distance croissante à l'origine
    :param : (list)
    :return: (int)
    :Exemple:
    >>> tri_points([(2,0), (1,0), (0,3)])
    [(1, 0), (2, 0), (0, 3)]
    """
    for i in range(len(liste)):
....................(20).............................
    return t    













if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)

