JOUEUR_NOIR=1
JOUEUR_BLANC=2
PROFONDEUR = 3

import random
import main
import copy

def choisir_premier_joueur():
    """
    renvoie le nom du joueur qui débute
    param : rien
    return : joueur_courant
    >>> choisir_premier_joueur()
    1
    """
    return JOUEUR_NOIR

def incrementer_joueur(joueur):
    """
    retourne le joueur après avoir switché
    param : int
    return : int
    >>> incrementer_joueur(JOUEUR_NOIR)
    2
    >>> incrementer_joueur(JOUEUR_BLANC)
    1
    """
    return 3-joueur

def creer_config_init():
    """
    : créer la configuration initiale du jeu
    : param : rien
    : return : list
    >>> creer_config_init()
    [[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]]
    """
    return [ [0 for colonne in range(7)]    for ligne in range(6)]

def afficher_config(configuration):
    """
    : Affiche la situation courante du jeu
    : param : list
    : return : strg
    >>> afficher_config(creer_config_init())
      1 2 3 4 5 6 7
      · · · · · · · 
      · · · · · · · 
      · · · · · · · 
      · · · · · · · 
      · · · · · · · 
      · · · · · · · 
    """
    print("  1 2 3 4 5 6 7")
    for ligne in configuration:
        print(' ',end=' ')
        for element in ligne:
            if element==0:
                print('\u00B7',end=' ')
            if element==1:
                print('■',end=' ')
            if element==2:
                print('□',end=' ')
        print()

def test_valide(jeu,colonne,joueur):
    """
    renvoie `True` si le joueur courant peut effectivement jouer sur la colonne
    et `False` dans le cas contraire
    param : jeu : liste
    param : colonne : int
    param : joueur : int
    >>> config1 = [[1, 0, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0]]
    >>> afficher_config(config1)
      1 2 3 4 5 6 7
      ■ · · · · · · 
      ■ □ · · · · · 
      ■ □ · · · · · 
      ■ □ · · · · · 
      ■ □ · · · · · 
      ■ □ · · · · · 
    >>> test_valide(config1,2,JOUEUR_NOIR)
    True
    >>> test_valide(config1,1,JOUEUR_BLANC)
    False
    """
    if colonne in range(1,8):
        if jeu[0][colonne-1]==0:
            return True
    return False

def incrementer_config(jeu,colonne,joueur):
    """
    renvoie la nouvelle configuration
    param : jeu : liste
    param : colonne : int
    param : joueur : int
    >>> config1 = [[0, 0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0]]
    >>> afficher_config(config1)
      1 2 3 4 5 6 7
      · · · · · · · 
      · □ · · · · · 
      · □ · · · · · 
      ■ □ · · · · · 
      ■ □ · · · · · 
      ■ □ · · · · · 
    >>> afficher_config(incrementer_config(config1,2,JOUEUR_BLANC))
      1 2 3 4 5 6 7
      · □ · · · · · 
      · □ · · · · · 
      · □ · · · · · 
      ■ □ · · · · · 
      ■ □ · · · · · 
      ■ □ · · · · · 
    >>> afficher_config(incrementer_config(config1,1,JOUEUR_NOIR))
      1 2 3 4 5 6 7
      · □ · · · · · 
      · □ · · · · · 
      ■ □ · · · · · 
      ■ □ · · · · · 
      ■ □ · · · · · 
      ■ □ · · · · · 
    """
    if test_valide(jeu,colonne,joueur):
        ligne=6
        while not jeu[ligne-1][colonne-1]==0:
            ligne-=1
        jeu[ligne-1][colonne-1]=joueur
        return jeu
    else:
        pass


def est_jeu_fini(configuration):
    """
    : renvoie si le jeu est fini suite au coup gagnant ou au plateau rempli
    : param : configuration (list)
    : param : joueur (int)    
    : return : bool
    >>> config2 = [[1, 0, 0, 0, 0, 0, 0], [2, 2, 0, 0, 0, 0, 0], [1, 1, 2, 1, 0, 0, 0], [1, 2, 2, 2, 0, 0, 0], [2, 2, 1, 1, 0, 0, 0], [1, 1, 2, 1, 1, 0, 1]]
    >>> afficher_config(config2)
      1 2 3 4 5 6 7
      ■ · · · · · · 
      □ □ · · · · · 
      ■ ■ □ ■ · · · 
      ■ □ □ □ · · · 
      □ □ ■ ■ · · · 
      ■ ■ □ ■ ■ · ■ 
    >>> est_jeu_fini(config2)
    False
    >>> config3 = [ [1 for colonne in range(7)]    for ligne in range(6)]
    >>> est_jeu_fini(config3)
    True
    >>> est_jeu_fini(creer_config_init())
    False
    """ 
    if est_jeu_gagnant(configuration,JOUEUR_NOIR) or est_jeu_gagnant(configuration,JOUEUR_BLANC):
        return True
    try:
        for ligne in range(6):
            for colonne in range(7):
                if configuration[ligne-1][colonne-1]==0 :
                    return False               
    except IndexError:
        pass               
    return True
    
    
