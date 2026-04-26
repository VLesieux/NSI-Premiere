
def situation_init():
    """
    : création de la situation initiale du jeu
    : renvoie le plateau initiale
    : param : Rien
    Exemple:
    """
    plateau=[
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]
    ]
    return plateau


def aff_evolution_jeu(param_jeu):
    """
    : affiche la configuration courante du jeu
    : param : list
    : return : str
    Exemple:
    >>> aff_evolution_jeu(situation_init())
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    """
    print("1 2 3 4 5 6 7")
    for ligne in param_jeu:
        for element in ligne:
            if element==0:
                print('\u00B7',end=' ')
            if element==1:
                print('●',end=' ')
            if element==2:
                print('○',end=' ')
        print()

def test_colonne(configuration,joueur):
    """
    Renvoie True si alignement selon colonne des jetons de joueur sinon False
    >>> config = [[0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 2, 0, 0, 2, 0, 0], [0, 2, 0, 0, 2, 0, 0]]
    >>> aff_evolution_jeu(config)
    1 2 3 4 5 6 7
    · ● · · · · · 
    · ● · · · · · 
    · ● · · · · · 
    · ● · · · · · 
    · ○ · · ○ · · 
    · ○ · · ○ · · 
    >>> test_colonne(config,True)
    True
    >>> test_colonne(config,False)
    False
    >>> config1 = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [2, 1, 0, 0, 0, 0, 0]]
    >>> aff_evolution_jeu(config1)
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    ○ ● · · · · · 
    >>> test_colonne(config1,True)
    False
    """
    if joueur==True:
        jeton=1
    else:
        jeton=2
        
    for colonne in range(7):

        for ligne in range(3):

            if all([configuration[ligne+i][colonne] == jeton for i in range(4)]):

                return True

    return False


def test_ligne(configuration,joueur):
    """
    Renvoie True si alignement selon ligne des jetons de joueur sinon False
    >>> config = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 2, 0, 0], [0, 2, 1, 1, 1, 1, 0]]
    >>> aff_evolution_jeu(config)
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · ○ · · ○ · · 
    · ○ ● ● ● ● · 
    >>> test_ligne(config,True)
    True
    >>> config1 = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [2, 1, 0, 0, 0, 0, 0]]
    >>> aff_evolution_jeu(config1)
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    ○ ● · · · · · 
    >>> test_ligne(config1,True)
    False
    """
    if joueur==True:
        jeton=1
    else:
        jeton=2
        
    for ligne in range(6):

        for colonne in range(4):

            if all([configuration[ligne][colonne+i] == jeton for i in range(4)]):

                return True

    return False

# 
def test_diagonale_up(configuration,joueur):
    """
    Renvoie True si alignement selon diagonale montante des jetons de joueur sinon False
    >>> config = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0], [0, 0, 0, 1, 1, 2, 0], [0, 1, 1, 2, 1, 1, 0], [0, 1, 2, 2, 2, 1, 0]]
    >>> aff_evolution_jeu(config)
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · ● ● · 
    · · · ● ● ○ · 
    · ● ● ○ ● ● · 
    · ● ○ ○ ○ ● · 
    >>> test_diagonale_up(config,True)
    True
    >>> config1 = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [2, 1, 0, 0, 0, 0, 0]]
    >>> aff_evolution_jeu(config1,)
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    ○ ● · · · · · 
    >>> test_diagonale_up(config1,False)
    False
    """
    if joueur==True:
        jeton=1
    else:
        jeton=2
        
    for ligne in range(3,6):

        for colonne in range(4):

            if all([configuration[ligne-i][colonne+i] == jeton for i in range(4)]):

                return True

    return False

def test_diagonale_down(configuration,joueur):
    """
    Renvoie True si alignement selon diagonale descendante des jetons de joueur sinon False
    >>> config = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 1, 1, 0], [0, 0, 2, 1, 1, 2, 0], [0, 1, 1, 2, 1, 1, 0], [0, 1, 2, 2, 2, 1, 0]]
    >>> aff_evolution_jeu(config)
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · ● · ● ● · 
    · · ○ ● ● ○ · 
    · ● ● ○ ● ● · 
    · ● ○ ○ ○ ● · 
    >>> test_diagonale_down(config,True)
    True
    >>> config1 = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [2, 1, 0, 0, 0, 0, 0]]
    >>> aff_evolution_jeu(config1)
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    ○ ● · · · · · 
    >>> test_diagonale_down(config1,False)
    False
    """
    if joueur==True:
        jeton=1
    else:
        jeton=2
        
    for ligne in range(3):

        for colonne in range(4):

            if all([configuration[ligne+i][colonne+i] == jeton for i in range(4)]):

                return True

    return False

