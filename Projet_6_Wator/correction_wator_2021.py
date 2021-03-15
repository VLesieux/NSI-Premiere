from random import randrange
import time
import pylab
H=25
V=25
G_THON=2
G_REQUIN=5
E_THON=0
E_REQUIN=3
P_THON=0.3
P_REQUIN=0.1

def creer_grille_methode1(nb_lignes,nb_colonnes):
    """
    création d'une grille avec une double boucle
    param : nb_lignes : int
    param : nb_colonnes : int
    return : list
    >>> creer_grille_methode1(2,3)
    [[(0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0)]]
    """
    grille=[]    
    for i in range(nb_lignes):
        ligne=[]
        for j in range(nb_colonnes):
            ligne.append((0,0,0))
        grille.append(ligne)
    return grille


def creer_grille(nb_lignes,nb_colonnes):
    """
    création d'une grille avec une double boucle
    param : nb_lignes : int
    param : nb_colonnes : int
    return : list
    >>> creer_grille(2,3)
    [[(0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0)]]
    """
    grille=[[(0, 0, 0) for j in range(nb_colonnes)] for i in range(nb_lignes)]    
    return grille


def selection_case(nb_cases_h,nb_cases_v):
    """
    sélection de case au hasard
    param : nb_cases_h: int
    param : nb_cases_v : int
    return : tuple    
    """
    return (randrange(nb_cases_h),randrange(nb_cases_v))


def init_case(nature):
    """
    retourne le tuple correspondant aux valeurs initiales des paramètres de gestation G et d'énergie E correspondant à la nature de cet élément
    param : nature : int
    return : (0, 0, 0) si nature=0 ; (1, 2, 0) si nature=1 ; (2, 5, 3) si nature=2
    >>> init_case(0)
    (0, 0, 0)
    >>> init_case(1)
    (1, 2, 0)
    >>> init_case(2)
    (2, 5, 3)
    """
    if nature==0:
        valeurs_initiales=(0, 0, 0)
    elif nature==1:
        valeurs_initiales=(1, 2, 0)
    else:
        valeurs_initiales=(2, 5, 3)
    return valeurs_initiales


def placement_espece(grille,nature,nb_poissons):
    """
    renvoie une grille comportant nb_poissons de nature placés de façon aléatoire
    param : grille : list
    param : nature : int
    param : nb_poissons
    """
    while nb_poissons>0:
        case=selection_case(len(grille[0]),len(grille))
        x=case[0]
        y=case[1]
        if grille[y][x][0]==0:
            grille[y][x]=init_case(nature)
            nb_poissons-=1
    return grille
            
def denombre_espece(grille,nature):
    """
    renvoie le nombre de poissons de nature dans la grille
    param : grille : list
    param : nature : int
    return : int
    >>> denombre_espece(placement_espece(creer_grille(3,2),2,4),2)
    4    
    """
    nombre=0
    for colonne in range(len(grille[0])):
        for ligne in range(len(grille)):
            if grille[ligne][colonne][0]==nature:
                nombre+=1
    return nombre

def init_grille(p_thons,p_requins,nb_lignes,nb_colonnes):
    """
    renvoie une grille aléatoire comportant le pourcentage de thons et de requins
    param : p_thons : float
    param : p_requins : float
    param : nb_lignes : int
    param : nb_colonnes : int
    return : list
    >>> denombre_espece(init_grille(0.5,0.5,2,2), 1)
    2
    >>> denombre_espece(init_grille(0.5,0.5,2,2), 2)
    2   
    """
    grille=creer_grille(nb_lignes,nb_colonnes)
    placement_espece(grille,1,p_thons*nb_lignes*nb_colonnes)
    placement_espece(grille,2,p_requins*nb_lignes*nb_colonnes)
    return grille
    
def afficher_grille(grille):
    """
    affiche la grille
    param : list   
    """
    
    for ligne in range(len(grille)):
        chaine=""
        for colonne in range(len(grille[0])):
            if grille[ligne][colonne][0]==0:
                chaine+=" _ "
            elif grille[ligne][colonne][0]==1:
                chaine+=" T "
            else:
                chaine+=" R "
        print(chaine)
        print()
    print("################################################################")
    
    
