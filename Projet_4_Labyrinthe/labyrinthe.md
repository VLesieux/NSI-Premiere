

<img src="Assets/lab1.png">


 <img src="Assets/lab2.png">







```Python
labyrinthe=[
[1,1,1,1,1,0,0,0,0,0,1],
[1,0,0,0,1,0,1,0,1,0,1],
[1,0,1,0,1,0,1,0,1,0,1],
[1,0,1,0,1,0,1,0,1,0,1],
[1,0,1,0,1,0,1,0,1,0,1],
[2,0,1,0,0,0,1,0,1,0,3],
[1,1,1,1,1,1,1,0,1,0,1],
[1,0,0,0,1,0,0,0,1,0,1],
[1,0,1,0,1,0,1,1,1,0,1],
[1,0,1,1,1,0,1,0,0,0,1],
[1,0,0,0,0,0,1,1,0,1,1]
      ]

lab1=[
[1,1,1,1,1,1,1],
[2,0,0,0,0,0,1],
[1,1,1,1,1,0,1],
[1,0,1,0,0,0,1],
[1,0,1,0,1,0,1],
[1,0,0,0,1,0,1],
[1,1,1,1,1,3,1]
    ]




def nombre_colonnes(graphe):
    """
    Renvoie le nombre de colonnes du graphe
    param : graphe : list
    return : int
    >>> nombre_colonnes(lab1)
    7
    """
    return len(graphe[0])

def nombre_lignes(graphe):
    """
    Renvoie le nombre de lignes du graphe
    param : graphe : list
    return : int
    >>> nombre_lignes(lab1)
    7
    """
    return len(graphe)

def representation(graphe):
    """
    Affiche une représentation du graphe
    param : graphe : list
    return : None
    >>> representation(lab1)
    ⬛⬛⬛⬛⬛⬛⬛
    ⬜⬜⬜⬜⬜⬜⬛
    ⬛⬛⬛⬛⬛⬜⬛
    ⬛⬜⬛⬜⬜⬜⬛
    ⬛⬜⬛⬜⬛⬜⬛
    ⬛⬜⬜⬜⬛⬜⬛
    ⬛⬛⬛⬛⬛⬜⬛
    <BLANKLINE>
    """
    texte=""
    for i in range(len(graphe)):
        for j in range(len(graphe[0])):
            if graphe[i][j]==1:
                texte+="⬛"
            else:
                texte+="⬜"           
        texte+="\n"
    print(texte)
    
    
def est_valide(i,j,graphe):
    """
    Renvoie True si le couple (i,j) correspond à des coordonnées valides
    param : i : int
    param : j : int
    param : graphe : list
    return : bool
    >>> est_valide(5,2,lab1)
    True
    >>> est_valide(-3,4,lab1)
    False
    """
    return i>=0 and i<=nombre_lignes(graphe) and j>=0 and j<=nombre_colonnes(graphe)
    

def entree(graphe):
    """
    Renvoie les coordonnées du point de départ
    param : graphe : list
    return : tuple
    >>> entree(lab1)
    (1, 0)
    """
    for i in range(len(graphe)):
        for j in range(len(graphe[0])):
            if graphe[i][j]==2:
                return (i, j)
            
def arrivee(graphe):
    """
    Renvoie les coordonnées du point de départ
    param : graphe : list
    return : tuple
    >>> arrivee(lab1)
    (6, 5)
    """
    for i in range(len(graphe)):
        for j in range(len(graphe[0])):
            if graphe[i][j]==3:
                return (i, j)
            
def nombre_cases_vides(graphe):
    """
    Renvoie le nombre de cases vides(0) du graphe, entrée(2), sortie(3), visités (4) comprises.
    param : graphe : list
    return : int
    >>> nombre_cases_vides(lab1)
    19
    """
    compteur=0
    for i in range(len(graphe)):
        for j in range(len(graphe[0])):
            if graphe[i][j]==0 or graphe[i][j]==2 or graphe[i][j]==3 or graphe[i][j]==4:
                compteur+=1
    return compteur
    

def voisines_valides(x,y,graphe):
    """
    Renvoie la liste des cases valides qui ne sont pas des murs autour de la case (x,y)
    On tourne dans le sens des aiguilles d'une montre à partir du haut à gauche
    param : i : int
    param : j : int
    param : graphe : list
    return : list
    >>> voisines_valides(1,5,lab1)
    [(1, 4), (2, 5)]
    """
    liste=[(x-1,y),(x,y-1),(x,y+1),(x+1,y)]
    resultat=[]
    for element in liste:
        if est_valide(element[0],element[1],graphe) and graphe[element[0]][element[1]] !=1:
            resultat.append(element)
    return resultat


def marquer_case(i,j,graphe):
    """
    Place 4 dans la case (i,j) pour indiquer que celle-ci est visitée
    param : i : int
    param : j : int
    param : graphe : list
    return : list
    >>> marquer_case(1,4,lab1)
    [[1, 1, 1, 1, 1, 1, 1], [2, 0, 0, 0, 4, 0, 1], [1, 1, 1, 1, 1, 0, 1], [1, 0, 1, 0, 0, 0, 1], [1, 0, 1, 0, 1, 0, 1], [1, 0, 0, 0, 1, 0, 1], [1, 1, 1, 1, 1, 3, 1]]
    """
    graphe[i][j]=4
    return graphe

import copy
    
# def solution(graphe):
#     """
#     Renvoie le chemin correspondant à la solution du labyrinthe
#     param : entree : tuple
#     param : graphe : list
#     return : list
#     >>> solution(lab1)
#     [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5)]
#     """
#     copie=copy.deepcopy(graphe)
#     chemin=[entree(graphe)]
#     fin=arrivee(graphe)
#     while chemin[-1] != fin :
#         marquer_case(chemin[-1][0],chemin[-1][1],copie)
#         possibles=[element for element in voisines_valides(chemin[-1][0],chemin[-1][1],copie) if copie[element[0]][element[1]] !=4]
#         if len(possibles) > 0:
#             chemin.append(possibles[0])           
#         else:
#             chemin.pop()
#     return(chemin)
# 
# solution(lab1)


def solution(graphe):
    """
    Renvoie la solution du labyrinthe
    param : lab :list
    return : list
    >>> solution(lab1)
    [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5)]
    """
    chemin=[entree(graphe)]
    case=chemin[0]
    i=case[0]
    j=case[1]
    while graphe[i][j]!=3:
        graphe[i][j]=4
        voisins=voisines_valides(i,j,graphe)
        if len(voisins)>0:
            case=voisins.pop()
            i=case[0]
            j=case[1]
            chemin.append(case)
        else:
            chemin.pop()
            i=chemin[-1][0]
            j=chemin[-1][1]

    return chemin
       

def representation_solution(graphe):
    """
    Affiche une représentation du graphe
    param : graphe : list
    return : None
    >>> representation_solution(lab1)
    ⬛⬛⬛⬛⬛⬛⬛
    🔴🔴🔴🔴🔴🔴⬛
    ⬛⬛⬛⬛⬛🔴⬛
    ⬛⬜⬛⬜⬜🔴⬛
    ⬛⬜⬛⬜⬛🔴⬛
    ⬛⬜⬜⬜⬛🔴⬛
    ⬛⬛⬛⬛⬛🔴⬛
    <BLANKLINE>
    """
    texte=""
    copie=copy.deepcopy(graphe)
    chemin=solution(copie)
    for i in range(len(graphe)):
        for j in range(len(graphe[0])):
            if graphe[i][j]==1:
                texte+="⬛"
            elif (i,j) in chemin :
                texte+="🔴"
            else:
                texte+="⬜"           
        texte+="\n"
    print(texte)


if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)
```