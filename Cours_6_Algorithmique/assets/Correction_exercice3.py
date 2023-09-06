L=[0.5,1.0,2.0,3.7,5.0,6.0,7.0]
Classes=['T','C','C','T','T','C','C']

def distance(a,b):
    """
    renvoie la distance qui sépare deux points d'abscisse a et b
    param : a, b : float
    return : float
    >>> distance(2,5)
    3
    """
    return abs(a-b)

def critere(a):
    """
    renvoie la deuxième valeur du doublet
    >>> critere([3,8])
    8
    """
    return a[1]

def Kvoisins(liste,k,x):
    """
    renvoie la liste des indices des k objets les plus proches de l'élément d'abscisse x
    param : liste : list
    param : k : int
    param : x : float
    return : list
    >>> Kvoisins(L,3,3.0)
    [3, 2, 1]
    """
    ListeDistanceIndice=[[i,distance(L[i],x)] for i in range(len(L))]
    ListeDistanceIndice=sorted(ListeDistanceIndice,key=critere)
    result=[ListeDistanceIndice[i][0] for i in range(k)]
    return result
    
def predire_classe(liste_positions,liste_classes,k,x):
    """
    renvoie la classe correspondant à l'élement x
    param : liste_positions : list
    param : liste_classes : list
    param : k : int
    param : x : float
    return : string
    >>> predire_classe(L,Classes,3,3.0)
    'C'
    >>> predire_classe(L,Classes,5,3.0)
    'T'    
    """
    liste=Kvoisins(liste_positions,k,x)
    compte_C=len([liste[i] for i in range(len(liste)) if liste_classes[i]=='C'])
    compte_T=len([liste[i] for i in range(len(liste)) if liste_classes[i]=='T'])
    if compte_T>compte_C:
        return 'T'
    else:
        return 'C'
