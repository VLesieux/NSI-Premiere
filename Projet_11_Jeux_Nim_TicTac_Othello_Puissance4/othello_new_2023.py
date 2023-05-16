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

def compte_points(plateau):
    """
    Renvoie le couple compte_blanc, compte_noir
    >>> plateau=[[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 2, 1, 0, 0, 0],[0, 0, 0, 1, 2, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0, 0, 0]]
    >>> compte_points(plateau)
    (2, 2)
    """
    compte_blanc=0
    compte_noir=0
    for i in range(8):
        for j in range(8):
            if plateau[i][j]==1:
                compte_noir+=1
            elif plateau[i][j]==2:
                compte_blanc+=1
    return compte_blanc,compte_noir


def test_jeu_rempli(plateau):
    """
    >>> test_jeu_rempli(situation_init())
    False
    """
    for i in range(8):
        for j in range(8):
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
        joueur='I blanc'
    else:
        joueur='II noir'
    #init choix jeu
    choix=False
    #Les joueurs doivent ramasser tour à tour 2 ou 3 allumettes
    while choix !=True:
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
    4 · · · □ □ □ · · 
    5 · · · ■ □ · · · 
    6 · · · · · · · · 
    7 · · · · · · · · 
    8 · · · · · · · · 
    """
    liste=[]
    if valeur_joueur==True:
        pion=2
        plateau[choix_joueur[0]-1][choix_joueur[1]-1]=2
    else:
        pion=1
        plateau[choix_joueur[0]-1][choix_joueur[1]-1]=1  
    directions=[(-1,0),(1,0),(0,1),(0,-1),(-1,1),(1,-1),(1,1),(-1,-1)]
    for direction in directions:
        liste=[]
        direction_x=direction[0]
        direction_y=direction[1]
        x,y=choix_joueur[0]-1,choix_joueur[1]-1
        while y+direction_y>=0 and y+direction_y<len(plateau[0]) and x+direction_x>=0 and x+direction_x<len(plateau) and plateau[x+direction_x][y+direction_y]==3-pion:
            liste.append((x+direction_x,y+direction_y))
            x,y=x+direction_x,y+direction_y
            if len(liste)>0 and liste[-1][1]+direction_y>=0 and liste[-1][1]+direction_y<len(plateau[0]) and liste[-1][0]+direction_x>=0 and liste[-1][0]+direction_x<len(plateau) and plateau[liste[-1][0]+direction_x][liste[-1][1]+direction_y]==pion:
                for element in liste:
                    plateau[element[0]][element[1]]=pion
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
    >>> test_validite_choix(True,(2,2),situation_init())
    False
    >>> test_validite_choix(True,(3,5),situation_init())
    True
    >>> test_validite_choix(False,(3,4),situation_init())
    True
    >>> test_validite_choix(False,(4,6),situation_init())
    False
    >>> test_validite_choix(False,(4,4),situation_init())
    False
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
    >>> test_validite_choix(False,(4,3),evolution_jeu(True,situation_init(),(3,6)))
    True
    """
    if not (le_choix[0] in [1,2,3,4,5,6,7,8] and le_choix[1] in [1,2,3,4,5,6,7,8]):
        return False
    if plateau[le_choix[0]-1][le_choix[1]-1]!=0:
        return False    
    if valeur_joueur==True:
        pion=2
    else:
        pion=1
    directions=[(-1,0),(1,0),(0,1),(0,-1),(-1,1),(1,-1),(1,1),(-1,-1)]
    for direction in directions:
        liste=[]
        x,y=le_choix[0]-1,le_choix[1]-1
        direction_x=direction[0]
        direction_y=direction[1]
        while y+direction_y>=0 and y+direction_y<len(plateau[0]) and x+direction_x>=0 and x+direction_x<len(plateau) and plateau[x+direction_x][y+direction_y]==3-pion:
            liste.append((x+direction_x,y+direction_y))
            x,y=x+direction_x,y+direction_y
        if len(liste)>0 and liste[-1][1]+direction_y>=0 and liste[-1][1]+direction_y<len(plateau[0]) and liste[-1][0]+direction_x>=0 and liste[-1][0]+direction_x<len(plateau) and plateau[liste[-1][0]+direction_x][liste[-1][1]+direction_y]==pion:
            return True
    return False
           

def action_joueur(valeur_joueur,param_jeu):
    """
    : permet de connaitre le nombre d'allumettes à enlever
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : return : int(choix) choix du joueur
    """
    lechoix=choix_joueur(valeur_joueur,param_jeu)
    return lechoix
         

def etat_final(plateau):
    """
    """
    if test_jeu_rempli(plateau):
        fini=True
    else:
        fini=False
    return fini


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)