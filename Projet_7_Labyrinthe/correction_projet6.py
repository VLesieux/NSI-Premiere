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
    """
    texte=""
    for i in range(len(graphe)):
        for j in range(len(graphe[0])):
            if graphe[i][j]==1:
                texte+="⬛"
            else:
                texte+="⬜"
    
        texte+="\n"
    texte=texte.strip("\n")
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
    return i >=0 and j >=0 and i<len(graphe) and j < len(graphe[0])

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
                return (i,j)
            

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
                return (i,j)    

def nombre_cases_vides(graphe):
    """
    Renvoie le nombre de cases vides(0) du graphe, l'entrée(2), la sortie(3), les cases visitées (4) comprises.
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

def voisines_valides(i,j,graphe):
    """
    Renvoie la liste des cases valides voisines, non visités (!=4) et qui ne sont pas des murs autour de la case (x,y)
    param : i : int
    param : j : int
    param : graphe : list
    return : list
    >>> voisines_valides(1,5,lab1)
    [(2, 5), (1, 4)]
    """
    possibles=[(i-1,j), (i+1,j), (i, j-1), (i, j+1)]
    solution=[]
    for element in possibles:
        if graphe[element[0]][element[1]]!=1 and graphe[element[0]][element[1]]!=4:#ni mur ni déjà visité
            solution.append(element)
    return solution
import copy
            
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
    copie=copy.deepcopy(graphe)
    copie[i][j]=4
    return copie

def solution(graphe):
    """
    Renvoie la solution du labyrinthe
    param : lab :list
    return : list
    >>> solution(lab1)
    [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5)]
    """
    chemin=[entree(graphe)]
    graphe=marquer_case(entree(graphe)[0],entree(graphe)[1],graphe)
    while graphe[chemin[-1][0]][chemin[-1][1]] !=3:
        voisines=voisines_valides(chemin[-1][0],chemin[-1][1],graphe)
        if len(voisines)>0:
            chemin.append(voisines[0])
            if graphe[chemin[-1][0]][chemin[-1][1]] ==3:
                return chemin
            graphe=marquer_case(chemin[-1][0],chemin[-1][1],graphe)
        else:            
            chemin.pop()
                   

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
    """
    texte=""
    for i in range(len(graphe)):
        for j in range(len(graphe[0])):
            if graphe[i][j]==1:
                texte+="⬛"
            elif (i,j) in solution(graphe):
                texte+="🔴"
            else:
                texte+="⬜"
    
        texte+="\n"
        
    texte=texte.strip("\n")
    print(texte)    




if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)



