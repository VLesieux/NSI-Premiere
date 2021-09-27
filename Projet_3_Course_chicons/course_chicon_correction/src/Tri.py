def compare_entier_croissant(a, b):
    """
    :param a: (int) un entier
    :param b: (int) un entier
    :return: (int)  
             * >0  si a est supérieur à b
             * 0 si a est égal à b
             * <0 si a est inférieur à b
    :CU: aucune
    :Exemples:

    >>> compare_entier_croissant(1, 3) < 0
    True
    """
    return a-b


def compare_chaine_lexicographique(a, b):
    return (a>b)-(a<b)

    
def compare_entier_décroissant(a, b):
    """
    :param a: (int) un entier
    :param b: (int) un entier
    :return: (int) 
             * >0 si a est inférieur à b
             * 0 si a est égal à b
             * <0 si a est supérieur à b
    :CU: aucune
    :Exemples:

    >>> compare_entier_décroissant(1, 3) > 0
    True
    """
    return b-a

def tri_selection(l,comp):
    """
        paramètre l : liste
        paramètre comp : mode de comparaison
        valeur renvoyée : liste triée

    CU : liste non vide

    Exemples :

    >>> tri_selection([1,8,3,10,5],compare_entier_croissant)
    [1, 3, 5, 8, 10]
    
    """
    for i in range(len(l)):
        j=selection_min(l,i,comp)
        l[i],l[j]=l[j],l[i]
    return l
        
def selection_min(l,i,comp):
    """
        paramètre l : liste
        paramètre i : int
        comp : mode de comparaison
        valeur renvoyée : l'indice du minimum à partir de l'indice i

    CU : liste non vide

    Exemples :

    >>> selection_min([1,8,3,10,5,2,6],2,compare_entier_croissant)
    5
    
    """
    i_min=i
    for j in range(i+1,len(l)):
        if comp(l[j],l[i_min])<0:
            i_min=j
    return i_min


def selection_min_longueur(l,i,comp):
    """
        paramètre l : liste
        paramètre i : int
        comp : mode de comparaison
        valeur renvoyée : l'indice du minimum à partir de l'indice i

    CU : liste non vide

    Exemples :

    >>> selection_min([1,8,3,10,5,2,6],2,compare_entier_croissant)
    5
    
    """
    i_min=i
    for j in range(i+1,len(l)):
        if comp(len(l[j]),len(l[i_min]))<0:
            i_min=j
    return i_min


def compare_chaine_longueur(l,comp):
    for i in range(len(l)):
        j=selection_min_longueur(l,i,comp)
        l[i],l[j]=l[j],l[i]
    return l

alphabet=["a","b","c","d","e"]

def selection_min_chaine(l,i,comp):
    """
        paramètre l : liste
        paramètre i : int
        comp : mode de comparaison
        valeur renvoyée : l'indice du minimum à partir de l'indice i

    CU : liste non vide

    Exemples :

    >>> selection_min([1,8,3,10,5,2,6],2,compare_entier_croissant)
    5
    
    """
    i_min=i
    for j in range(i+1,len(l)):
        if comp(alphabet.index(l[i][0]),alphabet.index(l[i_min][0]))<0:
            i_min=j
    return i_min


def compare_chaine_lexico(l,comp):
    for i in range(len(l)):
        j=selection_min_chaine(l,i,comp)
        l[i],l[j]=l[j],l[i]
    return l

    

    
    





if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)