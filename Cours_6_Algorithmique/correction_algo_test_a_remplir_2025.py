def recherche_maximum_liste_parcours_element(t):
    """
    Renvoie le maximum d'une liste de nombres
    param : t : list
    return : int
    >>> recherche_maximum_liste_parcours_element([3,18,5,21,6])
    21
    """
    maximum=t[0]
    for element in t:
…………………………………………(1)……………………………
…………………………………………(2)……………………………
    return maximum
#########################################################################################
def recherche_dichotomie(T,valeur):
    """
    Recherche valeur dans T par dichotomie
    Renvoie deux choses : l'indice de position de valeur dans T, et le nombre d'étapes nécessaires
    param : T : list
    param : valeur : int
    return : tuple
    >>> recherche_dichotomie([1,7,12,16,18,20,24,28,35,43,69],18)
    (4, 4)
    >>> recherche_dichotomie([1,7,12,16,18,20,24,28,35,43,69],40)
    'La valeur recherchée est absente de la liste'
    >>> recherche_dichotomie([1,7,12,16,18,20,24,28,35,43,69],90)
    "La valeur recherchée n'est pas dans les bornes de la liste"
    """
    g=0
    d=len(T)-1
    if T[g]>valeur or valeur > T[d]:
        return "La valeur recherchée n'est pas dans les bornes de la liste"
    compteur=0
…………………………………………(3)……………………………
        compteur+=1
        m=(g+d)//2
…………………………………………(4)……………………………
…………………………………………(5)……………………………
…………………………………………(6)……………………………
…………………………………………(7)……………………………
        else:
            return (m,compteur)
    return "La valeur recherchée est absente de la liste"
#########################################################################################
def recherche_mot_dans_un_texte_v2(mot,texte):
    """
    Renvoie, si elle existe, la première occurence du mot dans le texte
    param : mot : str
    param : texte : str
    return : int
    >>> recherche_mot_dans_un_texte_v2("oui","ce n'était pas si dur, oui, il fallait y croire")
    23
    >>> recherche_mot_dans_un_texte_v2("oui","ce n'était pas si dur, il fallait y croire")
    'Le mot est absent du texte'
    """
    for i in range(len(texte)-len(mot)):
…………………………………………(8)……………………………
            trouve=True
while..……………………………….(9)……………………………
…………………………………………(10)……………………………
…………………………………………(11)……………………………
…………………………………………(12)……………………………
    return "Le mot est absent du texte"
#########################################################################################
def tri_bulles(T):
    """
    Renvoie une liste triée par l'algorithme bulle
    param : T : list
    return : T : list
    >>> tri_bulles([4,7,2,9,1])
    [1, 2, 4, 7, 9]
    """
    n=len(T)
    for i in range(n-1):
…………………………………………(13)……………………………
…………………………………………(14)……………………………
…………………………………………(15)……………………………
    return T
#########################################################################################
def tri_selection_direct(liste):
    """
    param : liste : list
    return : list
    >>> tri_selection_direct([43,12,18,31,10])
    [10, 12, 18, 31, 43]
    """
    for i in range(len(liste)):
        minimum=liste[i]
        indice=i
        for j in range(i,len(liste)):
            if liste[j]<=minimum:
                minimum=liste[j]
…………………………………………(16)……………………………
…………………………………………(17)……………………………
    return liste
#########################################################################################
def tri_insertion(liste):
    """
    param : liste : list
    return : list
    >>> tri_insertion([43,12,18,31,10])
    [10, 12, 18, 31, 43]
    """
    for i in range(1,len(liste)):
…………………………………………(18)……………………………
       while key<liste[i-1] and i>0:
…………………………………………(19)……………………………
…………………………………………(20)……………………………
        liste[i]=key
    return liste

#########################################################################################


def f(x):
    """
    Renvoie l'image de x par la fonction
    param : x : float
    return : float
    >>> f(2)
    -1
    """
    pass

def recherche_solution_dichotomie(fonction,a,b,precision):
    """
    Renvoie la valeur approchée de l'équation f(x)=0 avec x entre a et b avec la precision
    demandée, et le nombre d'opérations effectuée
    param : f : function
    param : a : float
    param : b : float
    param : precision : float
    return : tuple
    >>> recherche_solution_dichotomie(f,1,3,0.001)
    (2.0947265625, 11)
    """
    pass

#########################################################################################


def tri_insertion(tab):
    """
    Renvoie une liste triée par insertion
    param : tab
    return : tab
    >>> tri_insertion([3, 5, 10, 11, 20, 7, 12])
    [3, 5, 7, 10, 11, 12, 20]
    """
    for i in range(1, len(tab)):
        key=tab[i]
..............................................
#décale vers la droite pour faire de la place à key aussi longtemps que...
..........................................
..............................................
#positionne la clé au bon endroit  
...............................      
    return tab

#########################################################################################

def recherche_indice_position_insertion_par_dichotomie(tab,x):
    """
    Renvoie  par dichotomie l'indice de position où insérer une valeur dans une liste supposée ordonnée
    param : tab : list
    param : x : int
    return : int
    >>> recherche_indice_position_insertion_par_dichotomie([3, 5, 10, 11, 20],7)
    2    
    """
    gauche=0
    droite=len(tab)-1
    while gauche<=droite:
        milieu=(gauche+droite)//2
        if tab[milieu]>x:
..........................................
        else:
..........................................
    return gauche

#########################################################################################

def tri_insertion_dicho(tab):
    """
    Renvoie une liste triée par insertion en utilisant la dichotomie
    param : tab : list
    return : list
    >>> tri_insertion_dicho([3, 5, 10, 11, 20, 7, 12])
    [3, 5, 7, 10, 11, 12, 20]
    """
    for i in range(1, len(tab)):
        key = tab[i]
        # Trouver par dichotomie l'indice d'insertion pour la clé dans la liste supposée ordonnée jusque i-1, c.a.d dans tab[:i]
        ..........................................
        # Décaler les éléments vers la droite pour faire de la place à key avec une boucle for (puisqu'on sait sa position finale)
        ..........................................
        ..........................................
        # Insérer key à la bonne position
        ..........
    return tab
    

if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)