from random import randrange
import time
import pylab

G_THON,G_REQUIN,E_THON,E_REQUIN=2,5,0,3
P_THON,P_REQUIN=0.3,0.1

H=25
V=25
PAS_AFFICHAGE = 200
# indique le nombre de pas entre chaque affichage de la grille-: durée d'un cycle
PAS_TOTAL = 125000   # pas total pour la simulation

def creer_grille_methode1(nb_lignes,nb_colonnes):
    """
    Renvoie une grille de nb_colonnes et nb_lignes formé de tuple (0,0,0)
    param : nb_colonnes : int
    param : nb_lignes : int
    return : list
    >>> creer_grille_methode1(2,4)
    [[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]]    
    """
    grille=[]
    for i in range(nb_lignes):
        ligne=[]
        for j in range(nb_colonnes):
            ligne.append(((0, 0, 0)))
        grille.append(ligne)
    return grille

def creer_grille(nb_lignes,nb_colonnes):
    """
    Renvoie une grille de nb_colonnes et nb_lignes formé de tuple (0,0,0)
    param : nb_colonnes : int
    param : nb_lignes : int
    return : list
    >>> creer_grille(2,4)
    [[(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)], [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]]    
    """
    grille=[ [(0, 0, 0) for i in range(nb_colonnes)] for j in range(nb_lignes)]
    return grille


def selection_case(nb_lignes,nb_colonnes):
    return (randrange(nb_lignes),randrange(nb_colonnes))


def init_case(nature):
    """
    >>> init_case(0)
    (0, 0, 0)
    >>> init_case(1)
    (1, 2, 0)
    >>> init_case(2)
    (2, 5, 3)
    """
    if nature==0:
        sortie=(0, 0, 0)
    elif nature==1:
        sortie=(1,G_THON,E_THON)
    else:
        sortie=(2,G_REQUIN,E_REQUIN)
    return sortie
    

def placement_espece(grille,nature,nb_poissons):
    while nb_poissons>0:
        case=selection_case(len(grille),len(grille[0]))        
        if grille[case[0]][case[1]][0]==0:
            grille[case[0]][case[1]]=init_case(nature)
            nb_poissons-=1
    return grille
            

def denombre_espece(grille,nature):
    """
    >>> denombre_espece(placement_espece(creer_grille(3,2),2,4),2)
    4
    >>> denombre_espece(init_grille(0.5,0.5,2,2), 1)
    2
    >>> denombre_espece(init_grille(0.5,0.5,2,2), 2)
    2
    """
    compteur=0
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j][0]==nature:
                compteur+=1
    return compteur


def init_grille(p_thons,p_requins,nb_lignes,nb_colonnes):
    """
    Renvoie une grille possédant nb_lignes et nb_colonnes
    avec p_thons et p_requins
    >>> denombre_espece(init_grille(0.5,0.5,2,2), 1)
    2
    >>> denombre_espece(init_grille(0.5,0.5,2,2), 2)
    2    
    """
    nombre_thons=p_thons*nb_lignes*nb_colonnes
    nombre_requins=p_requins*nb_lignes*nb_colonnes
    grille=creer_grille(nb_lignes,nb_colonnes)
    placement_espece(grille,1,nombre_thons)
    placement_espece(grille,2,nombre_requins)
    return grille

def afficher_grille(grille):
    """
    >>> grille1 = [[(1, 2, 0), (1, 2, 0), (0, 0, 0)],[(0, 0, 0), (2, 5, 3), (0, 0, 0)]]
    >>> afficher_grille(grille1)
     T  T  _ 
     _  R  _ 
     
    """
    chaine=""
    for i in range(len(grille)):
        for j in range(len(grille[0])):
            if grille[i][j][0]==0:
                chaine+=" _ "
            elif grille[i][j][0]==1:
                chaine+=" T "
            else:
                chaine+=" R "
        chaine+="\n"
    print(chaine)

def cases_voisines(case,nb_lignes,nb_colonnes):
    """
    Renvoie les 4 cases voisines de case dans la grille torique
    dans l'ordre OUEST, NORD, SUD et EST
    >>> cases_voisines((1,1),2,2)
    [(1, 0), (0, 1), (0, 1), (1, 0)]
    >>> cases_voisines((1,1),3,3)
    [(1, 0), (0, 1), (2, 1), (1, 2)]
    >>> cases_voisines((0,2),3,3)
    [(0, 1), (2, 2), (1, 2), (0, 0)]
    """
    x=case[0]
    y=case[1]
    if x>0:
        case_nord=(x-1,y)
    else:
        case_nord=(nb_lignes-1,y)
    if x<nb_lignes-1:
        case_sud=(x+1,y)
    else:
        case_sud=(0,y)
    if y>0:
        case_ouest=(x,y-1)
    else:
        case_ouest=(x,nb_colonnes-1)
    if y<nb_colonnes-1:
        case_est=(x,y+1)
    else:
        case_est=(x,0)
    return [case_ouest,case_nord,case_sud,case_est]
    
    
