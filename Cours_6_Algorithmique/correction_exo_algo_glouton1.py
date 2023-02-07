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
        difference=[(somme-pieces[i]) for i in range(len(pieces)) if (somme-pieces[i])>=0]
        piece_choisie=somme-min(difference)
        rendu.append(piece_choisie)
        somme-=piece_choisie
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
    - lpoids est triée par ordre croissant de poids
    >>> choix_glouton(lpoids,lvaleurs,15)
    4
    >>> choix_glouton(lpoids,lvaleurs,6)
    3
    """
    liste=[(lpoids[i]-P) for i in range(len(lpoids)) if (lpoids[i]-P)<=0]
    if len(liste)>0:
        return liste.index(max(liste))
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
    [4, 3, 1]
    >>> ks_glouton(lvaleurs, lpoids,6)
    [3]
    """
    copie=deepcopy(lpoids)
    poids_disponible=P
    resultat=[]
    while poids_disponible>0:
        choix=choix_glouton(copie,lvaleurs,poids_disponible)
        if choix !=None:
            resultat.append(choix)
            poids_disponible-=copie[choix]
            copie[choix]=math.inf
    return resultat
              
    
def interet_glouton(lvaleurs, lpoids,P) :
    """
    renvoie l'interet obtenu par application de l'algorithme glouton
    >>> interet_glouton(lvaleurs, lpoids,15)
    52
    """
    resultat=0
    for i in range(len(ks_glouton(lvaleurs, lpoids,P))):
        resultat+=lvaleurs[ks_glouton(lvaleurs, lpoids,P)[i]]
    return resultat











if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)