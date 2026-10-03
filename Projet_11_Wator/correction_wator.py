from random import randrange
import pylab
import time
H=25
V=25

G_THON=2
G_REQUIN=5
E_THON=0
E_REQUIN=3


P_THON=0.3
P_REQUIN=0.1
PAS_AFFICHAGE = 200
# indique le nombre de pas entre chaque affichage de la grille-: durée d'un cycle
PAS_TOTAL = 125000   # pas total pour la simulation

def creer_grille_methode1(n,p):
    """
    renvoie une liste de listes correspondant à une grille aux dimensions souhaitées
    n désigne le nombre de lignes, p désigne le nombre de colonnes
    param : n : int 
    param : p : int
    param : return : list
    Exemple:
    >>> creer_grille_methode1(2,2)
    [[(0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0)]]
    """
    liste1=[]
    for i in range(n):
        liste2=[]
        for j in range(p):
            liste2.append((0,0,0))
        liste1.append(liste2)
    return liste1

def creer_grille(nb_ligne,nb_colonne):
    """
    renvoie une liste de listes correspondant à une grille aux dimensions souhaitées
    n désigne le nombre de lignes, p désigne le nombre de colonnes
    param : n : int 
    param : p : int
    param : return : list
    Exemple:
    >>> creer_grille(2,4)
    [[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]]
    """
    return [[(0, 0, 0) for _ in range(nb_colonne)] for _ in range(nb_ligne)]


def selection_case(taille_horizontale,taille_verticale):
    """
    Renvoie un tuple qui désigne une case choisie aléatoirement dans la grille
    """
    return (randrange(taille_horizontale),randrange(taille_verticale))


def init_case(nature):
    """
    Renvoie le tuple correspondant aux valeurs initiales des paramètres de gestation G et d'énergie E correspondant à la nature de l'élément
    param : nature : int
    param : return : tuple
    Exemple:
    >>> init_case(1)
    (1, 2, 0)
    """
    if nature==0:
        case=(0, 0, 0)
    elif nature==1:
        case=(1,G_THON,E_THON)
    else:
        case=(2,G_REQUIN,E_REQUIN)
    return case

def placement_espece(grille,nature,nb_poissons):
    """
    renvoie une grille qui contient le nombre de poissons de cette nature placés aléatoirement
    param: grille: list
    param: nature : int
    param : nb_poissons
    param : return : list
    """
    while nb_poissons>0:
        case=selection_case(len(grille[0]),len(grille))
        if grille[case[1]][case[0]][0]==0:
            grille[case[1]][case[0]]=init_case(nature)
            nb_poissons-=1
    return grille


def denombre_espece(grille,nature):
    """
    renvoie le nombre d'espèce de la nature donnée dans la grille
    param : grille : list
    param : nature : int
    param : return : int
    Exemple:
    >>> denombre_espece(placement_espece(creer_grille(3,2),2,4),2)
    4
    """
    compte=0
    for ligne in grille:
        for case in ligne:
            if case[0]==nature:
                compte+=1
    return compte

def init_grille(p_thons,p_requins,nb_lignes,nb_colonnes):
    """
    renvoie une grille de nb_lignes et n_colonnes comportant les pourcentages de thons et de requins
    Exemples:
    >>> denombre_espece(init_grille(0.5,0.5,2,2), 1)
    2
    """
    nb_thons=p_thons*nb_lignes*nb_colonnes
    nb_requins=p_requins*nb_lignes*nb_colonnes
    grille=creer_grille(nb_lignes,nb_colonnes)
    placement_espece(grille,1,nb_thons)
    placement_espece(grille,2,nb_requins)
    return grille


    
def afficher_grille(grille):
    for ligne in grille:
        texte=""
        for case in ligne:
            if case[0]==0:
                texte+=" _ "
            elif case[0]==1:
                texte+=" T "
            else:
                texte+=" R "
        print(texte)

            
def cases_voisines(case,nb_lignes,nb_colonnes):
    """
    Retourne la liste des cases voisines N,O,E,S
    >>> cases_voisines((1,1),2,2)
    [(1, 0), (0, 1), (0, 1), (1, 0)]
    >>> cases_voisines((1,1),3,3)
    [(1, 0), (0, 1), (2, 1), (1, 2)]
    >>> cases_voisines((2,0),3,3)
    [(2, 2), (1, 0), (0, 0), (2, 1)]
    """
    liste=[]
    #case au Nord
    if case[1]==0:
        liste.append((case[0],nb_lignes-1))
    else:
        liste.append((case[0],case[1]-1))
    #case à l'ouest
    if case[0]==0:
        liste.append((nb_colonnes-1,case[1]))
    else:
        liste.append((case[0]-1,case[1]))
    #case à l'est
    if case[0]==nb_colonnes-1:
        liste.append((0,case[1]))
    else:
        liste.append((case[0]+1,case[1]))
    #case au Sud
    if case[1]==nb_lignes-1:
        liste.append((case[0],0))
    else:
        liste.append((case[0],case[1]+1))
    return liste

       