def cases_voisines(case, nb_lignes, nb_colonnes):
    """
    renvoie les cases voisines de case sur la mer torique
    param : case : tuple
    param : nb_colonnes : int
    param : nb_lignes : int
    >>> cases_voisines((1,1),2,2)
    [(1, 0), (0, 1), (0, 1), (1, 0)]
    >>> cases_voisines((1,1),3,3)
    [(1, 0), (0, 1), (2, 1), (1, 2)]
    >>> cases_voisines((2,0),3,3)
    [(2, 2), (1, 0), (0, 0), (2, 1)]
    """
    x=case[0]
    y=case[1]
    if x==0:
        ouest=(nb_colonnes-1,y)
    else:
        ouest=(x-1,y)
        
    if x==nb_colonnes-1:
        est=(0,y)
    else:
        est=(x+1,y)
        
    if y==0:
        nord=(x,nb_lignes-1)
    else:
        nord=(x,y-1)
    
    if y==nb_lignes-1:
        sud=(x,0)
    else:
        sud=(x,y+1)
    
    return [nord,ouest,est,sud]
    
    
def recherche_case(liste_4_cases,grille,nature):
    """
    retourne les coordonnées d'une case tirée au sort parmi celles répondant aux critères, sinon False
    param : liste_4_cases : list
    param : grille : list
    param : nature : int
    """
    cases_possibles=[]
    for case in liste_4_cases:
        x=case[0]
        y=case[1]
        if grille[y][x][0]==nature:
            cases_possibles.append(case)
    if len(cases_possibles)>0:
        tirage_sort=randrange(len(cases_possibles))
        return cases_possibles[tirage_sort]
    else:
        return False

def evol_gestation(case,grille):
    """
    renvoie la durée de gestation de case moins 1
    param : case : tuple
    param : grille : list
    return : int
    >>> evol_gestation((0,0),Grille)
    1
    >>> evol_gestation((1,1),Grille)
    4
    """
    x=case[0]
    y=case[1]
    return grille[y][x][1]-1

def deplace_vers_mer(nature,case_ini,case_finale,grille,gestation,energie=0):
    """
    modifie la grille suite à un déplacement
    param: nature : int
    param : case_ini: tuple
    param : case_finale : tuple
    param : grille : list
    param : gestation : int
    param : energie : int
    return : list
    """
    nb_lignes=len(grille)
    nb_colonnes=len(grille[0])
    x_ini=case_ini[0]
    y_ini=case_ini[1]
    x_final=case_finale[0]
    y_final=case_finale[1]
    if gestation==0:
        if nature==1:
            grille[y_final][x_final]=init_case(nature)
        elif nature==2:
            grille[y_final][x_final]=(nature,G_REQUIN,energie)        
        grille[y_ini][x_ini]=init_case(nature)
    else:
        grille[y_final][x_final]=(nature,gestation,energie)
        grille[y_ini][x_ini]=init_case(0)    
    return grille
        
        
def tour_thon(case,grille):
    """
    renvoie une nouvelle grille donnant l'état de celle-ci à la fin de ce tour.
    param : case : tuple
    param: liste_cases : list
    param : grille : list
    return : list
    """
    nb_lignes=len(grille)
    nb_colonnes=len(grille[0])
    x=case[0]
    y=case[1]
    temps_gestation=evol_gestation(case,grille)
    recherche=recherche_case(cases_voisines(case, nb_lignes, nb_colonnes),grille,0)
    if recherche:
        grille=deplace_vers_mer(1,case,recherche,grille,temps_gestation)
    else:
        if temps_gestation==0:
            grille[y][x]=init_case(1)
        else:
            grille[y][x]=(1,temps_gestation,0)
    return grille

def evol_energie(case,grille):
    """
    renvoie l'énergie de case moins 1
    param : case : tuple
    param : grille : list
    return : int
    >>> evol_energie((1, 1),[[(1, 2, 0), (1, 2, 0), (0, 0, 0)], [(0, 0, 0),(2, 5, 3), (0, 0, 0)]])
    2
    """
    x=case[0]
    y=case[1]
    return grille[y][x][2]-1


