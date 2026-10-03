
def situation_init():
    """
    : création de la situation initiale du jeu
    : renvoie le plateau initiale
    : param : Rien
    Exemple:
    """
    plateau=[
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 3, 1, 0, 0, 0],
    [0, 0, 0, 1, 3, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]]
    return plateau


def aff_evolution_jeu(plateau):
    """
    : permet d'afficher le plateau
    : param : int(param_jeu) nombres d'allumettes
    : return : None
    Exemple:
    >>> aff_evolution_jeu(situation_init())
      1 2 3 4 5 6 7 8
    1 · · · · · · · ·
    2 · · · · · · · ·
    3 · · · · · · · ·
    4 · · · □ ■ · · ·
    5 · · · ■ □ · · ·
    6 · · · · · · · ·
    7 · · · · · · · ·
    8 · · · · · · · ·
    """
    print("  1 2 3 4 5 6 7 8")
    for ligne in range(len(plateau)):
        print(ligne+1,end="")
        for colonne in range(len(plateau[0])):
            if plateau[ligne][colonne]==0:
                print(" ·",end="")
            if plateau[ligne][colonne]==3:
                print(" □",end="")
            if plateau[ligne][colonne]==1:
                print(" ■",end="")
        print()    

import copy

def evolution_jeu(valeur_joueur,plateau,choix_joueur):
    """
    : permet de faire évoluer le jeu
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : param : plateau : list
    : param : choix_joueur : tuple: 
    return : le nouveau plateau : list
    >>> aff_evolution_jeu(situation_init())
      1 2 3 4 5 6 7 8
    1 · · · · · · · ·
    2 · · · · · · · ·
    3 · · · · · · · ·
    4 · · · □ ■ · · ·
    5 · · · ■ □ · · ·
    6 · · · · · · · ·
    7 · · · · · · · ·
    8 · · · · · · · ·
    >>> aff_evolution_jeu(evolution_jeu(True,situation_init(),(4,6)))
      1 2 3 4 5 6 7 8
    1 · · · · · · · ·
    2 · · · · · · · ·
    3 · · · · · · · ·
    4 · · · □ □ □ · ·
    5 · · · ■ □ · · ·
    6 · · · · · · · ·
    7 · · · · · · · ·
    8 · · · · · · · ·
    >>> aff_evolution_jeu(evolution_jeu(False,situation_init(),(6,5)))
      1 2 3 4 5 6 7 8
    1 · · · · · · · ·
    2 · · · · · · · ·
    3 · · · · · · · ·
    4 · · · □ ■ · · ·
    5 · · · ■ ■ · · ·
    6 · · · · ■ · · ·
    7 · · · · · · · ·
    8 · · · · · · · ·
    >>> plateau_exemple=[[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 3, 1, 0, 0, 0],[0, 0, 0, 3, 1, 3, 0, 0],[0, 0, 0, 3, 1, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0]]
    >>> aff_evolution_jeu(plateau_exemple)
      1 2 3 4 5 6 7 8
    1 · · · · · · · ·
    2 · · · · · · · ·
    3 · · · □ ■ · · ·
    4 · · · □ ■ □ · ·
    5 · · · □ ■ · · ·
    6 · · · · · · · ·
    7 · · · · · · · ·
    8 · · · · · · · ·
    >>> aff_evolution_jeu(evolution_jeu(True,plateau_exemple,(3,6)))
      1 2 3 4 5 6 7 8
    1 · · · · · · · ·
    2 · · · · · · · ·
    3 · · · □ □ □ · ·
    4 · · · □ □ □ · ·
    5 · · · □ ■ · · ·
    6 · · · · · · · ·
    7 · · · · · · · ·
    8 · · · · · · · ·
    >>> config=evolution_jeu(False,plateau_exemple,(2,5))
    >>> aff_evolution_jeu(config)
      1 2 3 4 5 6 7 8
    1 · · · · · · · ·
    2 · · · · ■ · · ·
    3 · · · □ ■ · · ·
    4 · · · □ ■ □ · ·
    5 · · · □ ■ · · ·
    6 · · · · · · · ·
    7 · · · · · · · ·
    8 · · · · · · · ·
    >>> config1=[[0, 0, 3, 1, 1, 1, 0, 0],[0, 3, 3, 3, 1, 1, 0, 1],[0, 0, 3, 1, 3, 1, 3, 0],[0, 0, 3, 1, 1, 1, 3, 3],[0, 0, 3, 3, 1, 3, 0, 0],[1, 1, 1, 3, 3, 3, 1, 0],[1, 1, 1, 1, 3, 3, 0, 1],[3, 3, 3, 3, 3, 3, 0, 0]]
    >>> aff_evolution_jeu(config1)
      1 2 3 4 5 6 7 8
    1 · · □ ■ ■ ■ · ·
    2 · □ □ □ ■ ■ · ■
    3 · · □ ■ □ ■ □ ·
    4 · · □ ■ ■ ■ □ □
    5 · · □ □ ■ □ · ·
    6 ■ ■ ■ □ □ □ ■ ·
    7 ■ ■ ■ ■ □ □ · ■
    8 □ □ □ □ □ □ · ·
    >>> config2=evolution_jeu(True,config1,(1,7))
    >>> aff_evolution_jeu(config2)
      1 2 3 4 5 6 7 8
    1 · · □ □ □ □ □ ·
    2 · □ □ □ ■ □ · ■
    3 · · □ ■ □ ■ □ ·
    4 · · □ ■ ■ ■ □ □
    5 · · □ □ ■ □ · ·
    6 ■ ■ ■ □ □ □ ■ ·
    7 ■ ■ ■ ■ □ □ · ■
    8 □ □ □ □ □ □ · ·
    """
    copie_plateau=copy.deepcopy(plateau)
    directions=[(1,0),(-1,0),(1,1),(1,-1),(0,1),(0,-1),(-1,-1),(-1,1)]
    position=(choix_joueur[0]-1,choix_joueur[1]-1)
    x=position[0]
    y=position[1]
    if valeur_joueur==True:
        copie_plateau[x][y]=3
    else:
        copie_plateau[x][y]=1
    for direction in directions:
            #attention de réinitialiser x,y pour chaque nouvelle direction !
            x=position[0]
            y=position[1]
            modifications=[]
            while x+direction[0]>=0 and x+direction[0]<len(plateau) and y+direction[1]>=0 and y+direction[1]<len(plateau[0]) and abs(copie_plateau[position[0]][position[1]]-copie_plateau[x+direction[0]][y+direction[1]])==2:
                x=x+direction[0]
                y=y+direction[1]
                modifications.append((x,y))
            if modifications !=[] and x+direction[0]>=0 and x+direction[0]<len(plateau) and y+direction[1]>=0 and y+direction[1]<len(plateau[0]) and copie_plateau[x+direction[0]][y+direction[1]]==copie_plateau[position[0]][position[1]]:
                for modification in modifications:
                    copie_plateau[modification[0]][modification[1]]=copie_plateau[position[0]][position[1]]
    return copie_plateau
    
    
