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

def aff_evolution_jeu(param_jeu):
    """
    : permet d'afficher le nombre d'allumettes restantes
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
    affichage="  1 2 3 4 5 6 7 8\n"
    for i in range(len(param_jeu)):
        affichage+=str(i+1)
        for j in range(len(param_jeu[0])):
            if param_jeu[i][j]==0:
                affichage+=" ·"
            elif param_jeu[i][j]==1:
                affichage+=" ■"
            else:
                affichage+=" □"
        affichage+="\n"
    affichage=affichage[0:-1]
    print(affichage)

import copy

def evolution_jeu(valeur_joueur,param_jeu,choix_joueur):
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
    3 · · · □ ■ □ · ·
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
    initial=copy.deepcopy(param_jeu)
    evolution=False
    i=choix_joueur[0]-1
    j=choix_joueur[1]-1
    
    if valeur_joueur==True:
        param_jeu[i][j]=3
    else:
        param_jeu[i][j]=1    
        
    directions=[(-1,0),(1,0),(0,1),(0,-1),(1,1),(-1,1),(-1,-1),(1,-1)]

    for direction in directions:
        k=i+direction[0]
        l=j+direction[1]
        cases=[] 
        while k>=0 and k<=7 and l>=0 and l<=7 and abs(param_jeu[i][j]-param_jeu[k][l])==2:
            cases.append((k,l))
            k=k+direction[0]
            l=l+direction[1]
        if k>=0 and k<=7 and l>=0 and l<=7 and param_jeu[k][l]==param_jeu[i][j]:
            for case in cases:
                param_jeu[case[0]][case[1]]=param_jeu[i][j]
                evolution=True
    if evolution:
        return param_jeu
    else:
        return initial
            
def test_jeu_rempli(param_jeu):
    """
    Renvoie True si le jeu est rempli sinon False
    """
    for i in range(len(param_jeu)):
        for j in range(len(param_jeu[0])):
            if param_jeu[i][j]==0:
                return False
    return True


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
    compteur=0
    if valeur_joueur==True:
        for i in range(len(param_jeu)):
            for j in range(len(param_jeu[0])):
                if param_jeu[i][j]==3:
                    compteur+=1
    else:
        for i in range(len(param_jeu)):
            for j in range(len(param_jeu[0])):
                if param_jeu[i][j]==1:
                    compteur+=1
    return compteur


def etat_final(param_jeu):
    """
    : vérification si fin jeu
    : param : int(param_jeu)
    : return : bool(fini),bool(per_gag)
    """
    per_gag=False
    fini=False
    #per_gag=True désigne le cas d'égalité
    #fini désigne l'état de la partie qui est finie ou non
    if test_jeu_rempli(param_jeu):
        fini=True
        if compteur_pieces(True,param_jeu)>compteur_pieces(False,param_jeu):
            per_gag=True
        else:
            per_gag=False
    return fini,per_gag

def test_validite_choix(valeur_joueur,lechoix,param_jeu):
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
    False
    >>> test_validite_choix(True,(10,10),situation_init())
    False
    >>> test_validite_choix(True,(3,5),situation_init())
    True
    >>> test_validite_choix(False,(6,5),situation_init())
    True
    """
    possibles=[1,2,3,4,5,6,7,8]
    if lechoix[0] not in possibles or lechoix[1] not in possibles:
        return False        
    if param_jeu==evolution_jeu(valeur_joueur,param_jeu,lechoix):
        return True
    else:
        return False
        
def choix_joueur(valeur_joueur,param_jeu):
    """
    : Demande au joueur d'effectuer un choix de position
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : param : param_jeu : list : la grille
    : return : choix du joueur
    Remarque: Ne pas faire de doctest sur des fonctions d'entrées /sorties
    """
    if valeur_joueur:
        joueur='I'
    else:
        joueur='II'

    choix=False
    #Les joueurs doivent ramasser tour à tour 2 ou 3 allumettes
    while choix !=True:
        question= input('JOUEUR {} : Choisir la position de votre pion par exemple 1,1 : '.format(joueur))
        position= int(question[0]),int(question[2])
        choix=test_validite_choix(valeur_joueur,position,param_jeu)
        if choix:
            return position


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
