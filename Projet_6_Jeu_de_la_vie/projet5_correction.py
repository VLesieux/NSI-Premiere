def creer_grille(nb_colonnes,nb_lignes):
    """
    renvoie une grille vide comportant nb_lignes et nb_colonnes
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

from random import *

def aleatoire(probabilite):
    valeur=0
    if random()<probabilite:
        valeur=1
    return valeur

def creer_grille_aleatoire(nb_lignes,nb_colonnes,probabilite):
    return [[aleatoire(probabilite) for i in range(nb_colonnes)] for j in range(nb_lignes)]
    

Grille = [[0, 1, 0], [1, 0, 0], [1, 1, 1]]

def voisins_case(grille,abscisse,ordonnee):
    """
    renvoie la liste des voisins d'une case
    >>> voisins_case(Grille, 1, 1)
    [0, 1, 0, 1, 0, 1, 1, 1]
    >>> voisins_case(Grille, 2, 2)
    [0, 0, 1]
    >>> voisins_case(Grille, 0, 2)
    [1, 0, 0]
    """
    voisins=[]
    for j in range(-1,2):
       for i in range(-1,2):
           if i==0 and j==0:
               continue
           if abscisse+j>=0 and ordonnee+i>=0:
               if abscisse+j<hauteur_grille(grille) and ordonnee+i<largeur_grille(grille):
                   voisins.append(grille[abscisse+j][ordonnee+i])
    return voisins


def nb_cellules_voisines(grille,abscisse,ordonnee):
    """
    renvoie le nombre de cases voisines de la case passée en paramètre
    >>> nb_cellules_voisines(Grille, 1, 1)
    5
    >>> nb_cellules_voisines(Grille, 2, 2)
    1
    """
    return len([element for element in voisins_case(grille,abscisse,ordonnee) if element==1])


def afficher_grille(grille):
    """
    affiche la grille
    >>> afficher_grille(Grille)
     _  O  _ 
     O  _  _ 
     O  O  O 
    >>> afficher_grille(creer_grille(3, 2))
     _  _  _ 
     _  _  _ 
    """
    texte=""
    for i in range(hauteur_grille(grille)):
        for j in range(largeur_grille(grille)):
            if grille[i][j]==1:
                texte+=" O "
            else:
                texte+=" _ "
        texte+="\n"
    texte=texte.strip("\n")
    print(texte)

import copy


def generation_suivante(grille):
    """
    Calcule la grille après la génération suivante
    >>> generation_suivante(Grille)
    [[0, 0, 0], [1, 0, 1], [1, 1, 0]]
    >>> generation_suivante([[0, 0, 0], [1, 0, 1], [1, 1, 0]])
    [[0, 0, 0], [1, 0, 0], [1, 1, 0]]
    >>> generation_suivante([[0, 0, 0], [1, 0, 0], [1, 1, 0]])
    [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    """
    copie = copy.deepcopy(grille)
    for ligne in range(hauteur_grille(grille)):
        for colonne in range(largeur_grille(grille)):
            if nb_cellules_voisines(grille,ligne,colonne)==3:
                copie[ligne][colonne]=1
            if nb_cellules_voisines(grille,ligne,colonne)<2 or nb_cellules_voisines(grille,ligne,colonne)>3:
                copie[ligne][colonne]=0
    return copie

import time

def evolution_n_generations(grille,n):
    for i in range(n):
        grille=generation_suivante(grille)
        afficher_grille(grille)
        time.sleep(1.0)
        print()

##oscillateur à deux états
Grille1=[[0, 0, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 0, 0]]


##planeur
Grille2=[[0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]




if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)