def recherche_case(liste,grille,nature):
    """
    Renvoie aléatoirement une des cases de la liste présente dans la grille
    et qui répond à la nature demandée
    : param liste : (list) représente une liste de cases
    : param grille : (grille) représente la grille dans laquelle il faut chercher les cases
    : param nature : (int) la nature de la case
    :Exemples:
    >>> grille = [[(1,2,0),(0,0,0),(0,0,0)],[(0,0,0),(2,5,3),(0,0,0)]]
    >>> recherche_case([(2, -1), (1, 0), (0, 0), (2, 1)], grille, 2)
    False
    >>> recherche_case([(1, -1), (0, 0), (2, 0), (1, 1)], grille, 1)
    (0, 0)
    
    """
    possible=[]
    for element in liste:
        if grille[element[1]][element[0]][0]==nature:
            possible.append(element)
    if len(possible)>0:
        return possible[randrange(len(possible))]
    else:
        return False
    
def evol_gestation(case,grille):
    return grille[case[1]][case[0]][1]-1


def deplace_vers_mer(nature,case_ini,case_mer,grille,duree_gestation,energie=0):
    if duree_gestation ==0:
        if nature==1:
            grille[case_mer[1]][case_mer[0]]=init_case(nature)
        elif nature==2:
            grille[case_mer[1]][case_mer[0]]=(2,G_REQUIN,energie)
        grille[case_ini[1]][case_ini[0]]=init_case(nature)
    else:
        grille[case_mer[1]][case_mer[0]]=(nature,duree_gestation,energie)
        grille[case_ini[1]][case_ini[0]]=init_case(0)
    return grille


def tour_thon(case,grille):
    """
    Traduit le comportement d'un thon lors de son tour
    :param case:(tuple) coordonnées de la case choisie contenant un thon de la forme (x, y)
    :param liste:(list) coordonnées des 4 cases voisines (liste de tuples)
    :param grille:(list) grille du jeu
    :return: (list) la grille mise à jour après le tour du thon
    """
    liste=cases_voisines(case,len(grille),len(grille[0]))
    gestation = evol_gestation(case, grille)
    # recherche d'une mer libre dans les cases voisines
    case_mer = recherche_case(liste, grille, 0)
    if case_mer:
        grille = deplace_vers_mer(1, case, case_mer, grille, gestation)
    else:  # si pas de cases dispo
        if gestation == 0:  # si la durée de gestation devient nulle
            grille[case[1]][case[0]] = init_case(1)  # durée de gestation réinitialisée
        else:
            grille[case[1]][case[0]] = (1, gestation, 0)
    return grille       
    
def evol_energie(case,grille):
    return grille[case[1]][case[0]][2]-1    
    
def chasse_au_thon(case, case_thon, grille, gestation):
    """
    renvoie la grille mise à jour
    : param case_depart : (tuple) les coordonnées
    : param case_occupee : (tuple) les coordonnées
    : param grille : (list) la grille
    : param gestation : (int) le niveau de gestation
    """
    if gestation == 0:  # si la gestation devient nulle
        grille[case[1]][case[0]] = init_case(2)  # un requin nait sur la case quitée
        grille[case_thon[1]][case_thon[0]] = init_case(2)
        # le requin mange le thon, son energie et sa gestation sont restaurées
    else:
        grille[case_thon[1]][case_thon[0]] = (2, gestation, E_REQUIN)
        # le requin mange le thon, son energie est restaurée
        grille[case[1]][case[0]] = init_case(0)  # case quittée devient une mer
    return grille    

