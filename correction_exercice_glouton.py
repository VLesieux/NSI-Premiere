def rendu_monnaie_glouton(somme,pieces):
    """
    Renvoie les pièces à rendre selon un algorithme glouton
    param : somme : int
    param : pieces : list
    return : list
    >>> rendu_monnaie_glouton(177,[100,50,10,5,2])
    [100, 50, 10, 10, 5, 2]
    """
    rendu=[]
    while somme>0:
        difference=[(somme-pieces[i]) for i in range(len(pieces)) if (somme-pieces[i])>=0 ]
        choix=min(difference)
        prise=somme-choix
        rendu.append(prise)
        somme-=prise
    return rendu
    


lpoids=[1,2,5,6,7]
lvaleurs=[1,6,22,18,28]



def choix_glouton(lpoids,lvaleurs,P):
    """
    : return : renvoie l'indice de l'objet
    * de poids <= limite P
    * de plus grande valeur
    * qui n'est pas encore dans le sac
    s'il existe
    sinon renvoyez none
    :CU: 
    - len(lvaleurs) == len(lpoids) 
    - lpoids est triée par ordre croissant
    >>> choix_glouton(lpoids,lvaleurs,15)
    4
    >>> choix_glouton(lpoids,lvaleurs,6)
    2
    """ 
    possibles=[ i for i in range(len(lpoids)) if lpoids[i]<=P]
    valeurs_des_possibles=[lvaleurs[i] for i in range(len(possibles))]
    if len(valeurs_des_possibles)>0:
        choix=max(valeurs_des_possibles)
        return valeurs_des_possibles.index(choix)
    else:
        return None


from copy import deepcopy
import math 

def ks_glouton(lvaleurs, lpoids,P) :
    """
    renvoie un ensemble d'objet (indices dans lvaleurs et lpoids) pour lesquels
    un choix glouton a été effectué    
    :CU: 
    - len(lvaleurs) == len(lpoids) 
    - lpoids est triée par ordre croissant
    >>> ks_glouton(lvaleurs, lpoids,15)
    [4, 2, 1, 0]
    >>> ks_glouton(lvaleurs, lpoids,6)
    [2, 0]
    """
    copie=deepcopy(lpoids)
    liste=[]
    poids_disponible=P
    while poids_disponible>0:
        choix=choix_glouton(copie,lvaleurs,poids_disponible)
        if not choix==None:
            liste.append(choix)
            poids_disponible-=lpoids[choix]
            copie[choix]=math.inf                    
    return liste

def interet_glouton(lvaleurs, lpoids,P) :
    """
    renvoie l'interet obtenu par application de l'algorithme glouton
    >>> interet_glouton(lvaleurs, lpoids,15)
    57
    """
    compte=0
    for indice in ks_glouton(lvaleurs, lpoids,P):
        compte+=lvaleurs[indice]
    return compte












if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)