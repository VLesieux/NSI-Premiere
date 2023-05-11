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
    [0, 0, 0, 2, 1, 0, 0, 0],
    [0, 0, 0, 1, 2, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]]
    return plateau

def aff_evolution_jeu(plateau):
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
    print("  1 2 3 4 5 6 7 8")
    numero=1
    for ligne in plateau:
        print(numero,end=' ')
        for element in ligne:
            if element==0:
                print('\u00B7',end=' ')
            if element==1:
                print( '■',end=' ')
            if element==2:
                print( '□',end=' ')
        numero+=1
        print()

def test_jeu_rempli(plateau):
    """
    >>> test_jeu_rempli(situation_init())
    False
    """
    for i in range(3):
        for j in range(3):
            if plateau[i][j]==0:
                return False
    return True

def choix_joueur(valeur_joueur,plateau):
    """
    : Demande au joueur d'effectuer un choix d'allumettes à enlever (2 ou 3)
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : param : int(param_jeu) nombres d'allumettes
    : return : int(choix) choix du joueur
    Remarque: Ne pas faire de doctest sur des fonctions d'entrées /sorties
    """
    if valeur_joueur:
        joueur='I'
    else:
        joueur='II'
    #init choix jeu
    position=3,3
    #Les joueurs doivent ramasser tour à tour 2 ou 3 allumettes
    while not (position[0] in [1,2,3,4,5,6,7,8] and position[1] in [1,2,3,4,5,6,7,8]):
        question= input('JOUEUR {} : Choisir la position de votre pion par exemple 1,1 : '.format(joueur))
        position= int(question[0]),int(question[2])
    choix=test_validite_choix(valeur_joueur,position,plateau)
    return position

def evolution_jeu(valeur_joueur,plateau,choix_joueur):
    """
    : permet de faire évoluer le jeu
    : param : int(param_jeu) nombres d'allumettes
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : return : int(param_jeux) le nombres d'allumettes restantes
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
    4 · · · □ ■ □ · · 
    5 · · · ■ □ · · · 
    6 · · · · · · · · 
    7 · · · · · · · · 
    8 · · · · · · · · 
    """
    if valeur_joueur==True:
        plateau[choix_joueur[0]-1][choix_joueur[1]-1]=2
    else:
        plateau[choix_joueur[0]-1][choix_joueur[1]-1]=1  
    return plateau

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
    >>> test_validite_choix(True,(4,6),situation_init())
    True
    >>> test_validite_choix(True,(3,5),situation_init())
    True
    >>> aff_evolution_jeu(evolution_jeu(True,situation_init(),(3,6)))
      1 2 3 4 5 6 7 8
    1 · · · · · · · · 
    2 · · · · · · · · 
    3 · · · · · □ · · 
    4 · · · □ ■ · · · 
    5 · · · ■ □ · · · 
    6 · · · · · · · · 
    7 · · · · · · · · 
    8 · · · · · · · · 
    >>> test_validite_choix(True,(6,3),evolution_jeu(True,situation_init(),(3,6)))
    True
    """
    if valeur_joueur==True:
        pion=2
    else:
        pion=1
    directions=[(-1,0),(1,0),(0,1),(0,-1),(-1,1),(1,-1),(1,1),(-1,-1)]
    position_choisi=[le_choix[0]-1,le_choix[1]-1]
    for direction in directions:
        position=position_choisi
        while plateau[position[0]+direction[0]][position[1]+direction[1]]==3-pion:
            position[0]=position[0]+direction[0]
            position[1]=position[1]+direction[1]
        if plateau[position[0]+direction[0]][position[1]+direction[1]]==pion:
            return True
    return False
           
  
#
# def action_joueur(valeur_joueur,param_jeu):
#     """
#     : permet de connaitre le nombre d'allumettes à enlever
#     : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
#     : return : int(choix) choix du joueur
#     """
#     lechoix=choix_joueur(valeur_joueur,param_jeu)
#     return lechoix
#

#

           
       

# def etat_final(plateau):
#     """
#     >>> etat_final([['-', 'X', '-'], ['X', 'X', 'X'], ['0', '-', '0']])
#     (True, False)
#     >>> etat_final([['X', 'X', '0'], ['X', '0', 'X'], ['0', 'X', '0']])
#     (True, False)
#     """
#     per_gag=False
#     fini=False
#    
#     #per_gag=True désigne le cas d'égalité
#     #fini désigne l'état de la partie qui est finie ou non
#     if (test_ligne(plateau)|test_diagonale1(plateau)|test_diagonale2(plateau)|test_colonne(plateau)):
#         fini=True
#         return fini,per_gag
#     else:
#         fini=False
#         if test_jeu_rempli(plateau):
#             per_gag=True
#         return fini,per_gag


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)