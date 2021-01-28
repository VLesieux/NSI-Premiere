import TSP_biblio



def matrice_distances(fichier):
    """
    génère, à partir du fichier txt, une matrice qui stocke les distances 2 à 2 entre toutes les villes 
    :param fichier: (file name) nom du fichier txt contenant les données
    :return: (list) liste double des distances entre villes deux à deux
    :CU: utilise TSP_biblio
    """
    liste_villes = TSP_biblio.get_tour_fichier(fichier)
    l = len(liste_villes)
    distances = [[0]*l for i in range(l)]
    for i in range(l):
        for j in range(l):
            if(i!=j):
                distances[i][j] =TSP_biblio.distance(liste_villes,i,j)
            else:
                distances[i][j] = 99999 # pour que la ville elle-même ne soit pas la plus proche
    return distances

def liste_ville(fichier):
    '''
    :retourne la liste des indices des villes de 0 à la longueur
    :param fichier:file
    :return:list
    
    '''
    tour=TSP_biblio.get_tour_fichier(fichier)
    l=len(tour)
    liste_ville=[k for k in range(l)]
    return liste_ville


def indice_plus_proche(ville, liste_ville, table):
    distance_min = table[ville][liste_ville[0]]
    indice_min = liste_ville[0]    
    for i in range(len(liste_ville)):
        if table[ville][liste_ville[i]] < distance_min:
            distance_min = table[ville][liste_ville[i]]
            indice_min = liste_ville[i]
    return indice_min

def glouton(ind_ville,liste_ville,mat_dist):
    '''
    :retourne la liste des indices des villes des plus proches
    :param ind_ville:int indice de la ville
    :param liste_ville:list
    :param mat_dist:list
    :return:list
    '''
    l=len(liste_ville)
    ind_depart=ind_ville
    tour=[ind_depart]
    liste_ville.remove(ind_ville)
    while len(tour)!=l:
        ind_ville=indice_plus_proche(ind_ville,liste_ville,mat_dist)
        tour.append(ind_ville)    
        liste_ville.remove(ind_ville)
    tour.append(ind_depart)
    return(tour)

def indice_ville(ville,fichier):
    '''
    :retourne l'indice de la ville dans le fichier
    :param ville:string
    :param fichier:file
    :return:int
    
    '''
    tour=TSP_biblio.get_tour_fichier(fichier)
    liste_ville_vers_indice=[]
    for i in range(len(tour)):
        liste_ville_vers_indice.append(tour[i][0])
    return(liste_ville_vers_indice.index(ville))


def tournee(ville,fichier):
    '''
    :creation de la tournee the tour et affichage
    '''
    ind_ville=indice_ville(ville,fichier)#indice de la ville entree
    mat_distance=matrice_distances(fichier)#matrice des distances
    liste_des_villes=liste_ville(fichier)#liste des indices villes
    tour=TSP_biblio.get_tour_fichier(fichier)
    tournee_liste_indice=glouton(ind_ville,liste_des_villes,mat_distance)
    the_tour=[]
    for i in tournee_liste_indice:
        the_tour.append(tour[i])
    print(the_tour)
    print(TSP_biblio.longueur_tour(the_tour))
    TSP_biblio.trace(the_tour)



#tournee('Lille',"exemple.txt")
    
if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)    