def chasse_au_thon(case_ini,case_finale,grille,gestation):
    """
    retournera la grille ayant évolué en conséquence
    param : case_ini : tuple
    param : case_finale : tuple
    param : grille : list
    param : gestation : int
    """
    nb_lignes=len(grille)
    nb_colonnes=len(grille[0])
    x_ini=case_ini[0]
    y_ini=case_ini[1]
    x_final=case_finale[0]
    y_final=case_finale[1]
    if gestation==0:
        grille[y_ini][x_ini]=init_case(2)
        grille[y_final][x_final]=init_case(2)
    else:
        grille[y_ini][x_ini]=init_case(0)
        grille[y_final][x_final]=(2,gestation,E_REQUIN)
    return grille

def tour_requin(case,grille):
    """
    met à jour la grille après le tour du requin
    param : case : tuple
    param : grille : list
    return : list
    """
    nb_lignes=len(grille)
    nb_colonnes=len(grille[0])
    x=case[0]
    y=case[1]    
    gestation=evol_gestation(case,grille)
    energie=evol_energie(case,grille)
    if energie==0:
       grille[y][x]=init_case(0)
       return grille
    recherche_thon=recherche_case(cases_voisines(case, nb_lignes, nb_colonnes),grille,1)
    recherche_mer=recherche_case(cases_voisines(case, nb_lignes, nb_colonnes),grille,0)  
    if recherche_thon:
        grille=chasse_au_thon(case,recherche_thon,grille,gestation)
    elif recherche_mer:
        grille=deplace_vers_mer(2,case,recherche_mer,grille,gestation,energie)
    else:
        if gestation==0:
            grille[y][x]=(2, G_REQUIN, energie)
        else:
            grille[y][x]=(2, gestation, energie)
    return grille

    
def evol_population(grille):
    """
    renvoie la grille après un temps d'évolution
    param : list
    return : list
    """
    nb_lignes=len(grille)
    nb_colonnes=len(grille[0])
    case=selection_case(nb_colonnes,nb_lignes)
    x=case[0]
    y=case[1]
    if grille[y][x][0]==1:
        tour_thon(case,grille)
    elif grille[y][x][0]==2:
        tour_requin(case,grille)
    return grille
    
    
def simulation(grille, pas_affichage, nb_pas_total):
    """
    Simule N-tours complets de jeu
    :param grille:(list) grille du jeu
    :param p_affichage:(int) pas aubout du quel un affichage de la grille est réalisé
    :param n_pas_total:(int) nombre de pas total pour la simulation
    :return: (NoneType)
    """
    liste_thons = [] # liste contenant le nombre de thons à chaque pas de la simulation
    liste_requins = []  # liste contenant le nombre de requins à chaque pas de la simulation
    for i in range(nb_pas_total):
        evol_population(grille)
        nb_thons = denombre_espece(grille, 1)
        nb_requins = denombre_espece(grille, 2)
        liste_thons.append(nb_thons)
        liste_requins.append(nb_requins)
        if i%pas_affichage==0:
            afficher_grille(grille)
            time.sleep(0.5)
    construct_courbe(liste_thons, liste_requins, nb_pas_total)


def construct_courbe(liste_thons, liste_requins, nb_pas_total):
    """
    Construction et affichage des courbes représentants l'évolution du nombre
    de chaque espèces en fonction du pas de simulation
    :param liste_thons:(list) liste contenant le nombre de thons
    à chaque pas de la simulation
    :param liste_requins:(list) liste contenant le nombre de requins
    à chaque pas de la simulation
    :param nb_pas_total:(int) nombre de pas total pour la simulation
    :return: (NoneType)
    """
    data_x = [i for i in range(nb_pas_total)]  # abscisses
    pylab.plot(data_x, liste_thons, label='Nombre de thons')
    pylab.plot(data_x, liste_requins, label='Nombre de requins')
    pylab.legend()
    pylab.title('Evolution des populations de thons et de requins')
    pylab.xlabel('pas de la simulation')
    pylab.ylabel('Population')
    pylab.grid()
    pylab.show()


def demarrage():
    """
    fonction d'initialisation
    """
    grille = init_grille(P_THON, P_REQUIN, H, V)  # création de la grille aléatoire
    simulation(grille, PAS_AFFICHAGE, PAS_TOTAL)
    
PAS_AFFICHAGE = 200
# indique le nombre de pas entre chaque affichage de la grille-: durée d'un cycle
PAS_TOTAL = 125000

demarrage()


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)