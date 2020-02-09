# coding: UTF-8
import random, numpy, math, pylab, copy

def get_tour_fichier(f):
    """
    :author: DIU-Bloc2 - Univ. Lille
    :date: 2019, Mai
    : lecture fichier de ville format ville, latitude, longitude
    : renvoie un tour contenant les villes dans l ordre du fichier
    : param f: file
    : return : (list)
    """
    fichier = open(f, "r")
    tour_initial = fichier.read().replace (",", ".").split ("\n")
    tour_initial=[ t.strip ("\r\n ").split ("\t") for t in tour_initial ]
    tour_initial = [ t [:1] + [ float (x) for x in t [1:] ] for t in tour_initial ]
    fichier.close()
    return tour_initial[:len(tour_initial)-1]


def distance (tour, i,j) :
    """
    Calcul la distance euclidienne entre i et j
    : param tour: seqeunce de ville
    : param i: numero de la ville de départ
    : param j: numero de la ville d arrivee
    : return: float
    CU: i et j dans le tour
    """
    dx = tour [i][1] - tour [j][1]
    dy = tour [i][2] - tour [j][2]
    return (dx**2 + dy**2) ** 0.5


def longueur_tour (tour) :
    """
    calcul la longueur total d une tournée de la ville de départ et retourne à la ville de départ
    : param tour: tournee de ville n villes = n segments
    : return: float distance totale
    """
    d = 0
    for i in range (0,len(tour)-1) :
        d += distance (tour, i,i+1)
    # il ne faut pas oublier de boucler pour le dernier segment  pour retourner à la ville de départ
    d += distance (tour, 0,-1)
    return d

def trace (tour) :
    """
    Trace la tournée realisée
    : param tour: list de ville
    """
    x = [ t[1] for t in tour ]
    y = [ t[2] for t in tour ] 
    x += [ x [0] ] # on ajoute la dernière ville pour boucler
    y += [ y [0] ] #
    pylab.plot (x,y, linewidth=5)
    for ville,x,y in tour :
        pylab.text (x,y,ville) 
    pylab.show ()

    
def test2():
    """
    Fonction de test des fonctions precedentes
    """
    
    the_tour = get_tour_fichier("exemple.txt")
    print(the_tour)
    print(longueur_tour(the_tour))
    trace(the_tour)