def est_jeu_gagnant(configuration,joueur):
    """
    : renvoie si coup du joueur est gagnant
    : param : configuration (list)
    : param : joueur (int)    
    : return : bool
    >>> config2 = [[1, 0, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0], [1, 1, 2, 1, 0, 0, 0], [1, 2, 1, 2, 0, 0, 0], [2, 2, 1, 1, 0, 0, 0], [1, 1, 2, 1, 1, 0, 1]]
    >>> afficher_config(config2)
      1 2 3 4 5 6 7
      ■ · · · · · · 
      ■ □ · · · · · 
      ■ ■ □ ■ · · · 
      ■ □ ■ □ · · · 
      □ □ ■ ■ · · · 
      ■ ■ □ ■ ■ · ■ 
    >>> est_jeu_gagnant(config2,JOUEUR_NOIR)
    True
    >>> config3 = [[0, 0, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0], [1, 1, 2, 1, 0, 0, 0], [1, 2, 1, 2, 0, 0, 0], [2, 2, 1, 1, 0, 0, 0], [1, 1, 2, 1, 1, 1, 1]]
    >>> afficher_config(config3)
      1 2 3 4 5 6 7
      · · · · · · · 
      ■ □ · · · · · 
      ■ ■ □ ■ · · · 
      ■ □ ■ □ · · · 
      □ □ ■ ■ · · · 
      ■ ■ □ ■ ■ ■ ■ 
    >>> est_jeu_gagnant(config3,JOUEUR_NOIR)
    True
    >>> config4 = [[2, 0, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0], [1, 1, 2, 1, 0, 0, 0], [1, 2, 1, 2, 0, 0, 0], [2, 2, 1, 1, 0, 0, 0], [1, 1, 2, 1, 1, 0, 1]]
    >>> afficher_config(config4)
      1 2 3 4 5 6 7
      □ · · · · · · 
      ■ □ · · · · · 
      ■ ■ □ ■ · · · 
      ■ □ ■ □ · · · 
      □ □ ■ ■ · · · 
      ■ ■ □ ■ ■ · ■ 
    >>> est_jeu_gagnant(config4,JOUEUR_BLANC)
    True
    >>> config5 = [[2, 0, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0], [1, 1, 2, 1, 0, 0, 0], [1, 2, 1, 2, 0, 0, 0], [2, 1, 1, 1, 0, 0, 0], [1, 1, 2, 1, 1, 0, 1]]
    >>> afficher_config(config5)
      1 2 3 4 5 6 7
      □ · · · · · · 
      ■ □ · · · · · 
      ■ ■ □ ■ · · · 
      ■ □ ■ □ · · · 
      □ ■ ■ ■ · · · 
      ■ ■ □ ■ ■ · ■ 
    >>> est_jeu_gagnant(config5,JOUEUR_NOIR)
    True
        >>> config6 = [[2, 0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 0, 0], [1, 1, 2, 1, 0, 0, 0], [1, 2, 2, 2, 0, 0, 0], [2, 1, 1, 1, 0, 0, 0], [1, 1, 2, 1, 1, 0, 1]]
    >>> afficher_config(config6)
      1 2 3 4 5 6 7
      □ · · · · · · 
      ■ · · · · · · 
      ■ ■ □ ■ · · · 
      ■ □ □ □ · · · 
      □ ■ ■ ■ · · · 
      ■ ■ □ ■ ■ · ■ 
    >>> est_jeu_gagnant(config6,JOUEUR_NOIR)
    False
    >>> est_jeu_gagnant(creer_config_init(),JOUEUR_NOIR)
    False
    >>> config3 = [[1, 0, 0, 0, 0, 0, 0], [2, 2, 0, 2, 0, 0, 0], [1, 1, 2, 1, 0, 0, 0], [1, 2, 2, 2, 0, 0, 0], [2, 2, 1, 1, 0, 0, 0], [1, 1, 2, 1, 1, 1, 0]]
    >>> afficher_config(config3)
      1 2 3 4 5 6 7
      ■ · · · · · · 
      □ □ · □ · · · 
      ■ ■ □ ■ · · · 
      ■ □ □ □ · · · 
      □ □ ■ ■ · · · 
      ■ ■ □ ■ ■ ■ · 
    >>> est_jeu_gagnant(incrementer_config(config3,7,JOUEUR_NOIR),JOUEUR_NOIR)
    True
    >>> est_jeu_gagnant(incrementer_config(config3,5,JOUEUR_BLANC),JOUEUR_BLANC)
    True
    """ 
    #test vertical
    try:
        for ligne in range(6):
            for colonne in range(7):
                #test vertical
                if configuration[ligne-1][colonne-1]==joueur and configuration[ligne-1][colonne-1]==configuration[ligne-2][colonne-1] and configuration[ligne-1][colonne-1]==configuration[ligne-3][colonne-1] and configuration[ligne-1][colonne-1]==configuration[ligne-4][colonne-1]:
                    return True
                #test horizontal
                if configuration[ligne-1][colonne-1]==joueur and configuration[ligne-1][colonne-1]==configuration[ligne-1][colonne-2] and configuration[ligne-1][colonne-1]==configuration[ligne-1][colonne-3] and configuration[ligne-1][colonne-1]==configuration[ligne-1][colonne-4]:
                    return True
                #test diagonal droit
                if configuration[ligne-1][colonne-1]==joueur and configuration[ligne-1][colonne-1]==configuration[ligne-2][colonne-2] and configuration[ligne-1][colonne-1]==configuration[ligne-3][colonne-3] and configuration[ligne-1][colonne-1]==configuration[ligne-4][colonne-4]:
                    return True
                #test diagonal gauche
                if configuration[ligne-1][colonne-1]==joueur and configuration[ligne-1][colonne-1]==configuration[ligne-2][colonne] and configuration[ligne-1][colonne-1]==configuration[ligne-3][colonne+2] and configuration[ligne-1][colonne-1]==configuration[ligne-4][colonne+3]:
                    return True                 
    except IndexError:
        pass               
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
            choix_colonne=int(input("Au "+nom+ " de jouer, donner la colonne choisie : "))
            if test_valide(configuration,choix_colonne,joueur):
                poursuite=True
                return choix_colonne
    elif choix=="2":
        poursuite=False
        if joueur==1:
            while poursuite==False:
                choix_colonne=int(input("A vous de jouer, donnez la colonne choisie : "))
                if test_valide(configuration,choix_colonne,joueur):
                    poursuite=True
            return choix_colonne
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
        

