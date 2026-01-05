def recherche(tab,n):
    """
    Renvoie l'indice de la dernière occurence de l'élément cherché
    Si absent, renvoie la longueur du tableau
    param : tab : list
    param : n : int
    >>> recherche([5,3],1)
    2
    >>> recherche([2,4],2)
    0
    >>> recherche([2,3,5,2,4],2)
    3
    """
    resultat=None
    for i in range(len(tab)):
        if tab[i]==n:
            resultat=i
    if resultat !=None:
        return resultat
    else:
        return len(tab)
    
from math import sqrt#import de la fonction racince carrée

def distance(point1,point2):
    """
    Calcule et renvoie la distance entre deux points
    param : point1 : tuple
    param : point2 : tuple
    >>> distance((0,0),(4,3))
    5.0
    """
    return sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)

def plus_courte_distance(tab,depart):
    """
    Renvoie la plus courte distance du point de départ aux points du tableau
    param : tab : list
    param : depart : tuple
    >>> plus_courte_distance([(7,9),(2,5),(5,2)],(0,0))
    (2, 5)
    """
    point=tab[0]
    min_dist=0
    for i in range(1,len(tab)):
        if distance(tab[i],depart)>min_dist:
            point=tab[i]
            min_dist=distance(point,depart)
    return point

            
def moyenne(tab):
    """
    Revoie la moyenne des éléments de tab si non vide sinon affiche 'erreur'
    param : tab : list
    >>> moyenne([5,3,8])
    5.333333333333333
    >>> moyenne([1,2,3,4,5,6,7,8,9,10])
    5.5
    >>> moyenne([])
    'erreur'
    """
    resultat=0
    if len(tab)>0:
        for element in tab:
            resultat+=element
        return resultat/len(tab)
    else:
        return 'erreur'


def dichotomie(tab,x):
    """
    Renvoie True si tab contient x et False sinon
    param : tab : list
    param : x : int
    >>> dichotomie([15,16,18,19,23,24,28,29,31,33],28)
    True
    >>> dichotomie([15,16,18,19,23,24,28,29,31,33],27)
    False
    """
    debut=0
    fin=len(tab)-1
    while debut<=fin:
        m=(debut+fin)//2
        if x==tab[m]:
            return True
        if x>tab[m]:
            debut=m+1
        else:
            fin=m-1
    return False
        










if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)