def compteur_pieces(valeur_joueur,param_jeu):
    """
    Compte le nombre de pièces du joueur
    param : valeur_joueur : bool
    param : param_jeu : list
    >>> aff_evolution_jeu(situation_init())
      1 2 3 4 5 6 7 8
    1 · · · · · · · ·
    2 · · · · · · · ·
    3 · · · · · · · ·
    4 · · · □ ■ · · ·
    5 · · · ■ □ · · ·
    6 · · · · · · · ·
    7 · · · · · · · ·
    8 · · · · · · · ·
    >>> compteur_pieces(True,situation_init())
    2
    >>> compteur_pieces(False,situation_init())
    2
    """
    if valeur_joueur==True:
        recherche=3
    else:
        recherche=1
    compteur=0
    for ligne in range(len(param_jeu)):
        for colonne in range(len(param_jeu[0])):
            if param_jeu[ligne][colonne]==recherche:
                compteur+=1
    return compteur

def test_jeu_rempli(param_jeu):
    """
    Renvoie True si le jeu est rempli sinon False
    """
    for ligne in range(len(param_jeu)):
        for colonne in range(len(param_jeu[0])):
            if param_jeu[ligne][colonne]==0:
                return False
    return True    

def etat_final(param_jeu):
    """
    : vérification si fin jeu
    : return : bool(fini), bool(per_gag)
    per_gag vaut True en cas d'égalité, False sinon.
    """
    fini = test_jeu_rempli(param_jeu)
    if not fini:
        return False, False
    nb_joueur_I = compteur_pieces(True, param_jeu)
    nb_joueur_II = compteur_pieces(False, param_jeu)
    per_gag = (nb_joueur_I == nb_joueur_II)
    return fini, per_gag

def test_validite_choix(valeur_joueur,le_choix,plateau):
    """
    : test de la validité de la position
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : param le_choix: tuple
    : param plateau : la grille de jeu
    : return : le choix validé ou non du joueur
    >>> aff_evolution_jeu(situation_init())
      1 2 3 4 5 6 7 8
    1 · · · · · · · ·
    2 · · · · · · · ·
    3 · · · · · · · ·
    4 · · · □ ■ · · ·
    5 · · · ■ □ · · ·
    6 · · · · · · · ·
    7 · · · · · · · ·
    8 · · · · · · · ·
    >>> test_validite_choix(False,(4,6),situation_init())
    True
    >>> test_validite_choix(True,(10,10),situation_init())
    False
    >>> test_validite_choix(True,(3,5),situation_init())
    True
    >>> test_validite_choix(False,(5,5),situation_init())
    False
    """
    ligne=le_choix[0]-1
    colonne=le_choix[1]-1
    if ligne>=0 and ligne<len(plateau) and colonne>=0 and colonne<len(plateau[0]) and plateau[ligne][colonne]==0:
        return True
    return False

def choix_joueur(valeur_joueur,param_jeu):
    """
    : Demande au joueur d'effectuer un choix de position
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : param : l
    : return : int(choix) choix du joueur
    Remarque: Ne pas faire de doctest sur des fonctions d'entrées /sorties
    """
    if valeur_joueur:
        joueur='I'
    else:
        joueur='II'
    #init choix jeu
    x,y=0,0
    #Les joueurs doivent ramasser tour à tour 2 ou 3 allumettes
    while (x<1 or x>8 or y<1 or y>8):
        reponse= input('JOUEUR {} : choisir la position de votre pion par exemple 3,5 : '.format(joueur))
        x=int(reponse[0])
        y=int(reponse[2])
        if test_validite_choix(valeur_joueur,(x,y),param_jeu):
            return (x,y)

def action_joueur(valeur_joueur,param_jeu):
    """
    : permet de connaitre le nombre d'allumettes à enlever
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : return : int(choix) choix du joueur
    """
    lechoix=choix_joueur(valeur_joueur,param_jeu)
    return lechoix

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
