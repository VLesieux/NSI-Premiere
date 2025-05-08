def situation_init():
    """
    : création de la situation initiale du jeu
    : renvoie tableau vide
    : param : Rien
    : return : tableau
    Exemple:
    >>> situation_init()
    [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    """
    param_jeu=[['-' for i in range(3)] for j in range(3)]
    return param_jeu

def test_ligne(param_jeu):
    """
    Renvoie True si alignement selon ligne, False sinon
    param : param_jeu : list
    return : bool
    >>> test_ligne([['-', 'X', '-'], ['X', 'X', 'X'], ['0', '-', '0']])
    True
    >>> test_ligne([['-', 'X', '-'], ['0', 'X', 'X'], ['0', '-', '0']])
    False
    """
    for i in range(3):
        if param_jeu[i][0]==param_jeu[i][1] and param_jeu[i][0]==param_jeu[i][2] and param_jeu[i][0] !='-':
            return True
    return False

def test_colonne(param_jeu):
    """
    Renvoie True si alignement selon diagonale1, False sinon
    param : param_jeu : list
    return : bool
    >>> test_colonne([['0', 'X', '-'], ['0', 'X', 'X'], ['0', '-', '0']])
    True
    >>> test_colonne([['-', 'X', '-'], ['0', 'X', 'X'], ['0', '-', '0']])
    False
    """
    for i in range(3):
        if param_jeu[0][i]==param_jeu[1][i] and param_jeu[0][i]==param_jeu[2][i] and param_jeu[0][i] !='-':
            return True
    return False

def test_diagonale1(param_jeu):
    """
    Renvoie True si alignement selon diagonale2, False sinon
    param : param_jeu : list
    return : bool
    >>> test_diagonale1([['-', 'X', '-'], ['X', 'X', 'X'], ['0', '-', '0']])
    False
    >>> test_diagonale1([['-', 'X', '0'], ['0', '0', 'X'], ['0', '-', '0']])
    True
    """
    if param_jeu[2][0]==param_jeu[1][1] and param_jeu[1][1]==param_jeu[0][2] and param_jeu[1][1] !='-':
            return True
    return False

def test_diagonale2(param_jeu):
    """
    Renvoie True si alignement selon diagonale2, False sinon
    param : param_jeu : list
    return : bool
    >>> test_diagonale2([['-', 'X', '-'], ['X', 'X', 'X'], ['0', '-', '0']])
    False
    >>> test_diagonale2([['0', 'X', '0'], ['0', '0', 'X'], ['0', '-', '0']])
    True
    """
    if param_jeu[0][0]==param_jeu[1][1] and param_jeu[1][1]==param_jeu[2][2] and param_jeu[1][1] !='-':
            return True
    return False

def test_jeu_rempli(param_jeu):
    """
    Renvoie True si le jeu est rempli sinon False
    >>> test_jeu_rempli([['-', 'X', '-'], ['X', 'X', 'X'], ['0', '-', '0']])
    False
    >>> test_jeu_rempli([['0', '0', 'X'], ['0', '0', 'X'], ['0', 'X', '0']])
    True
    """
    for i in range(3):
        for j in range(3):
            if param_jeu[i][j]=='-':
                return False
    return True

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
    #init choix jeu
    lechoix=(5,5)

    while not test_validite_choix(valeur_joueur,lechoix,param_jeu):
        entree= input('JOUEUR {} : votre case sous la forme 1,1 : '.format(joueur))
        lechoix=(int(entree[0]),int(entree[2]))
        lechoix=test_validite_choix(valeur_joueur,lechoix,param_jeu)
        
    return lechoix

def test_validite_choix(valeur_joueur,lechoix,param_jeu):
    """
    : test de la validité du choix de la case
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : param lechoix: (tuple) la case choisie
    : param param_jeu: (list) la param_jeu de jeu
    : return : la case choisie par le joueur    
    >>> test_validite_choix(True,(1,1),[['-', 'X', '-'], ['X', 'X', 'X'], ['0', '-', '0']])
    False
    >>> test_validite_choix(True,(1,1),[['-', 'X', '-'], ['X', '-', 'X'], ['0', '-', '0']])
    (1, 1)
    """
    if lechoix != False:
        if lechoix[0] >2 or lechoix[1] >2:
            return False
    if param_jeu[lechoix[0]][lechoix[1]] =='-':
        return lechoix
    else:
        return False


def action_joueur(valeur_joueur,param_jeu):
    """
    : permet de connaitre le nombre d'allumettes à enlever
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : return : int(choix) choix du joueur
    """
    lechoix=choix_joueur(valeur_joueur,param_jeu)
    return lechoix

def evolution_jeu(valeur_joueur,param_jeu,choix_joueur):
    """
    : permet de faire évoluer le jeu
    : param : int(param_jeu) nombres d'allumettes
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : return : int(param_jeux) le nombres d'allumettes restantes
    Exemple:
    >>> evolution_jeu(True,[['0', '0', 'X'], ['0', '0', 'X'], ['0', 'X', '0']],(1,1))
    [['0', '0', 'X'], ['0', 'X', 'X'], ['0', 'X', '0']]
    """
    if valeur_joueur==True:
        param_jeu[choix_joueur[0]][choix_joueur[1]]='X'
    else:
        param_jeu[choix_joueur[0]][choix_joueur[1]]='0'
    return param_jeu

def aff_evolution_jeu(param_jeu):
    """
    : permet d'afficher le nombre d'allumettes restantes
    : param : int(param_jeu) nombres d'allumettes
    : return : None
    Exemple:
    >>> aff_evolution_jeu([['0', '0', 'X'], ['0', '0', 'X'], ['0', 'X', '0']])
    [ 0 , 0 , X ]
    [ 0 , 0 , X ]
    [ 0 , X , 0 ]
    """
    affichage=""
    for i in range(len(param_jeu)):
        affichage+="[ "
        for j in range(len(param_jeu[0])):
            affichage+=param_jeu[i][j]+" , "
        affichage=affichage[:-2]
        affichage+="]"+"\n"
    affichage=affichage[0:-1]
    print(affichage)
        
def etat_final(param_jeu):
    """
    : vérification si fin jeu
    : param : int(param_jeu)
    : return : bool(fini),bool(per_gag)
    Exemple:
    >>> aff_evolution_jeu([['0', '0', 'X'], ['0', '0', 'X'], ['0', 'X', '0']])
    [ 0 , 0 , X ]
    [ 0 , 0 , X ]
    [ 0 , X , 0 ]
    >>> etat_final([['-', 'X', '-'], ['X', 'X', 'X'], ['0', '-', '0']])
    (True, False)
    >>> etat_final([['X', 'X', '0'], ['X', '0', 'X'], ['0', 'X', '0']])
    (True, False)
    """
    per_gag=False
    fini=False
    #per_gag=True désigne le cas d'égalité
    #fini désigne l'état de la partie qui est finie ou non
    if test_jeu_rempli(param_jeu):
        fini=True
        per_gag=True
        
    if test_ligne(param_jeu) or test_diagonale1(param_jeu) or test_diagonale2(param_jeu) or test_colonne(param_jeu) :
        fini=True
        per_gag=False

    return fini,per_gag    

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

