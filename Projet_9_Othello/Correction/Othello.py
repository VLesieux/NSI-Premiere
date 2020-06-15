JOUEUR_NOIR=1
JOUEUR_BLANC=2
PROFONDEUR = 3

import random
import main
import copy

def choisir_premier_joueur():
    '''
    retourne le nom du joueur qui débute
    -   paramètres: rien
    -   return: joueur_courant
    >>> choisir_premier_joueur()
    1
    '''
    return JOUEUR_NOIR

def creer_config_init():
    """
    : créer la configuration initiale du jeu
    : param : rien
    : return : list
    Exemple:
    >>> creer_config_init()
    [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 1, 0, 0, 0], [0, 0, 0, 1, 2, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    """
    liste=[[0 for ligne in range(8)] for colonne in range(8)]
    liste[3][3]=2
    liste[3][4]=1
    liste[4][3]=1
    liste[4][4]=2
    return liste

def afficher_config(configuration):
    """
    : affiche la configuration courante du jeu
    : param : list
    : return : str
    Exemple:
    >>> afficher_config(creer_config_init())
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
    for ligne in configuration:
        print(numero,end=' ')
        for element in ligne:
            if element==0:
                print('\u00B7',end=' ')
            if element==1:
                print('■',end=' ')
            if element==2:
                print('□',end=' ')
        numero +=1
        print()

def incrementer_joueur(joueur):
    """
    >>> incrementer_joueur(JOUEUR_NOIR)
    2
    >>> incrementer_joueur(JOUEUR_BLANC)
    1
    """    
    return 3-joueur
    
    
def test_dir_valide(configuration,coordonnees,direction,joueur):
    """
    : teste la validité d'une position sur la grille pouvant provoquer le retournement de pions
    noirs dans une direction donnée
    : param : configuration : list
    : param : coordonnees : tuple
    : param : direction : tuple
    : joueur : int
    : return : bool
    >>> config = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 2, 1, 0, 0, 0], [0, 0, 0, 1, 2, 0, 0, 0], [0, 0, 2, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    >>> afficher_config(config)
      1 2 3 4 5 6 7 8
    1 · · · · · · · · 
    2 · · · · · · · · 
    3 · · · · · · · · 
    4 · · · □ ■ · · · 
    5 · · · ■ □ · · · 
    6 · · □ · · ■ · · 
    7 · · · · · · · · 
    8 · · · · · · · · 
    >>> test_dir_valide(config,(3,4),(1,0),JOUEUR_NOIR)
    True
    >>> test_dir_valide(config,(3,3),(1,1),JOUEUR_BLANC)
    False
    >>> test_dir_valide(config,(3,3),(1,1),JOUEUR_NOIR)
    True
    >>> test_dir_valide(config,(6,3),(-1,1),JOUEUR_BLANC)
    True
    >>> test_dir_valide(config,(6,4),(-1,0),JOUEUR_BLANC)
    True
    >>> test_dir_valide(config,(8,8),(0,1),JOUEUR_BLANC)
    False
    """        
    liste=[]
    x=coordonnees[0]-1
    y=coordonnees[1]-1
    direction_x=direction[0]
    direction_y=direction[1]
    try:
        while configuration[y+direction_y][x+direction_x]==3-joueur:
            liste.append((y+direction_y,x+direction_x))
            x,y=x+direction_x,y+direction_y
        if configuration[liste[-1][0]+direction_y][liste[-1][1]+direction_x]==joueur:
            return True
        return False
    except IndexError:
        return False

def est_coup_possible(configuration,joueur):
    """
    : renvoie si le joueur dispose d'un coup possible
    : param : configuration (list)
    : param : joueur (int)    
    : return : bool
    >>> config = creer_config_init()
    >>> est_coup_possible(config,JOUEUR_NOIR)
    True
    >>> config = [[1 for _ in range(8)] for _ in range(8)]
    >>> est_coup_possible(config,JOUEUR_BLANC)
    False
    """    
    directions=[(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,-1),(1,1),(-1,1)]
    for i in range(1,9):
        for j in range(1,9):
            if configuration[i-1][j-1]==0:
                coordonnees=(j,i)
                for direction in directions:
                    if test_dir_valide(configuration,coordonnees,direction,joueur):
                        return True    
    return False
                    
def est_jeu_fini(configuration):
    """
    : renvoie si le jeu est fini ou non
    : param : configuration : list
    : return : bool
    >>> config = creer_config_init()
    >>> est_jeu_fini(config)
    False
    >>> config = [[1 for _ in range(8)] for _ in range(8)]
    >>> est_jeu_fini(config)
    True
    """  
    if not(est_coup_possible(configuration,JOUEUR_NOIR)) and not(est_coup_possible(configuration,JOUEUR_BLANC)):
        return True
    else:
        return False


def verif_coup_valide(configuration,case,joueur):
    """
    : renvoie True si le coup est valide et False dans le cas contraire
    : param : configuration (list) 
    : return : bool
    >>> s = creer_config_init()
    >>> verif_coup_valide(s,(3,4),JOUEUR_NOIR)
    True
    >>> s = creer_config_init()
    >>> verif_coup_valide(s,(3,4),JOUEUR_BLANC)
    False
    """     
    coordonnees=(case[0],case[1])
    directions=[(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,-1),(1,1),(-1,1)]
    for direction in directions:
        if test_dir_valide(configuration,coordonnees,direction,joueur):
            return True
    return False


def coup_joueur(configuration,joueur,choix):
    """
    : renvoie une variable `coup ` qui contient les coordonnées de la case où le joueur désire placer son pion.
    : param : configuration (list)
    : param : joueur (str) 
    : return : tuple
    
    """  
    if choix=="1":
        poursuite=False
        while poursuite==False:
            nom=""
            if joueur==1:
                nom="JOUEUR_NOIR"
            else:
                nom="JOUEUR_BLANC"
            choix=input("Au "+nom+ " de jouer, donner la case choisie au format x,y : ")
            x=int(choix.split(",")[0])
            y=int(choix.split(",")[1])
            case=(x,y)
            if verif_coup_valide(configuration,case,joueur):
                poursuite=True
                return (x,y)
    elif choix=="2":
        poursuite=False
        if joueur==1:
            while poursuite==False:
                choix=input("A vous de jouer, donner la case choisie au format x,y : ")
                x=int(choix.split(",")[0])
                y=int(choix.split(",")[1])
                case=(x,y)
                if verif_coup_valide(configuration,case,joueur):
                    poursuite=True
            return (x,y)
        elif joueur==2:
# JEU AU SIMPLE HASARD ; CHOIX ALEATOIRE PARMI LES POSSIBLES
#                coups_possibles=[]
#                for i in range(1,9):
#                    for j in range(1,9):
#                        if configuration[j-1][i-1]==0 and verif_coup_valide(configuration,(i,j),joueur):
#                            coups_possibles.append((i,j))
#                if len(coups_possibles)>0:
#                    case=coups_possibles[random.randint(0,len(coups_possibles)-1)]
#                    poursuite=True
#                    return case
#                else:
#                    poursuite=True
#                    return None
            liste_coups_possibles = creer_liste_coups_possibles(configuration, joueur)
            meilleur_coup = liste_coups_possibles[0]
            meilleur_eval = -100000
            for coup in liste_coups_possibles:
                conf = copy.deepcopy(configuration)
                conf = incrementer_config(conf, coup, joueur)
                val = main.min_max(conf, PROFONDEUR, joueur)
                if val > meilleur_eval:
                    meilleur_eval = val
                    meilleur_coup = coup
            return meilleur_coup
        
def incrementer_config(configuration,case,joueur):
    """
    : modifie la configuration du jeu en ajoutant le nouveau pion et en retournant le ou les pions de couleur opposée
    : param : configuration (list)
    : param : joueur (str) 
    : return : liste
    >>> s = creer_config_init()
    >>> afficher_config(s)
      1 2 3 4 5 6 7 8
    1 · · · · · · · · 
    2 · · · · · · · · 
    3 · · · · · · · · 
    4 · · · □ ■ · · · 
    5 · · · ■ □ · · · 
    6 · · · · · · · · 
    7 · · · · · · · · 
    8 · · · · · · · · 
    >>> s1=incrementer_config(s,(3,4),JOUEUR_NOIR)
    >>> afficher_config(s1)
      1 2 3 4 5 6 7 8
    1 · · · · · · · · 
    2 · · · · · · · · 
    3 · · · · · · · · 
    4 · · ■ ■ ■ · · · 
    5 · · · ■ □ · · · 
    6 · · · · · · · · 
    7 · · · · · · · · 
    8 · · · · · · · · 
    >>> afficher_config(incrementer_config(s1,(3,3),JOUEUR_BLANC))
      1 2 3 4 5 6 7 8
    1 · · · · · · · · 
    2 · · · · · · · · 
    3 · · □ · · · · · 
    4 · · ■ □ ■ · · · 
    5 · · · ■ □ · · · 
    6 · · · · · · · · 
    7 · · · · · · · · 
    8 · · · · · · · · 
    >>> afficher_config(incrementer_config(s1,(6,3),JOUEUR_BLANC))
      1 2 3 4 5 6 7 8
    1 · · · · · · · · 
    2 · · · · · · · · 
    3 · · □ · · · · · 
    4 · · ■ □ ■ · · · 
    5 · · · ■ □ · · · 
    6 · · · · · · · · 
    7 · · · · · · · · 
    8 · · · · · · · · 
    """     
    x=case[0]-1
    y=case[1]-1
    directions=[(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,-1),(1,1),(-1,1)]
    for direction in directions:
        direction_x=direction[0]
        direction_y=direction[1]
        liste=[]
        x=case[0]-1
        y=case[1]-1
        try:
            while configuration[y+direction_y][x+direction_x]==3-joueur:
                x,y=x+direction_x,y+direction_y
                liste.append((y,x))
            if configuration[liste[-1][0]+direction_y][liste[-1][1]+direction_x]==joueur:            
                configuration[case[1]-1][case[0]-1]=joueur
                for element in liste:
                    configuration[element[0]][element[1]]=joueur
        except IndexError:
            pass
    return configuration


def creer_liste_coups_possibles(config, joueur):
    '''
    Fonction INTERNE qui prend en paramètre la configuration du jeu et
    le joueur courant. Elle retourne une liste de coups possibles.
    -   paramètres: config (liste) configuration du jeu
                    joueur (int) donne le nom du joueur courant 1 NOIR ou 2 BLANC
    -   return: liste_coups_suivantes (liste) liste de coups possibles.
    >>> s = creer_config_init()
    >>> afficher_config(s)
      1 2 3 4 5 6 7 8
    1 · · · · · · · · 
    2 · · · · · · · · 
    3 · · · · · · · · 
    4 · · · □ ■ · · · 
    5 · · · ■ □ · · · 
    6 · · · · · · · · 
    7 · · · · · · · · 
    8 · · · · · · · · 
    >>> creer_liste_coups_possibles(s, JOUEUR_NOIR)
    [(4, 3), (3, 4), (6, 5), (5, 6)]
    '''
    liste_coups_suivants = []
    directions=[(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,-1),(1,1),(-1,1)]
    for y in range(0,8):
        for x in range(0,8):
            case=(x+1,y+1)
            if config[y][x] == 0 and verif_coup_valide(config,case,joueur):
                liste_coups_suivants.append(case)
    return liste_coups_suivants

def creer_liste_configs_suivantes(config, joueur):
    '''
    Fonction INTERNE qui prend en paramètre la configuration du jeu et
    le joueur courant. Elle retourne des configurations représenttant les coups futur.
    -   paramètres: config (liste) configuration du jeu
                    joueur (int) donne le nom du joueur courant 1 NOIR ou 2 BLANC
    -   return: liste_configs_suivantes (liste) liste de configurations futur
    >>> s = creer_config_init()
    >>> afficher_config(s)
      1 2 3 4 5 6 7 8
    1 · · · · · · · · 
    2 · · · · · · · · 
    3 · · · · · · · · 
    4 · · · □ ■ · · · 
    5 · · · ■ □ · · · 
    6 · · · · · · · · 
    7 · · · · · · · · 
    8 · · · · · · · · 
    '''
    liste_configs_suivantes = []
    liste = creer_liste_coups_possibles(config, joueur)
    if len(liste) != 0: 
        for coup in liste:
            conf = copy.deepcopy(config)
            conf = incrementer_config(conf,coup,joueur)
            liste_configs_suivantes.append(conf)
        return liste_configs_suivantes
    else:
        liste_configs_suivantes.append(copy.deepcopy(config))
        return liste_configs_suivantes


def evaluation(config,joueur):
    '''
    Fonction INTERNE qui prend en paramètre la configuration du
    jeu et le joueur courant. Elle retourne une valeur image
    de la qualité du coup proposé.
    -   paramètres: config (liste) configuration du jeu
                    joueur (int) donne le nom du joueur courant 1 NOIR ou 2 BLANC
    -   return: Val (int) representatif de la qualité du coup proposé
    >>> config = [[1, 1, 2, 1, 0, 0, 0, 0], [0, 0, 2, 0, 0, 0, 0, 0], [0, 0, 2, 2, 0, 0, 0, 0], [0, 0, 0, 2, 1, 0, 0, 0], [0, 0, 0, 1, 2, 0, 0, 0], [0, 0, 2, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
    >>> afficher_config(config)
      1 2 3 4 5 6 7 8
    1 ■ ■ □ ■ · · · · 
    2 · · □ · · · · · 
    3 · · □ □ · · · · 
    4 · · · □ ■ · · · 
    5 · · · ■ □ · · · 
    6 · · □ · · ■ · · 
    7 · · · · · · · · 
    8 · · · · · · · · 
    >>> evaluation(config,JOUEUR_NOIR)
    800
    '''
    val = 0
    for x in range(2,6):
        if config[0][x] == joueur: val += 300
        if config[7][x] == joueur: val += 300
    for y in range(2,6):
        if config[y][0] == joueur: val += 300
        if config[y][7] == joueur: val += 300
    #coin haut gauche
    if config[1][0] == joueur: val += -500
    if config[1][1] == joueur: val += -500
    if config[0][1] == joueur: val += -500
    #coin haut droit
    if config[0][6] == joueur: val += -500
    if config[1][6] == joueur: val += -500
    if config[1][7] == joueur: val += -500
    #coin bas gauche
    if config[6][0] == joueur: val += -500
    if config[6][1] == joueur: val += -500
    if config[7][1] == joueur: val += -500
    #coin bas droit
    if config[7][6] == joueur: val += -500
    if config[6][6] == joueur: val += -500
    if config[6][7] == joueur: val += -500
    #angles
    #extremites
    if config[0][0] == joueur: val += 1000
    if config[0][7] == joueur: val += 1000
    if config[7][0] == joueur: val += 1000
    if config[7][7] == joueur: val += 1000
    
    return val

def coef_joueur(joueur):
    '''
    fonction INTERNE
    '''
    return 1 if joueur == JOUEUR_NOIR else -1



def compte_pions(config, joueur):
    '''
    Fonction INTERNE qui prend en paramètre la configuration du jeu et
    le joueur courant. Elle retourne le nombre de pion du joueur
    -   paramètres: config (liste) configuration du jeu
                    joueur (int) donne le nom du joueur courant 1 NOIR ou 2 BLANC
    -   return: nb_pion (int) nombre du pions du joueur.
    >>> s = creer_config_init()
    >>> compte_pions(s, JOUEUR_NOIR)
    2
    '''
    nb_pion = 0
    for y in range(8):
        for x in range(8):
            if config[y][x] == joueur:
                nb_pion += 1
    return nb_pion     
    
def afficher_fin(config, joueur):
    '''
    Fonction qui prend en paramètre la configuration du jeu et
    le joueur courant et qui affiche les résultats du jeu.
    -   paramètres: config (liste) configuration du jeu
                    joueur (int) donne le nom du joueur courant 1 NOIR ou 2 BLANC
    -   return: rien
    >>> s = creer_config_init()
    >>> afficher_fin(s,JOUEUR_NOIR)
    ====================
      Egalité 
    ====================
    >>> s1=incrementer_config(s,(3,4),JOUEUR_NOIR)
    >>> afficher_fin(s1,JOUEUR_NOIR)
    ====================
    Le gagnant est JOUEUR_NOIR
    ====================
    '''
    print("====================")
    nb_pion_joueur = compte_pions(config, joueur)
    nb_pion_adverse = compte_pions(config, 3-joueur)
    joueurs={1:"JOUEUR_NOIR",2:"JOUEUR_BLANC"}
    if joueur==1:
        nom=joueurs[1]
    else:
        nom=joueurs[2]
    if nb_pion_joueur > nb_pion_adverse:
        print(f"Le gagnant est {nom}")
    elif nb_pion_joueur < nb_pion_adverse:
        print(f"Le gagnant est {joueurs[3-joueur]}")
    else:
        print("  Egalité ")
    print("====================")    
    

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
    