def tour_requin(case,grille):
    """
     Traduit le comportement d'un requin lors de son tour
    :param case:(tuple) coordonnées de la case requin de la forme (x,y)
    :param liste:(list) coordonnées des 4 cases voisines (liste de tuples)
    :param grille:(list) grille du jeu
    :return: (list) la grille mise à jour après le tour du requin
    """
    liste=cases_voisines(case,len(grille),len(grille[0]))
    gestation = evol_gestation(case, grille)  # durée de gestation du requin
    energie = evol_energie(case, grille)
    if energie == 0:  # si energie nulle
        grille[case[1]][case[0]] = init_case(0)  # le requin ne se déplace pas et meurt
        return grille
    case_thon = recherche_case(liste, grille, 1)  # recherche d'un thon dans les cases voisines
    if case_thon:
        grille = chasse_au_thon(case, case_thon, grille, gestation)
    else:  # sinon recherche d'une mer libre dans les cases voisines
        case_mer = recherche_case(liste, grille, 0)
        if case_mer:  # si case de mer trouvée
            if energie == 0:  # si l'énergie est nulle
                grille[case_mer[1]][case_mer[0]] = init_case(0)  # le requin meurt
                grille[case[1]][case[0]] = init_case(0)  # case quittée devient une mer
            else:  # si energie requin n'est pas  nulle
                grille = deplace_vers_mer(2, case, case_mer, grille, gestation, energie)
        else:  # pas de déplacement
            if energie == 0:  # si energie nulle
                grille[case[1]][case[0]] = init_case(0)  # le requin ne se déplace pas et meurt
            else:
                if gestation == 0:  # si la gestation devient nulle
                    # la durée de gestation est réinitialisée
                    grille[case[1]][case[0]] = (2, G_REQUIN, energie)
                else:
                    grille[case[1]][case[0]] = (2, gestation, energie)
    return grille


def evol_population(grille):
    case_choisie=selection_case(len(grille),len(grille[0]))
    if grille[case_choisie[1]][case_choisie[0]][0]==1:
        tour_thon(case_choisie,grille)
    elif grille[case_choisie[1]][case_choisie[0]][0]==2:
        tour_requin(case_choisie,grille)
    return grille

def simulation(grille, p_affichage, n_pas_total):
    """
    Simule N-tours complets de jeu
    :param grille:(list) grille du jeu
    :param p_affichage:(int) pas aubout du quel un affichage de la grille est réalisé
    :param n_pas_total:(int) nombre de pas total pour la simulation
    :return: (NoneType)
    """
    liste_thons = [] # liste contenant le nombre de thons à chaque pas de la simulation
    liste_requins = []  # liste contenant le nombre de requins à chaque pas de la simulation
    for i in range(n_pas_total//p_affichage):
        for _ in range(p_affichage):
            evol_population(grille)
            nb_thons = denombre_espece(grille, 1)
            nb_requins = denombre_espece(grille, 2)
            liste_thons.append(nb_thons)
            liste_requins.append(nb_requins)
        afficher_grille2(grille, (i+1)*p_affichage, nb_thons, nb_requins)
        time.sleep(0.5)
    construct_courbe(liste_thons, liste_requins, n_pas_total)


def construct_courbe(liste_n_thons, liste_n_requins, n_pas_total):
    """
    Construction et affichage des courbes représentants l'évolution du nombre
    de chaque espèces en fonction du pas de simulation
    :param liste_n_thons:(list) liste contenant le nombre de thons
    à chaque pas de la simulation
    :param liste_n_requins:(list) liste contenant le nombre de requins
    à chaque pas de la simulation
    :param n_pas_total:(int) nombre de pas total pour la simulation
    :return: (NoneType)
    """
    data_x = [i for i in range(n_pas_total)]  # abscisses
    pylab.plot(data_x, liste_n_thons, label='Nombre de thons')
    pylab.plot(data_x, liste_n_requins, label='Nombre de requins')
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
    
def afficher_grille2(grille, pas_simul, nb_thons, nb_requins):
    """
    Réalise un affichage de la grille avec les paramètres de la simulation
    :param grille: (list) représente la grille du jeu
    :pas_simul:(int) valeur du pas de simulation
    :nb_thons:(int) nombre de thons présents dans la grille
    :nb_requins:(int) nombre de requins présents dans la grille
    :return: (NoneType) None
    :CU:  Les cases de mer seront affichées avec un tiret bas (_)
    , les cases requins avec un "R", celles avec un thon avec un "T"
      Le contenu des cases sera séparé par une espace.
      Chaque ligne de la grille sera affichée sur une ligne distincte.
    :Exemples:
    >>> grille = [[(0, 0, 0), (1, 0, 0), (0, 0, 0)], \
    [(2, 0, 0), (0, 0, 0), (0, 0,0)], \
    [(2, 0, 0), (1, 0, 0), (1, 0, 0)]]
    >>> afficher_grille(grille)
    _  T  _
    R  _  _
    R  T  T
    >>> afficher_grille(creer_grille(3, 2))
     _  _  _
     _  _  _

    """
    affichage = f'pas de simulation : {pas_simul}/{PAS_TOTAL} \n \
Nombre de thons :{nb_thons} Nombre de requins: {nb_requins}  \n\n'
    for ligne in grille:
        for case in ligne:
            if case[0] == 0:
                affichage += "_"+" "
            elif case[0] == 1:
                affichage += "T"+" "
            elif case[0] == 2:
                affichage += "R"+" "
        affichage += "\n"
    print(affichage)

    
demarrage()

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
        
    