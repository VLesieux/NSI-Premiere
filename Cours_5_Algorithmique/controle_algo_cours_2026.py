def recherche_indice_du_maximum(T):
    """
    Renvoie le maximum d'une liste de nombres
    param : T : list
    return : int
    >>> recherche_indice_du_maximum([3,18,5,21,6])
    3
    """
    maximum = T[0]
    j=0
    for i in range(len(T)):
        if T[i]>maximum:
            j=i#on retient l'indice du nouveau maximum
            maximum=T[i]#un nouveau maximum
    return j
    

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
    g=0
    d=len(T)-1
    if valeur<T[0] or valeur>T[-1]:
        return "La valeur recherchée n'est pas comprises dans les bornes de la liste"
    operations=0
    while g<=d:
        m=(g+d)//2
        operations +=1
        if T[m]>valeur:
            d=m-1
        elif T[m]<valeur:
            g=m+1
        else:
            return m,operations
    return 'La valeur recherchée est absente de la liste'

def tri_bulle(T):
    """
    renvoie une liste triée en faisant remonter les plus grandes valeurs par permutations successives
    param : T : list
    return : list
    >>> tri_bulle([2, 25, 10, 24, 5, 32, 3])
    [2, 3, 5, 10, 24, 25, 32]
    """
    for i in range(len(T)):
        for j in range(len(T)-i-1):#on restreint au fur et à mesure car la fin est triée
            if T[j]>T[j+1]:
                T[j],T[j+1]=T[j+1],T[j]#permutation des valeurs qui se suivent
    return T
    

def tri_selection(T):
    """
    param : T : list
    return : list
    >>> tri_selection([43,12,18,31,10])
    [10, 12, 18, 31, 43]
    """
    for i in range(len(T)):
        minimum=T[i]
        indice_minimum=i
        for j in range(i+1,len(T)):#recherche de l'indice du minimum
            if T[j]<minimum:
                 minimum=T[j]
                 indice_minimum=j
        T[i],T[indice_minimum]=T[indice_minimum],T[i]
    return T
    

def tri_insertion(T):
    """
    param : T : list
    return : list
    >>> tri_insertion([43,12,18,31,10])
    [10, 12, 18, 31, 43]
    """
    for i in range(1,len(T)):
        j=i
        cle=T[i]
        while j>0 and cle<T[j-1]:#l'odre est important car la première condition doit être vérifiée en premier
            T[j]=T[j-1]#on décale vers la droite
            j=j-1
        T[j]=cle#on insère la clé au bon endroit
    return T
            
            
    

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)

    