def situation_init():
    """
    : création de la situation initiale du jeu
    : renvoie le nombre d'allumettes du tas
    : param : Rien
    : return : nb_allumettes
    Exemple:
    >>> situation_init()
    [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
    """
    return [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

def test_ligne(plateau):
    """
    >>> test_ligne([['-', 'X', '-'], ['X', 'X', 'X'], ['0', '-', '0']])
    True
    >>> test_ligne([['-', 'X', '-'], ['0', 'X', 'X'], ['0', '-', '0']])
    False
    """
    for i in range(3):
            if plateau[i][0]==plateau[i][1] and plateau[i][0]==plateau[i][2] and plateau[i][0] !='-':
                return True
    return False

def test_diagonale1(plateau):
    """
    >>> test_diagonale1([['-', 'X', '-'], ['X', 'X', 'X'], ['0', '-', '0']])
    False
    >>> test_diagonale1([['-', 'X', '0'], ['0', '0', 'X'], ['0', '-', '0']])
    True
    """
    if plateau[0][2]==plateau[1][1] and plateau[1][1]==plateau[2][0] and plateau[0][2]!='-':
        return True
    return False

def test_diagonale2(plateau):
    """
    >>> test_diagonale2([['-', 'X', '-'], ['X', 'X', 'X'], ['0', '-', '0']])
    False
    >>> test_diagonale2([['0', 'X', '0'], ['0', '0', 'X'], ['0', '-', '0']])
    True
    """
    if plateau[0][0]==plateau[1][1] and plateau[1][1]==plateau[2][2] and plateau[2][2]!='-':
        return True
    return False


def test_colonne(plateau):
    """
    >>> test_colonne([['0', 'X', '-'], ['0', 'X', 'X'], ['0', '-', '0']])
    True
    >>> test_colonne([['-', 'X', '-'], ['0', 'X', 'X'], ['0', '-', '0']])
    False
    """
    for i in range(3):
        if plateau[0][i]==plateau[1][i] and plateau[1][i]==plateau[2][i] and plateau[2][i]!='-':
            return True
    return False


def test_jeu_rempli(plateau):
    """
    >>> test_jeu_rempli([['-', 'X', '-'], ['X', 'X', 'X'], ['0', '-', '0']])
    False
    >>> test_jeu_rempli([['0', '0', 'X'], ['0', '0', 'X'], ['0', 'X', '0']])
    True
    """
    for i in range(3):
        for j in range(3):
            if plateau[i][j]=='-':
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
    while not (position[0] in [0,1,2] and position[1] in [0,1,2]):
        question= input('JOUEUR {} : Choisir la position de votre pion par exemple 1,1 : '.format(joueur))
        position= int(question[0]),int(question[2])
    choix=test_validite_choix(valeur_joueur,position,plateau)
    return position

def test_validite_choix(valeur_joueur,le_choix,plateau):
    """
    : test de la validité de la position
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : param le_choix: tuple
    : param plateau : la grille de jeu
    : return : le choix validé ou non du joueur
    """
    correct=False
    if plateau[le_choix[0]][le_choix[1]]=='-':
        correct=True
    else:
        le_choix=choix_joueur(valeur_joueur,plateau)
        return le_choix
    if correct:
        return le_choix
    return None

def action_joueur(valeur_joueur,param_jeu):
    """
    : permet de connaitre le nombre d'allumettes à enlever
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : return : int(choix) choix du joueur
    """
    lechoix=choix_joueur(valeur_joueur,param_jeu)
    return lechoix

def evolution_jeu(valeur_joueur,plateau,choix_joueur):
    """
    : permet de faire évoluer le jeu
    : param : int(param_jeu) nombres d'allumettes
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : return : int(param_jeux) le nombres d'allumettes restantes
    """
    if valeur_joueur==True:
        plateau[choix_joueur[0]][choix_joueur[1]]='X'
    else:
        plateau[choix_joueur[0]][choix_joueur[1]]='0'    
    return plateau

def aff_evolution_jeu(plateau):
    """
    : permet d'afficher le nombre d'allumettes restantes
    : param : int(param_jeu) nombres d'allumettes
    : return : None
    Exemple:
    >>> aff_evolution_jeu([['0', '0', 'X'], ['0', '0', 'X'], ['0', 'X', '0']])
    ['0', '0', 'X']
    ['0', '0', 'X']
    ['0', 'X', '0']
    """
    for i in range(3):
        print(plateau[i])
    return None

def etat_final(plateau):
    """
    >>> etat_final([['-', 'X', '-'], ['X', 'X', 'X'], ['0', '-', '0']])
    (True, False)
    >>> etat_final([['X', 'X', '0'], ['X', '0', 'X'], ['0', 'X', '0']])
    (True, False)
    """
    per_gag=False
    fini=False
    
    #per_gag=True désigne le cas d'égalité
    #fini désigne l'état de la partie qui est finie ou non
    if (test_ligne(plateau)|test_diagonale1(plateau)|test_diagonale2(plateau)|test_colonne(plateau)):
        fini=True
        return fini,per_gag
    else:
        fini=False
        if test_jeu_rempli(plateau):
            per_gag=True
        return fini,per_gag

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)