def recherche_case(liste_4_cases,grille,nature):
    """
    Choisit aléatoirement dans la liste_4_cases celle qui correspondent à nature si possible
    sinon renvoie False
    >>> grille_exemple=[[(1, 2, 0), (0, 0, 0), (0, 0, 0)],[(1, 2, 0), (2, 5, 3), (0, 0, 0)],[(0, 0, 0), (0, 0, 0), (0, 0, 0)]]
    >>> afficher_grille(grille_exemple)
     T  _  _ 
     T  R  _ 
     _  _  _ 

    >>> recherche_case(cases_voisines((1,1),3,3),grille_exemple,1)
    (1, 0)
    """
    possible=[]
    for element in liste_4_cases:
        if grille[element[0]][element[1]][0]==nature:
            possible.append(element)
    if len(possible)>0:
        return possible[randrange(len(possible))]
    else:
        return False


def evol_gestation(case,grille):
    """
    Renvoie le niveau de gestation diminué d'une unité
    >>> grille_exemple=[[(1, 2, 0), (0, 0, 0), (0, 0, 0)],[(1, 2, 0), (2, 5, 3), (0, 0, 0)], [(0, 0, 0), (1, 2, 0), (0, 0, 0)]]
    >>> evol_gestation((0,0),grille_exemple)
    1
    >>> evol_gestation((1,1),grille_exemple)
    4    
    """
    return grille[case[0]][case[1]][1]-1



def deplace_vers_mer(nature,case_initiale,case_finale,grille,gestation,energie=0):
    """
    >>> grille1 = [[(1, 2, 0), (1, 2, 0), (0, 0, 0)],[(0, 0, 0), (2, 5, 3), (0, 0, 0)]]
    >>> afficher_grille(grille1)
     T  T  _ 
     _  R  _ 

    >>> afficher_grille(deplace_vers_mer(1, (0, 0), (1, 0),grille1, 1))
     _  T  _ 
     T  R  _
    >>> grille2 = [[(1, 0, 0), (1, 2, 0), (0, 0, 0)],[(0, 0, 0), (2, 5, 3), (0, 0, 0)]]
    >>> afficher_grille(grille2)
     T  T  _ 
     _  R  _ 

    >>> afficher_grille(deplace_vers_mer(1, (0, 0), (1, 0),grille2, 0))
     T  T  _ 
     T  R  _ 
    """
    if gestation==0:
        if nature==1:
            grille[case_finale[0]][case_finale[1]]=init_case(nature)
        elif nature==2:
            grille[case_finale[0]][case_finale[1]]=(2,G_REQUIN,energie)
        grille[case_initiale[0]][case_initiale[1]]=init_case(nature)
    else:
        grille[case_finale[0]][case_finale[1]]=(nature,gestation,energie)
        grille[case_initiale[0]][case_initiale[1]]=init_case(0)
    return grille
            
def tour_thon(case,grille):
    """
    >>> grille1=[[(0, 0, 0), (1, 2, 0), (0, 0, 0)],[(1, 1, 0), (2, 5, 3), (2, 5, 3)]]
    >>> afficher_grille(grille1)
     _  T  _ 
     T  R  R 
    >>> afficher_grille(tour_thon((1,0),grille1))
     T  T  _ 
     T  R  R   
    """
    liste=cases_voisines(case,len(grille),len(grille[0]))
    gestation = evol_gestation(case, grille)
    # recherche d'une mer libre dans les cases voisines
    case_mer = recherche_case(liste, grille, 0)
    if case_mer:
        grille = deplace_vers_mer(1, case, case_mer, grille, gestation)
    else:  # si pas de cases dispo
        if gestation == 0:  # si la durée de gestation devient nulle
            grille[case[0]][case[1]] = init_case(1)  # durée de gestation réinitialisée
        else:
            grille[case[0]][case[1]] = (1, gestation, 0)
    return grille 

    
