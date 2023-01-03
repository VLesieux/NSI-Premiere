def creer_grille(nb_colonnes,nb_lignes):
    """
    renvoie une grille vide comportant nb_lignes et nb_colonnes
    >>> creer_grille(3, 2)
    [[0, 0, 0], [0, 0, 0]]
    """
    return [[0 for i in range(nb_colonnes) ] for i in range(nb_lignes)]



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
#importation de toutes les fonctions du module random
#et en particulier la fonction random() 
def aleatoire(probabilite):
    valeur=0
    if random()<probabilite:
        valeur=1
    return valeur



def creer_grille_aleatoire(nb_colonnes,nb_lignes,p):
    return [[aleatoire(p) for i in range(nb_colonnes) ] for i in range(nb_lignes)]


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
                pass
            elif abscisse+j>=0 and ordonnee+i>=0:
                try:
                    voisins.append(grille[abscisse+j][ordonnee+i])
                except IndexError:
                    pass
    return voisins


def nb_cellules_voisines(grille,abscisse,ordonnee):
    """
    renvoie le nombre de cases voisines de la case passée en paramètre
    >>> nb_cellules_voisines(Grille, 1, 1)
    5
    >>> nb_cellules_voisines(Grille, 2, 2)
    1
    """
    compteur=0
    for element in voisins_case(grille,abscisse,ordonnee):
        if element==1:
            compteur+=1
    return compteur

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
    for ligne in range(len(grille)):
        for colonne in range(len(grille[0])):
            if grille[ligne][colonne]==0:
                texte+=" _ "
            else:
                texte+=" O "
        texte+="\n"
    texte=texte.strip("\n")
    print(texte)
            
    
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
    import copy
    copie = copy.deepcopy(grille)
    for ligne in range(len(grille)):
        for colonne in range(len(grille[0])):
            if nb_cellules_voisines(grille,ligne,colonne)==3:
                copie[ligne][colonne]=1
            elif nb_cellules_voisines(grille,ligne,colonne)<2 or nb_cellules_voisines(grille,ligne,colonne)>3:
                copie[ligne][colonne]=0
    return copie

import time

def evolution_n_generations(n,grille):
    for i in range(n):
        grille=generation_suivante(grille)
        afficher_grille(grille)
        time.sleep(1.0)
        print()
    
#grille_depart1=[[0, 0, 1, 0], [1, 0, 0, 1], [1, 0, 0, 1], [0, 1, 0, 0]]
#grille_depart2=[[0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [1, 1, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
#
#evolution_n_generations(10,grille_depart1)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)