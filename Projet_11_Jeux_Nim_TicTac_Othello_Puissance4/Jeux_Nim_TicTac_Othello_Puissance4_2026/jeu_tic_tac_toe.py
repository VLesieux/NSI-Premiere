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
    return [['-' for i in range(3)] for j in range(3)]


def test_ligne(param_jeu):
    """
    >>> test_ligne([['-', 'X', '-'], ['X', 'X', 'X'], ['0', '-', '0']])
    True
    >>> test_ligne([['-', 'X', '-'], ['0', 'X', 'X'], ['0', '-', '0']])
    False
    """
    for i in range(3):
        if param_jeu[i][0]==param_jeu[i][1] and param_jeu[i][1]==param_jeu[i][2] and param_jeu[i][1] != '-':
            return True
    return False

def test_diagonale1(param_jeu):
    """
    >>> test_diagonale1([['-', 'X', '-'], ['X', 'X', 'X'], ['0', '-', '0']])
    False
    >>> test_diagonale1([['-', 'X', '0'], ['0', '0', 'X'], ['0', '-', '0']])
    True
    """
    if param_jeu[0][2]==param_jeu[1][1] and param_jeu[1][1]==param_jeu[2][0] and param_jeu[1][1] != '-':
            return True
    return False


def test_colonne(param_jeu):
    """
    >>> test_colonne([['0', 'X', '-'], ['0', 'X', 'X'], ['0', '-', '0']])
    True
    >>> test_colonne([['-', 'X', '-'], ['0', 'X', 'X'], ['0', '-', '0']])
    False
    """
    for i in range(3):
        if param_jeu[0][i]==param_jeu[1][i] and param_jeu[1][i]==param_jeu[2][i] and param_jeu[1][i] != '-':
            return True
    return False

def test_diagonale2(param_jeu):
    """
    >>> test_diagonale2([['-', 'X', '-'], ['X', 'X', 'X'], ['0', '-', '0']])
    False
    >>> test_diagonale2([['0', 'X', '0'], ['0', '0', 'X'], ['0', '-', '0']])
    True
    """
    if param_jeu[0][0]==param_jeu[1][1] and param_jeu[1][1]==param_jeu[2][2] and param_jeu[1][1] != '-':
            return True
    return False

def test_jeu_rempli(param_jeu):
    """
    >>> test_jeu_rempli([['-', 'X', '-'], ['X', 'X', 'X'], ['0', '-', '0']])
    False
    >>> test_jeu_rempli([['0', '0', 'X'], ['0', '0', 'X'], ['0', 'X', '0']])
    True
    """
    for ligne in range(len(param_jeu)):
        for colonne in range(len(param_jeu[0])):
            if param_jeu[ligne][colonne]=='-':
                return False
    return True
    

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
    x,y=-1,-1
    #Les joueurs doivent ramasser tour à tour 2 ou 3 allumettes
    while (x<0 or x>2 or y<0 or y>2):
        reponse= input('JOUEUR {} : choisir la position de votre pion par exemple 1,1 : '.format(joueur))
        x=int(reponse[0])
        y=int(reponse[2])
    choix=test_validite_choix(valeur_joueur,(x,y),param_jeu)
    return choix

def test_validite_choix(valeur_joueur,lechoix,param_jeu):
    """
    : test de la validité du choix 2 ou 3 allumettes
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : param lechoix: (int) valeur allumettes à supprimer
    : param tas: (int) le nombre d'allumettes presentes
    : return : int(choix) le choix validé ou non du joueur
    """
    correct=False
    if param_jeu[lechoix[0]][lechoix[1]]=='-':
        correct=True
    else:
        lechoix=choix_joueur(valeur_joueur,param_jeu)
        return lechoix
    if correct:
        return lechoix
    return None
# 
def action_joueur(valeur_joueur,param_jeu):
    """
    : permet de connaitre le nombre d'allumettes à enlever
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : return : int(choix) choix du joueur
    """
    lechoix=choix_joueur(valeur_joueur,param_jeu)
    return lechoix
# 
def evolution_jeu(valeur_joueur,param_jeu,choix_joueur):
    """
    : permet de faire évoluer le jeu
    : param : int(param_jeu) nombres d'allumettes
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : return : int(param_jeux) le nombres d'allumettes restantes
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
    : permet d'afficher la situation actuelle du jeu
    : return : None
    >>> aff_evolution_jeu([['0', '0', 'X'], ['0', '0', 'X'], ['0', 'X', '0']])
    [  0    0    X  ]
    [  0    0    X  ]
    [  0    X    0  ]
    """
    for ligne in param_jeu:
        print ("[",end="")
        for element in ligne:
            print(' ',element,' ', end="")
        print ("]",end="")
        print()
            

def etat_final(param_jeu):
    """
    : vérification si fin jeu
    : param : int(param_jeu) nombres d'allumettes
    : return : bool(fini),bool(per_gag)
    Exemple:
    >>> etat_final([['-', 'X', '-'], ['X', 'X', 'X'], ['0', '-', '0']])
    (True, True)
    >>> etat_final([['X', 'X', '0'], ['0', '0', 'X'], ['X', '0', 'X']])
    (False, True)
    """
    per_gag,fini=False,False
    if test_ligne(param_jeu) or test_diagonale1(param_jeu) or test_colonne(param_jeu) or test_diagonale2(param_jeu):
        per_gag,fini=True,True
    if test_jeu_rempli(param_jeu):
        fini=True
    return per_gag,fini


def coups_possibles(param_jeu):
    """
    Renvoie la liste des cases encore libres.

    Une case libre contient '-'.

    Exemple :
    >>> coups_possibles([['X', '-', '-'], ['-', '0', '-'], ['-', '-', 'X']])
    [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)]
    """
    liste_coups = []

    for ligne in range(3):
        for colonne in range(3):
            if param_jeu[ligne][colonne] == '-':
                liste_coups.append((ligne, colonne))

    return liste_coups

def evaluation(param_jeu):
    """
    Donne une note à une position finale.
    +1 : la machine gagne
    -1 : l'humain gagne
     0 : égalité
    """
    if jeu.test_ligne(param_jeu) or jeu.test_colonne(param_jeu) or jeu.test_diagonale1(param_jeu) or jeu.test_diagonale2(param_jeu):
        # Si quelqu'un a gagné, on regarde qui a trois pions alignés
        lignes_gagnantes = [
            [(0,0), (0,1), (0,2)],
            [(1,0), (1,1), (1,2)],
            [(2,0), (2,1), (2,2)],
            [(0,0), (1,0), (2,0)],
            [(0,1), (1,1), (2,1)],
            [(0,2), (1,2), (2,2)],
            [(0,0), (1,1), (2,2)],
            [(0,2), (1,1), (2,0)]
        ]

        for ligne in lignes_gagnantes:
            a, b, c = ligne
            symbole = param_jeu[a[0]][a[1]]
            if symbole != '-' and symbole == param_jeu[b[0]][b[1]] and symbole == param_jeu[c[0]][c[1]]:
                if symbole == '0':
                    return 1
                else:
                    return -1

    return 0

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)