def evolution_jeu(valeur_joueur,param_jeu,choix_joueur):
    """
    : modifie la configuration du jeu en ajoutant le nouveau pion et en retournant le ou les pions de couleur opposée
    : param : param_jeu (list)
    : param : joueur (str) 
    : return : liste
    >>> s =[[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 0, 0, 0, 0]]
    >>> aff_evolution_jeu(s)
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · ● ○ · · · · 
    >>> s1=evolution_jeu(True,s,2)
    >>> aff_evolution_jeu(s1)
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · ● · · · · · 
    · ● ○ · · · · 
    >>> aff_evolution_jeu(evolution_jeu(False,s1,3))
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · ● ○ · · · · 
    · ● ○ · · · · 
    >>> aff_evolution_jeu(evolution_jeu(False,s1,2))
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · ○ · · · · · 
    · ● ○ · · · · 
    · ● ○ · · · · 
    """
    if valeur_joueur==True:
        jeton=1
    else:
        jeton=2
    
    colonne=choix_joueur-1
    
    for ligne in range(5,-1,-1):
        if param_jeu[ligne][colonne] == 0:
            param_jeu[ligne][colonne]=jeton
            return param_jeu
    return param_jeu


def test_validite_choix(valeur_joueur,lechoix,param_jeu):
    """
    : teste la validité d'une colonne
    : param : valeur_joueur : bool
    : param : lechoix : int
    : param : param_jeu : list
    : return : bool
    >>> config = [[0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]]
    >>> aff_evolution_jeu(config)
    1 2 3 4 5 6 7
    · ● · · · · · 
    · ● · · · · · 
    · ● · · · · · 
    · ● · · · · · 
    · ● · · · · · 
    · ● · · · · · 
    >>> test_validite_choix(False,2,config)
    False
    >>> test_validite_choix(True,1,config)
    True
    """  
    return param_jeu[0][lechoix-1]==0

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
    x=0
    #Les joueurs doivent ramasser tour à tour 2 ou 3 allumettes
    while (x<1 or x>8):
        reponse= input('JOUEUR {} : choisir la colonne : '.format(joueur))
        x=int(reponse)
        if test_validite_choix(valeur_joueur,x,param_jeu):
            return x
    
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
    : param : list(param_jeu)
    : return : bool(per_gag), bool(fini)
      per_gag=True signifie qu'il y a un gagnant
      per_gag=False signifie égalité
      fini=True siginfie que la partie est terminée
    """
    victoire_joueur_1 = (
        test_ligne(param_jeu, True)
        or test_diagonale_up(param_jeu, True)
        or test_diagonale_down(param_jeu, True)
        or test_colonne(param_jeu, True)
    )

    victoire_joueur_2 = (
        test_ligne(param_jeu, False)
        or test_diagonale_up(param_jeu, False)
        or test_diagonale_down(param_jeu, False)
        or test_colonne(param_jeu, False)
    )

    if victoire_joueur_1 or victoire_joueur_2:
        return True, True

    if test_jeu_rempli(param_jeu):
        return False, True

    return False, False


def coups_possibles(param_jeu):
    """
    Renvoie les colonnes jouables.
    Les colonnes vont de 1 à 7.
    """
    coups = []

    for colonne in range(1, 8):
        if param_jeu[0][colonne - 1] == 0:
            coups.append(colonne)

    return coups


def gagnant(param_jeu, valeur_joueur):
    return (
        test_ligne(param_jeu, valeur_joueur)
        or test_colonne(param_jeu, valeur_joueur)
        or test_diagonale_up(param_jeu, valeur_joueur)
        or test_diagonale_down(param_jeu, valeur_joueur)
    )


def evaluation(param_jeu):
    """
    +100 : la machine gagne
    -100 : l'humain gagne
       0 : position neutre
    """
    if gagnant(param_jeu, False):  # joueur II = machine
        return 100

    if gagnant(param_jeu, True):   # joueur I = humain
        return -100

    return 0




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
