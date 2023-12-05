lab1=[  
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

lab2=[
[1,1,1,1,1,1,1],
[2,0,0,0,0,0,1],
[1,1,1,1,1,0,1],
[1,0,1,0,0,0,1],
[1,0,1,0,1,0,1],
[1,0,0,0,1,0,1],
[1,1,1,1,1,3,1]
]


def est_valide(i,j,n,m):
    """
    Renvoie True si i<=n et j<=m sinon False
    >>> est_valide(5,2,10,10)
    True
    >>> est_valide(-3,4,10,10)
    False
    """
    return (i>=0 and j>=0 and i<=n-1 and j<=m-1)
   
def depart(lab):
    """
    Renvoie la position de l'entrée du lab
    param : lab : list
    return : tuple
    >>> depart(lab1)
    (5, 0)
    """
    n=len(lab)
    m=len(lab[0])
    for ligne in range(n):
        for colonne in range(m):
            if lab[ligne][colonne]==2:
                return (ligne,colonne)
   
def nb_cases_vides(lab):
    """
    Renvoie le nombre de cases vides
    param : lab : list
    return : tuple
    >>> nb_cases_vides(lab1)
    58
    """
    compteur=0
    n=len(lab)
    m=len(lab[0])
    for ligne in range(n):
        for colonne in range(m):
            if lab[ligne][colonne]==0 or lab[ligne][colonne]==2 or lab[ligne][colonne]==3 :
                compteur+=1
    return compteur

def voisines(i,j,lab):
    """
    Renvoie la liste des cases voisines de (i,j)
    param : i : int
    param : j : int
    param : lab : list
    >>> voisines(1,1,[[1,1,1],[4,0,0],[1,0,1]])
    [(2, 1), (1, 2)]
    """
    n=len(lab)
    m=len(lab[0])
    cases_voisines=[(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
    cases_retenues=[]
    for case in cases_voisines:
        if lab[case[0]][case[1]]==0 or lab[case[0]][case[1]]==3 and est_valide(case[0],case[1],n,m):
            cases_retenues.append(case)
    return cases_retenues


def solution(lab):
    """
    Renvoie la solution du labyrinthe
    param : lab :list
    return : list
    >>> solution(lab2)
    [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5)]
    """
    chemin=[depart(lab)]
    case=chemin[0]
    i=case[0]
    j=case[1]
    while lab[i][j]!=3:
        lab[i][j]=4
        voisins=voisines(i,j,lab)
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
       

   
   
   
   
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)