def evol_energie(case,grille):
    """
    Renvoie le niveau de gestation diminué d'une unité
    >>> grille_exemple=[[(1, 2, 0), (0, 0, 0), (0, 0, 0)],[(1, 2, 0), (2, 5, 3), (0, 0, 0)], [(0, 0, 0), (1, 2, 0), (0, 0, 0)]]
    >>> evol_energie((1,1),grille_exemple)
    2 
    """
    return grille[case[0]][case[1]][2]-1


def chasse_au_thon(case_initiale,case_finale,grille,gestation):
    """
    >>> grille1=[[(1, 2, 0), (1, 2, 0), (0, 0, 0)],[(0, 0, 0),(2, 0, 3), (0, 0, 0)]]
    >>> afficher_grille(grille1)
     T  T  _ 
     _  R  _ 

    >>> afficher_grille(chasse_au_thon((1,1),(0,1),grille1,0))
     T  R  _ 
     _  R  _ 
    
    """
    if gestation==0:
        grille[case_finale[0]][case_finale[1]]=init_case(2)
        grille[case_initiale[0]][case_initiale[1]]=init_case(2)# un requin nait sur la case quittée
    else:
        grille[case_finale[0]][case_finale[1]]=(2, gestation, E_REQUIN)
        # le requin mange le thon, son energie est restaurée
        grille[case_initiale[0]][case_initiale[1]]=init_case(0)# case quittée devient une mer
    return grille    

def tour_requin(case,grille):
    """
    >>> grille1=[[(1, 2, 0), (1, 2, 0), (0, 0, 0)],[(0, 0, 0),(2, 2, 4), (0, 0, 0)]]
    >>> afficher_grille(grille1)
     T  T  _ 
     _  R  _ 

    >>> afficher_grille(tour_requin((1,1),grille1))
     T  R  _ 
     _  _  _
    >>> grille2=[[(1, 2, 0), (1, 2, 0), (0, 0, 0)],[(0, 0, 0),(2, 2, 1), (0, 0, 0)]]
    >>> afficher_grille(grille2)
     T  T  _ 
     _  R  _ 

    >>> afficher_grille(tour_requin((1,1),grille2))
     T  T  _ 
     _  _  _
    >>> grille3=[[(1, 2, 0), (1, 2, 0), (0, 0, 0)],[(0, 0, 0),(2, 1, 2), (0, 0, 0)]]
    >>> afficher_grille(grille3)
     T  T  _ 
     _  R  _ 

    >>> afficher_grille(tour_requin((1,1),grille3))
     T  R  _ 
     _  R  _ 

    """
    liste=cases_voisines(case,len(grille),len(grille[0]))
    gestation = evol_gestation(case, grille)  # durée de gestation du requin
    energie = evol_energie(case, grille)
    if energie == 0:  # si energie nulle
        grille[case[0]][case[1]] = init_case(0)  # le requin ne se déplace pas et meurt
        return grille
    case_thon = recherche_case(liste, grille, 1)  # recherche d'un thon dans les cases voisines
    if case_thon:
        grille = chasse_au_thon(case, case_thon, grille, gestation)
    else:  # sinon recherche d'une mer libre dans les cases voisines
        case_mer = recherche_case(liste, grille, 0)
        if case_mer:  # si case de mer trouvée
            if energie == 0:  # si l'énergie est nulle
                grille[case_mer[0]][case_mer[1]] = init_case(0)  # le requin meurt
                grille[case[0]][case[1]] = init_case(0)  # case quittée devient une mer
            else:  # si energie requin n'est pas  nulle
                grille = deplace_vers_mer(2, case, case_mer, grille, gestation, energie)
        else:  # pas de déplacement
            if energie == 0:  # si energie nulle
                grille[case[0]][case[1]] = init_case(0)  # le requin ne se déplace pas et meurt
            else:
                if gestation == 0:  # si la gestation devient nulle
                    # la durée de gestation est réinitialisée
                    grille[case[0]][case[1]] = (2, G_REQUIN, energie)
                else:
                    grille[case[0]][case[1]] = (2, gestation, energie)
    return grille
            
        
def evol_population(grille):
    case_choisie=selection_case(len(grille),len(grille[0]))
    if grille[case_choisie[0]][case_choisie[1]][0]==1:
        tour_thon(case_choisie,grille)
    elif grille[case_choisie[0]][case_choisie[1]][0]==2:
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
        afficher_grille(grille)
#        time.sleep(0.5)
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
    
    
demarrage()


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)