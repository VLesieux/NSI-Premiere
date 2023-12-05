lab1 = [[1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1],[1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],[1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],[2, 0, 1, 0, 0, 0, 1, 0, 1, 0, 3],[1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],[1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],[1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1],[1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1],[1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1]]

lab2 = [[1, 1, 1, 1, 1, 1, 1],[2, 0, 0, 0, 0, 0, 1],[1, 1, 1, 1, 1, 0, 1],[1, 0, 1, 0, 0, 0, 1],[1, 0, 1, 0, 1, 0, 1],[1, 0, 0, 0, 1, 0, 1],[1, 1, 1, 1, 1, 3, 1]]

def est_valide(i,j,n,m):
    """
    Renvoie True si le couple (i,j) correspond à des coordonnées valides pour un
    labyrinthe de taille (n,m) et False sinon
    >>> est_valide(5, 2, 10, 10)
    True
    >>> est_valide(-3, 4, 10, 10)
    False
    """
    if i>=0 and i<=n-1 and j>=0 and j<=n-1:
        return True
    else:
        return False

def depart(lab):
    """
    renvoie, sous la forme d'un tuple, les coordonnées du départ d'un labyrinthe
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
    Renvoie le nombre de cases vides du labyrinthe y-compris le départ et l'arrivée
    >>> nb_cases_vides(lab2)
    19
    """
    compteur=0
    n=len(lab)
    m=len(lab[0])
    for ligne in range(n):
        for colonne in range(m):
            if lab[ligne][colonne]==0 or lab[ligne][colonne]==3 or lab[ligne][colonne]==2:
                compteur+=1
    return compteur


def voisines(i,j,lab):
    """
    Renvoie la liste des coordonnées des cases voisines de la case de coordonnées (i,j)
    qui sont valides, non visitées (différents de 4) et qui ne sont pas des murs
    >>> voisines(1, 1, [[1, 1, 1], [4, 0, 0], [1, 0, 1]])
    [(1, 2), (2, 1)]
    """
    liste=[]
    n=len(lab)
    m=len(lab[0])
    voisins=[(i,j-1),(i-1,j),(i+1,j),(i,j+1)]
    for ligne in range(n):
        for colonne in range(m):
            if est_valide(ligne,colonne,n,m) and lab[ligne][colonne] !=1 and lab[ligne][colonne] !=4 and (ligne,colonne) in voisins:
                liste.append((ligne,colonne))
    return liste


def solution(lab):
    """
    Renvoie le chemin solution du labyrinthe représenté par lab
    >>> solution(lab2)
    [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5)]
    """
    chemin=[depart(lab)]
    case=chemin[0]
    i=case[0]
    j=case[1]
    while lab[i][j] != 3:
        lab[i][j]=4
        voisins=voisines(i,j,lab)
        if len(voisins) !=0:                   
            case=voisins.pop()
            i=case[0]
            j=case[1]
            chemin.append((i,j))
        else:
            chemin.pop()
            i=chemin[-1][0]
            j=chemin[-1][1]
    return chemin    



if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)