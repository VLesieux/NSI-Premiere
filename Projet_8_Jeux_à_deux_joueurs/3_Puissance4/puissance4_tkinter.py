from tkinter import*
import copy

JOUEUR_NOIR=1
JOUEUR_BLANC=2
PROFONDEUR = 3

JOUEUR1 = 1
JOUEUR2 = 2

joueur_courant=JOUEUR_NOIR
fenetre=Tk()
canvas1=Canvas(fenetre,width=400,height=40)
canvas1.grid(row=1, column=0)

choix_colonne=None

class Bouton(object):
    def __init__(self,canvas,x,y,number):
        self.x=x
        self.y=y
        self.number=number
        self.canvas1=canvas1    
    def represente(self):
        self.canvas1.create_rectangle(self.x-20, self.y-20,self.x,self.y)
        self.canvas1.create_text(self.x-10, self.y-10,text=self.number)

boutons=[(i,(40*i+50,40)) for i in range(1,8)]

Boutons=[]

for i in range(len(boutons)):
    Boutons.append(Bouton(canvas1,boutons[i][1][0],boutons[i][1][1],i+1))
    Boutons[i].represente()
    
limites=[(i,(40*i+30,40*i+50)) for i in range(1,8)]


def detec_clic(event):
    global choix_colonne
    global config
    x , y = event.x, event.y
    if y>=20 and y<=40:
        for valeurs in range(len(limites)):
            if x>=limites[valeurs][1][0] and x<=limites[valeurs][1][1]:                
                choix_colonne=limites[valeurs][0]
                print(choix_colonne)
                jouer(choix_colonne)

    
canvas1.bind("<Button-1>", detec_clic)

canvas2=Canvas(fenetre,width=400,height=500,bg="green")
canvas2.grid(row=2, column=0)

class Jeton(object):
    def __init__(self,canvas,x,y,couleur):
        self.x=x
        self.y=y
        self.couleur=couleur
        self.canvas2=canvas2
    def represente(self):
        self.canvas2.create_oval(self.x-15,self.y-15,self.x+15,self.y+15,width=1,fill=self.couleur)


Jetons=[]


def afficher_config(config):
    for ligne in range(6):
        for colonne in range(7):
            if config[ligne][colonne]==0:
                Jetons.append(Jeton(canvas2,40*colonne+80,35*ligne+35,"white"))
            elif config[ligne][colonne]==1:
                Jetons.append(Jeton(canvas2,40*colonne+80,35*ligne+35,"red"))
            else:
                Jetons.append(Jeton(canvas2,40*colonne+80,35*ligne+35,"blue"))                
    for i in range(len(Jetons)):
        Jetons[i].represente() 


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

def test_valide(jeu,colonne,joueur):
    """
    renvoie `True` si le joueur courant peut effectivement jouer sur la colonne
    et `False` dans le cas contraire
    param : jeu : liste
    param : colonne : int
    param : joueur : int
    >>> config1 = [[1, 0, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0], [1, 2, 0, 0, 0, 0, 0]]
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
    """
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

def evaluation(config,joueur):
    '''
    Fonction INTERNE qui prend en paramètre la configuration du
    jeu et le joueur courant. Elle retourne une valeur image
    de la qualité du coup proposé.
    -   paramètres: config (liste) configuration du jeu
                    joueur (int) donne le nom du joueur courant 1 NOIR ou 2 BLANC
    -   return: Val (int) representatif de la qualité du coup proposé
    >>> config2 = [[1, 0, 0, 0, 0, 0, 0], [2, 2, 0, 2, 0, 0, 0], [1, 1, 2, 1, 0, 0, 0], [1, 2, 2, 2, 0, 0, 0], [2, 2, 1, 1, 0, 0, 0], [1, 1, 2, 1, 1, 0, 1]]
    >>> evaluation(config2,JOUEUR_NOIR)
    2000
    '''
    val = 0
#   A REVOIR
#    for ligne in range(2,6):
#        for colonne in range(2,7):
#            if config[ligne-1][colonne-1] == joueur:
#                val += 100
    for colonne in range(1,8):
        if test_valide(config,colonne,joueur) and est_jeu_gagnant(incrementer_config(config,colonne,joueur),joueur):
                val += 1000
        if test_valide(config,colonne,incrementer_joueur(joueur)) and est_jeu_gagnant(incrementer_config(config,colonne,incrementer_joueur(joueur)),incrementer_joueur(joueur)):
                val -= 1000
    return val

def coef_joueur(joueur):
    '''
    fonction INTERNE
    '''
    return 1 if joueur == JOUEUR_NOIR else -1

def creer_liste_coups_possibles(config, joueur):
    '''
    Fonction INTERNE qui prend en paramètre la configuration du jeu et
    le joueur courant. Elle retourne une liste de coups possibles.
    -   paramètres: config (liste) configuration du jeu
                    joueur (int) donne le nom du joueur courant 1 NOIR ou 2 BLANC
    -   return: liste_coups_suivantes (liste) liste de coups possibles.
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
    
def jouer(choix_colonne):
    global config
    global joueur_courant
    if test_valide(config,choix_colonne,JOUEUR_NOIR):            
        config = incrementer_config(config,choix_colonne,JOUEUR_NOIR)
        afficher_config(config)
    if est_jeu_fini(config):
        afficher_fin(config,joueur_courant)
    joueur_courant = incrementer_joueur(joueur_courant)
    liste_coups_possibles = creer_liste_coups_possibles(config, JOUEUR_BLANC)
    meilleur_coup = liste_coups_possibles[0]
    meilleur_eval = -100000
    for coup in liste_coups_possibles:
        conf = copy.deepcopy(config)
        conf = incrementer_config(conf, coup, JOUEUR_BLANC)
        val = min_max(conf, PROFONDEUR, JOUEUR_BLANC)
        if val > meilleur_eval:
            meilleur_eval = val
            meilleur_coup = coup
    config = incrementer_config(config,meilleur_coup,JOUEUR_BLANC)
    afficher_config(config)
    
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
    
    
def min_max(config, profondeur, joueur):
    '''
    Renvoie la valeur de la configuration passée en paramètre
    :param config: configuration du jeu
    :param profondeur: (int) profondeur restante pour l'évaluation de la configuration
    :param joueur: (int) numero du joueur courant    
    '''
    if est_jeu_fini(config) or profondeur == 0:
        return evaluation(config,joueur)*coef_joueur(joueur)
    else:
        if joueur == JOUEUR1:
            liste_configs_suivantes = creer_liste_configs_suivantes(config, JOUEUR1)
            return min([min_max(suivante, profondeur-1, JOUEUR2) for suivante in liste_configs_suivantes])
        else:
            liste_configs_suivantes = creer_liste_configs_suivantes(config, JOUEUR2)
            return max([min_max(suivante, profondeur-1, JOUEUR1) for suivante in liste_configs_suivantes])


config = creer_config_init()
afficher_config(config)

fenetre.mainloop()