def situation_init():
    """
    : création de la situation initiale du jeu
    : renvoie le plateau initiale
    : param : Rien
    Exemple:
    """
    plateau=[[0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]]
    return plateau



def aff_evolution_jeu(param_jeu):
    """
    : affiche la param_jeu courante du jeu
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
    numero=1
    for ligne in param_jeu:
        for element in ligne:
            if element==0:
                print('\u00B7',end=' ')
            if element==1:
                print('●',end=' ')
            if element==2:
                print('○',end=' ')
        numero +=1
        print()
        
def test_colonne(param_jeu):
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
    >>> test_colonne(config)
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
    >>> test_colonne(config1)
    False
    """
    for pion in range(1,3):
        for colonne in range(7):
            a=0
            for ligne in range(6):
                if param_jeu[ligne][colonne]==pion:
                    a+=1
                    if a==4:
                        return True
                else:
                    a=0
        return False

def test_ligne(param_jeu):
    """
    Renvoie True si alignement selon colonne des jetons de joueur sinon False
    >>> config = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 2, 0, 0], [0, 2, 1, 1, 1, 1, 0]]
    >>> aff_evolution_jeu(config)
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · ○ · · ○ · · 
    · ○ ● ● ● ● · 
    >>> test_ligne(config)
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
    >>> test_ligne(config1)
    False
    """
    for pion in range(1,3):
        for ligne in range(6):
            a=0
            for colonne in range(7):
                if param_jeu[ligne][colonne]==pion:
                    a+=1
                    if a==4:
                        return True
                else:
                    a=0

    return False



def test_diagonale_up(param_jeu):
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
    >>> test_diagonale_up(config)
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
    >>> test_diagonale_up(config1)
    False
    """
    for pion in range(1,3):
        for ligne in range(6):
            for colonne in range(7):
                try:
                    if param_jeu[ligne][colonne]==pion and param_jeu[ligne-1][colonne+1]==pion and param_jeu[ligne-2][colonne+2]==pion and param_jeu[ligne-3][colonne+3]==pion:
                        return True
                except IndexError:
                    pass            
    return False

def test_diagonale_down(param_jeu):
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
    >>> test_diagonale_down(config)
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
    >>> test_diagonale_down(config1)
    False
    """
    for pion in range(1,3):
        for ligne in range(6):
            for colonne in range(7):
                try:
                    if param_jeu[ligne][colonne]==pion and param_jeu[ligne+1][colonne+1]==pion and param_jeu[ligne+2][colonne+2]==pion and param_jeu[ligne+3][colonne+3]==pion:
                        return True
                except IndexError:
                    pass            
    return False

def evolution_jeu(valeur_joueur,param_jeu,choix_joueur):
    """
    : modifie la configuration du jeu en ajoutant le nouveau pion et en retournant le ou les pions de couleur opposée
    : param : configuration (list)
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
    >>> s1=evolution_jeu(False,s,2)
    >>> aff_evolution_jeu(s1)
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · ● · · · · · 
    · ● ○ · · · · 
    >>> aff_evolution_jeu(evolution_jeu(True,s1,3))
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · ● ○ · · · · 
    · ● ○ · · · · 
    >>> aff_evolution_jeu(evolution_jeu(True,s1,2))
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · · · · · · · 
    · ○ · · · · · 
    · ● ○ · · · · 
    · ● ○ · · · · 
    """
    colonne=choix_joueur
    if valeur_joueur==True:
        pion=2
    else:
        pion=1    
    liste=[]
    for ligne in range(6):
        if param_jeu[ligne][colonne-1] !=0:
            param_jeu[ligne-1][colonne-1]=pion
            break
    if param_jeu[5][colonne-1]==0:
        param_jeu[5][colonne-1]=pion
    return param_jeu

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
    if param_jeu[0][lechoix-1]==0:
        return True
    return False

        
def choix_joueur(valeur_joueur,param_jeu):
    """
    : Demande au joueur d'effectuer un choix de position
    : param : bool(valeur_joueur) identification du joueur (True:I;False:II)
    : param : param_jeu : list 
    : return : choix du joueur
    """
    if valeur_joueur:
        joueur='I'
    else:
        joueur='II'

    choix=False
    while choix !=True:
        question= input('JOUEUR {} : Choisir la position de votre pion par exemple 1 : '.format(joueur))
        colonne= int(question)
        choix=test_validite_choix(valeur_joueur,colonne,param_jeu)
        if choix:
            return colonne
        
def test_jeu_rempli(param_jeu):
    """
    Renvoie True si le jeu est rempli sinon False
    """
    for i in range(len(param_jeu)):
        for j in range(len(param_jeu[0])):
            if param_jeu[i][j]==0:
                return False
    return True

def etat_final(param_jeu):
    """
    : vérification si fin jeu
    : param : int(param_jeu)
    : return : bool(fini),bool(per_gag)
    Exemple:
    >>> config = [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 1, 2, 0, 2, 0, 0], [0, 1, 2, 2, 2, 0, 0], [0, 1, 2, 1, 1, 0, 0], [0, 2, 1, 2, 2, 0, 0]]
    >>> aff_evolution_jeu(config)
    1 2 3 4 5 6 7
    · · · · · · · 
    · · · · · · · 
    · ● ○ · ○ · · 
    · ● ○ ○ ○ · · 
    · ● ○ ● ● · · 
    · ○ ● ○ ○ · · 
    """
    per_gag=False
    fini=False
    #per_gag=True désigne le cas d'égalité
    #fini désigne l'état de la partie qui est finie ou non
    if test_jeu_rempli(param_jeu):
        fini=True
        per_gag=True
        
    if test_colonne(param_jeu) or test_ligne(param_jeu) or test_diagonale_up(param_jeu) or test_diagonale_down(param_jeu) :
        fini=True
        per_gag=False

    return fini,per_gag

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

