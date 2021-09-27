from random import *
import copy
import time

def creer_grille(nb_colonnes,nb_lignes):
    """
    renvoie une grille vide comportant nb_lignes et nb_colonnes colonnes
    >>> creer_grille(3, 2)
    [[0, 0, 0], [0, 0, 0]]
    """
    return [[0 for i in range(nb_colonnes)] for j in range(nb_lignes)]


def hauteur_grille(grille):
    """
    renvoie le nombre de lignes d'une grille
    >>> hauteur_grille(creer_grille(3, 2))
    2
    """    
    return len(grille)

def largeur_grille(grille):
    """
    renvoie le nombre de colonnes d'une grille
    >>> largeur_grille(creer_grille(3, 2))
    3
    """    
    return len(grille[0])

def aleatoire(probabilite):
    valeur=0
    if random()<probabilite:
        valeur=1
    return valeur

def creer_grille_aleatoire(nb_colonnes,nb_lignes,probabilite):
    grille=[[aleatoire(probabilite) for i in range(nb_colonnes)] for j in range(nb_lignes)]
    return grille

grille = [[0, 1, 0], [1, 0, 0], [1, 1, 1]]

def voisins_case(grille,abscisse,ordonnee):
    """
    renvoie la liste des voisins d'une case

    >>> voisins_case(grille, 1, 1)
    [0, 1, 0, 1, 0, 1, 1, 1]
    >>> voisins_case(grille, 2, 2)
    [0, 0, 1]
    >>> voisins_case(grille, 0, 2)
    [1, 0, 1]
    """
    cases_voisines=[]
    for j in range(-1,2):
        for i in range(-1,2):
            if i==0 and j==0:
                continue
            if ordonnee+j<0 or abscisse+i<0:
                continue
            try:
                cases_voisines.append(grille[ordonnee+j][abscisse+i])
            except IndexError:
                pass
    return cases_voisines

def nb_cellules_voisins(grille,abscisse,ordonnee):
    """
    renvoie le nombre de cases voisines de la case passée en paramètre
    >>> nb_cellules_voisins(grille, 1, 1)
    5
    >>> nb_cellules_voisins(grille, 2, 2)
    1
    """
    compte=0
    for i in voisins_case(grille,abscisse,ordonnee):
        if i==1:
            compte+=1
    return compte
    
def afficher_grille(grille):
    """
    affiche la grille
    >>> afficher_grille(grille)
    _ O _ 
    O _ _ 
    O O O 
    >>> afficher_grille(creer_grille(3, 2))
    _ _ _ 
    _ _ _ 
    
    """
    affichage=""
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j]==0:
                affichage+="_"
            else:
                affichage+="O"
            if j>0 or j<len(grille[0])-1:
                affichage+=" "
        if i<len(grille)-1:
            affichage+="\n"
    print(affichage)
        
    
def generation_suivante(grille):
    """
    Calcule la grille après la génération suivante
    >>> generation_suivante(grille)
    [[0, 0, 0], [1, 0, 1], [1, 1, 0]]
    >>> generation_suivante([[0, 0, 0], [1, 0, 1], [1, 1, 0]])
    [[0, 0, 0], [1, 0, 0], [1, 1, 0]]
    >>> generation_suivante([[0, 0, 0], [1, 0, 0], [1, 1, 0]])
    [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    """
    copie = copy.deepcopy(grille)
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if nb_cellules_voisins(grille,j,i)==3:
                copie[i][j]=1
            elif nb_cellules_voisins(grille,j,i)<2 or nb_cellules_voisins(grille,j,i)>3:
                copie[i][j]=0
    return copie

def evolution_n_generations(grille,n):
    j=0
    while j<n:
        j+=1
        time.sleep(1.0)
        print()
        grille=generation_suivante(grille)
        afficher_grille(grille)
    


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)