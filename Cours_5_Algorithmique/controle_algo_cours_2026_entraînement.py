def recherche_indice_du_maximum(T):
    """
    Renvoie le maximum d'une liste de nombres
    param : T : list
    return : int
    >>> recherche_indice_du_maximum([3,18,5,21,6])
    3
    """

    

def recherche_dichotomie(T,valeur):
    """
    Recherche valeur dans T par dichotomie
    Renvoie deux choses : l'indice de position de valeur dans T, et le nombre d'étapes nécessaires
    param : T : list
    param : valeur : int
    return : tuple
    >>> recherche_dichotomie([1,7,12,16,18,20,24,28,35,43,69],18)
    (4, 4)
    >>> recherche_dichotomie([1,7,12,16,18,20,24,28,35,43,69],90)
    "La valeur recherchée n'est pas comprises dans les bornes de la liste"
    >>> recherche_dichotomie([1,7,12,16,18,20,24,28,35,43,69],40)
    'La valeur recherchée est absente de la liste'
    """


def tri_bulle(T):
    """
    renvoie une liste triée en faisant remonter les plus grandes valeurs par permutations successives
    param : T : list
    return : list
    >>> tri_bulle([2, 25, 10, 24, 5, 32, 3])
    [2, 3, 5, 10, 24, 25, 32]
    """
    

def tri_selection(T):
    """
    param : T : list
    return : list
    >>> tri_selection([43,12,18,31,10])
    [10, 12, 18, 31, 43]
    """
    

def tri_insertion(T):
    """
    param : T : list
    return : list
    >>> tri_insertion([43,12,18,31,10])
    [10, 12, 18, 31, 43]
    """
            
            
    

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)

    