############################### À faire 1. ##################################
def valeur_commune(liste):
    """
    Renvoie la valeur commune de la liste sinon renvoie False
    param : liste : list
    return : int ou bool
    >>> valeur_commune([4,4,4,4])
    4
    >>> valeur_commune([4,4,3,4])
    False
    """
    for element in liste:
        if element !=liste[0]:
            return False
    return liste[0]
    ############################### À faire 2. ##################################
def valeur_commune_version2(liste):
    """
    Renvoie la valeur commune de la liste sinon renvoie False
    param : liste : list
    return : int ou bool
    >>> valeur_commune_version2([4,4,4,4])
    4
    >>> valeur_commune_version2([4,4,3,4])
    False
    """
    if all([liste[i]==liste[0] for i in range(len(liste))]):
        return liste[0]
    else:
        return False
    
#     
#     
#     
    ############################### À faire 3. ##################################
def somme_rangees(carre):
    """
    Renvoie la somme des valeurs des rangées
    param : carre
    return : list
    >>> somme_rangees([[2,8,6],[9,5,1],[4,3,8]])#ce carre n'est donc pas magique
    [16, 15, 15]
    """
    return [sum([carre[i][j] for j in range(len(carre))]) for i in range(len(carre))]


############################### À faire 4. ##################################
def somme_colonnes(carre):
    """
    Renvoie la somme des valeurs des colonnes
    param : carre
    return : list
    >>> somme_colonnes([[2,8,6],[9,5,1],[4,3,8]])#ce carre n'est donc pas magique
    [15, 16, 15]
    """
    return [sum([carre[i][j] for i in range(len(carre))]) for j in range(len(carre))]

############################### À faire 5. ##################################

def somme_premiere_diagonale(carre):
    """
    Renvoie la somme des valeurs de la première diagonale
    param : carre
    return : int
    >>> somme_premiere_diagonale([[2,7,6],[9,5,1],[4,3,8]])
    15
    """
    return sum([carre[i][i] for i in range(len(carre))])
# 
############################### À faire 6. ##################################

def somme_deuxieme_diagonale(carre):
    """
    Renvoie la somme des valeurs de la deuxième diagonale
    param : carre
    return : int
    >>> somme_deuxieme_diagonale([[2,7,6],[9,5,1],[5,3,8]])
    16
    """
    return sum([carre[i][len(carre)-1-i] for i in range(len(carre))])
# 
############################### À faire 7. ##################################
def est_magique(carre):
    """
    Renvoie True si le carre est magique, False sinon
    param : carre : list
    return : bool
    >>> est_magique([[2,7,6],[9,5,1],[4,3,8]])
    True
    >>> est_magique([[4,5,11,14],[15,10,8,1],[6,3,13,12],[9,16,2,7]])
    True
    >>> est_magique([[4,2,11,14],[15,10,8,1],[6,3,13,12],[9,16,2,7]])
    False
    """
    return valeur_commune(somme_colonnes(carre))==valeur_commune(somme_rangees(carre)) and valeur_commune(somme_colonnes(carre))==somme_deuxieme_diagonale(carre) and valeur_commune(somme_colonnes(carre))==somme_premiere_diagonale(carre)
############################### À faire 8 ##################################

# 
# liste=[]
# 
# 
# for a in range(1,6):
#     for b in range(1,6):
#         for c in range(1,6):
#             for d in range(1,6):
#                 for e in range(1,6):
#                     for f in range(1,6):
#                         for g in range(1,6):
#                             for h in range(1,6):
#                                 for i in range(1,6):
#                                     if est_magique([[a,b,c],[d,e,f],[g,h,i]]):
#                                         liste.append([[a,b,c],[d,e,f],[g,h,i]])
# print(len(liste))
                        
    
if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)