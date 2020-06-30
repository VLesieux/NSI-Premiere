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
    param_jeu=[[ "-" for colonne in range(3)] for ligne in range(3)]
    return param_jeu


def test_ligne(param_jeu):
    """
    : regarde si il y a un alignement en ligne
    : return : bool
    Exemple:
    >>> test_ligne([['-', 'X', '-'], ['X', 'X', 'X'], ['0', '-', '0']])
    True
    >>> test_ligne([['-', 'X', '-'], ['0', 'X', 'X'], ['0', '-', '0']])
    False
    """
    for i in param_jeu:
        if i[0]==i[1] and i[1]==i[2] and i[0]!='-' and i[1]!='-' and i[2]!='-':
            return True
    return False

def test_diagonale1(param_jeu):
    """
    : regarde si il y a un alignement en diagonale vers le haut
    : return : bool
    Exemple:
    >>> test_diagonale1([['-', 'X', '-'], ['X', 'X', 'X'], ['0', '-', '0']])
    False
    >>> test_diagonale1([['-', 'X', '0'], ['0', '0', 'X'], ['0', '-', '0']])
    True
    """    

    if param_jeu[0][2]==param_jeu[1][1] and param_jeu[1][1]==param_jeu[2][0] and param_jeu[0][2]!='-':
            return True
    return False


def test_colonne(param_jeu):
    """
    : regarde si il y a un alignement en colonne
    : return : bool
    Exemple:
    >>> test_colonne([['0', 'X', '-'], ['0', 'X', 'X'], ['0', '-', '0']])
    True
    >>> test_colonne([['-', 'X', '-'], ['0', 'X', 'X'], ['0', '-', '0']])
    False
    """
    for i in range(len(param_jeu)):
            if param_jeu[0][i]==param_jeu[1][i] and param_jeu[1][i]==param_jeu[2][i] and param_jeu[0][i]!='-':
                return True
    return False


def test_diagonale2(param_jeu):
    """
    : regarde si il y a un alignement en diagonale vers le bas
    : return : bool
    Exemple:
    >>> test_diagonale2([['-', 'X', '-'], ['X', 'X', 'X'], ['0', '-', '0']])
    False
    >>> test_diagonale2([['0', 'X', '0'], ['0', '0', 'X'], ['0', '-', '0']])
    True
    """    

    if param_jeu[0][0]==param_jeu[1][1] and param_jeu[1][1]==param_jeu[2][2] and param_jeu[0][0]!='-':
            return True
    return False

def test_jeu_rempli(param_jeu):
    """
    : regarde si le param_jeu de jeu est rempli
    : return : bool
    Exemple:
    >>> test_jeu_rempli([['-', 'X', '-'], ['X', 'X', 'X'], ['0', '-', '0']])
    False
    >>> test_jeu_rempli([['0', '0', 'X'], ['0', '0', 'X'], ['0', 'X', '0']])
    True
    """
    for i in range(len(param_jeu)):
        for j in range(len(param_jeu)):
            if param_jeu[i][j]=='-':
                return False
    return True

def action_joueur(valeur_joueur,param_jeu):
    """
    : permet de connaitre le nombre d'allumettes à enlevées
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : return : int(choix) choix du joueur

    """
    lechoix=choix_joueur(valeur_joueur,param_jeu)
    return lechoix

def choix_joueur(valeur_joueur,param_jeu):
    """
    : param : int(param_jeu) nombres d'allumettes
    : return : int(choix) choix du joueur
    Remarque: Ne pas faire de doctest sur des fonctions d'entrées /sorties
    """
    if valeur_joueur:
        joueur='I'
    else:
        joueur='II'
        
    emplacement_pion='3,3'

    while (int(emplacement_pion.split(',')[0]) not in [0,1,2]) and (int(emplacement_pion.split(',')[1]) not in [0,1,2]):
        emplacement_pion= input('JOUEUR {} :Choisir la position de votre pion par exemple 1,1 : '.format(joueur))

    choix=test_validite_choix(valeur_joueur,emplacement_pion,param_jeu)
    return choix

def test_validite_choix(valeur_joueur,lechoix,param_jeu):
    """
    : param lechoix: (int) valeur allumettes à supprimer
    : param tas: (int) le nombre d'allumettes presentes
    : return : int(choix) choix du joueuraff_evolution_jeu(9)
    """
    correct=False
    ligne=int(lechoix.split(',')[0])
    colonne=int(lechoix.split(',')[1])
    if param_jeu[ligne][colonne]=='-':
        correct=True
    else:
        lechoix=choix_joueur(valeur_joueur,param_jeu)
        return lechoix

    if correct:
        return lechoix
    return None

def evolution_jeu(valeur_joueur,param_jeu,choix_joueur):
    """
    : permet de faire évoluer le jeu
    : param : int(param_jeu) nombres d'allumettes
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : return : int(param_jeux) le nombres d'allumettes restantes
    Exemple:
    >>> evolution_jeu(True,[['0', '0', 'X'], ['0', '0', 'X'], ['0', 'X', '0']],'1,1')
    [['0', '0', 'X'], ['0', 'X', 'X'], ['0', 'X', '0']]
    """
    ligne=int(choix_joueur.split(',')[0])
    colonne=int(choix_joueur.split(',')[1])
    if valeur_joueur:
        param_jeu[ligne][ colonne]="X"
    else:
        param_jeu[ligne][ colonne]="0"

    return param_jeu

def aff_evolution_jeu(param_jeu):
    """
    : permet d'afficher le plateau de jeu
    : param : list(param_jeu)
    : return : None
    Exemple:
    >>> aff_evolution_jeu([['0', '0', 'X'], ['0', '0', 'X'], ['0', 'X', '0']])
    ['0', '0', 'X']
    ['0', '0', 'X']
    ['0', 'X', '0']
    """
    print(str(param_jeu[0])+'\n'+str(param_jeu[1])+'\n'+str(param_jeu[2]))
    return None

def etat_final(param_jeu):
    """
    : vérification si fin jeu
    : param : int(param_jeu) nombres d'allumettes
    : return : bool(fini)
    Exemple:
    >>> etat_final([['-', 'X', '-'], ['X', 'X', 'X'], ['0', '-', '0']])
    (True, False)
    >>> etat_final([['X', 'X', '0'], ['X', '0', 'X'], ['0', 'X', '0']])
    (True, False)
    """
    per_gag=False
    fini=False
    
    if (test_ligne(param_jeu))|(test_diagonale1(param_jeu))|(test_diagonale2(param_jeu))|(test_colonne(param_jeu)):
        fini=True
        return fini,per_gag

    if (test_jeu_rempli(param_jeu)):
        fini=True
        per_gag=True
        
    return fini,per_gag


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