def afficher_fin(configuration, joueur):
    '''
    Fonction qui prend en paramètre la configuration du jeu et
    le joueur courant et qui affiche les résultats du jeu.
    -   paramètres: config (liste) configuration du jeu
                    joueur (int) donne le nom du joueur courant 1 NOIR ou 2 BLANC
    -   return: rien
    '''
    print("====================")
    joueur = incrementer_joueur(joueur)
    joueurs={1:"JOUEUR_NOIR",2:"JOUEUR_BLANC"}
    if joueur==1:
        nom=joueurs[1]
    else:
        nom=joueurs[2]
    if est_jeu_gagnant(configuration,joueur):
        print(f"Le gagnant est {nom}")
    else:
        print("  Egalité ")
    print("====================")    
    


def creer_liste_coups_possibles(config, joueur):
    '''
    Fonction INTERNE qui prend en paramètre la configuration du jeu et
    le joueur courant. Elle retourne une liste de coups possibles.
    -   paramètres: config (liste) configuration du jeu
                    joueur (int) donne le nom du joueur courant 1 NOIR ou 2 BLANC
    -   return: liste_coups_suivantes (liste) liste de coups possibles.
        >>> config5 = [[2, 0, 1, 0, 0, 0, 0], [1, 2, 1, 0, 0, 0, 0], [1, 1, 2, 1, 0, 0, 0], [1, 2, 1, 2, 0, 0, 0], [2, 1, 1, 1, 0, 0, 0], [1, 1, 2, 1, 1, 0, 1]]
    >>> afficher_config(config5)
      1 2 3 4 5 6 7
      □ · ■ · · · · 
      ■ □ ■ · · · · 
      ■ ■ □ ■ · · · 
      ■ □ ■ □ · · · 
      □ ■ ■ ■ · · · 
      ■ ■ □ ■ ■ · ■ 
    >>> creer_liste_coups_possibles(config5, JOUEUR_NOIR)
    [2, 4, 5, 6, 7]
    '''    
    liste_coups_suivants = []
    for i in range(1,8):
        if test_valide(config,i,joueur):
            liste_coups_suivants.append(i)
    return liste_coups_suivants

def creer_liste_configs_suivantes(config, joueur):
    '''
    Fonction INTERNE qui prend en paramètre la configuration du jeu et
    le joueur courant. Elle retourne des configurations représentant les coups futurs.
    -   paramètres: config (liste) configuration du jeu
                    joueur (int) donne le nom du joueur courant 1 NOIR ou 2 BLANC
    -   return: liste_configs_suivantes (liste) liste de configurations futur
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
    >>> config2 = [[1, 0, 0, 0, 0, 0, 0], [2, 2, 0, 2, 0, 0, 0], [1, 1, 2, 1, 0, 0, 0], [1, 2, 2, 2, 0, 0, 0], [2, 2, 1, 1, 0, 0, 0], [1, 1, 2, 1, 1, 0, 1]]
    >>> afficher_config(config2)
      1 2 3 4 5 6 7
      ■ · · · · · · 
      □ □ · □ · · · 
      ■ ■ □ ■ · · · 
      ■ □ □ □ · · · 
      □ □ ■ ■ · · · 
      ■ ■ □ ■ ■ · ■ 
    >>> evaluation(config2,JOUEUR_NOIR)
    -4600
    '''
    val = 0
    for ligne in range(2,6):
        for colonne in range(2,7):
            if config[ligne-1][colonne-1] == joueur:
                val += 100
    for colonne in range(1,8):
        if test_valide(config,colonne,joueur) and est_jeu_gagnant(incrementer_config(config,colonne,joueur),joueur):
                val -= 1000
    return val

def coef_joueur(joueur):
    '''
    fonction INTERNE
    '''
    return 1 if joueur == JOUEUR_NOIR else -1





if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)