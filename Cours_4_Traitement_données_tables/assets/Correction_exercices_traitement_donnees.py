######################### Exercice 1 ########################
f=open("bon_commande.csv","r")
table_commande1=[ligne.rstrip().split(';') for ligne in f]
f.close()
del(table_commande1[0])
for i in range(len(table_commande1)):
    table_commande1[i][2]=float(table_commande1[i][2].replace(",","."))
    table_commande1[i][3]=int(table_commande1[i][3])
    
print(table_commande1)

dictionnaire_commande={table_commande1[i][0]:[table_commande1[i][1],table_commande1[i][2],table_commande1[i][3]] for i in range(len(table_commande1))}
print(dictionnaire_commande)

######################### Exercice 2 ########################
def verifie_quantites(table):
    """
    Renvoie True si les quantités sont positives, False sinon
    param : table : list
    return : bool
    >>> verifie_quantites(table_commande1)
    True
    """
    for element in table:
        if element[2]==0:
            return False
    return True

def nombre_produit(table):
    """
    Renvoie le nombre de produit commandé
    param : table : list
    return : int
    >>> nombre_produit(table_commande1)
    6
    """
    resultat=0
    for element in table:
        resultat+=element[3]
    return resultat

def prix(table):
    """
    Renvoie le montant de la commande
    param : table : list
    return : int
    >>> prix(table_commande1)
    13.8
    """
    resultat=0
    for element in table:
        resultat+=element[3]*element[2]
    return resultat

######################### Exercice 3 ########################
def tri(table):
    """
    Renvoie un dictionnaire où les valeurs sont rangées dans l'ordre décroissant
    param : table : list
    return : dict
    >>> tri(table_commande1)
    {'cahier petits carreaux': 3.5, 'lot crayons HB': 2.3, 'stylo rouge': 1.5}
    """
    table_tri=sorted(table,key=lambda element:element[2],reverse=True)
    dictionnaire_commande={table_tri[i][1]:table_tri[i][2] for i in range(len(table_tri))}
    return dictionnaire_commande
######################### Exercice 4 ########################
f=open("marques.csv","r")
table_commande2=[ligne.rstrip().split(';') for ligne in f]
f.close()
del(table_commande2[0])
    
print(table_commande2)

def fusion(table1,table2):
    """
    Renvoie la fusion des tables en réalisant leur jointure
    param : table1 : list
    param : table2 : list
    return : list
    >>> fusion(table_commande1,table_commande2)
    [['18635', 'lot crayons HB', 2.3, 1, 'BUC'], ['15223', 'stylo rouge', 1.5, 3, 'PALOT'], ['20112', 'cahier petits carreaux', 3.5, 2, 'CLOSEFONTAINE']]
    """
    resultat=[]
    for element1 in table1:
        for element2 in table2:
            if element1[1]==element2[0]:
                resultat.append([element1[0],element1[1],element1[2],element1[3],element2[1]])
    return resultat

######################### Exercice 5 ########################
import calcul_distance_latitude_longitude as distance

f=open("les_salles_de_cinemas_en_ile-de-france.csv","r")
table_des_donnees=[tuple(ligne.rstrip().split(';')) for ligne in f]
f.close()
del(table_des_donnees[0])

def denombre(departement,table):
    """
    Renvoie le nombre de salles de cinéma dans departement après le parcours de tableau 
    param : departement : str
    param : tableau : list
    return : int
    >>> denombre("93",table_des_donnees)
    30
    """
    compteur=0
    for donnee in table:
        if donnee[1]==departement:
            compteur+=1
    return compteur

def cinema_plus_d_entree(table):
    """
    Renvoie le nom du cinéma qui a fait le plus d'entrée
    param : table : list
    return : str
    >>> cinema_plus_d_entree(table_des_donnees)
    ('LES 2 SCENES', '9987.0')
    """
    resultat=[]
    for donnee in table:
        resultat.append((donnee[2],donnee[22]))
    resultat_ordonnee=sorted(resultat, key=lambda element: element[1])
    return resultat_ordonnee[-1][0],resultat_ordonnee[-1][1]

def cinema_plus_d_entree_par_code(table,code):
    """
    Renvoie le nom du cinéma qui a fait le plus d'entrée
    param : table : list
    param : code : int (#attention, penser à convertir la donnée str en int)
    return : str
    >>> cinema_plus_d_entree_par_code(table_des_donnees,95)
    ('STUDIO CINE', '9939.0')
    """
    resultat=[]
    for donnee in table:
        if int(donnee[1])==code:
            resultat.append((donnee[2],donnee[22]))
    resultat_ordonnee=sorted(resultat, key=lambda element: element[1])
    return resultat_ordonnee[-1][0],resultat_ordonnee[-1][1]

def nombre_de_cinemas_a_distance_de_Paris(table,d):
    """
    Renvoie le nombre de cinema à une distance d de Paris
    >>> nombre_de_cinemas_a_distance_de_Paris(table_des_donnees,10000)
    134
    """
    compteur=0
    for donnee in table:
        if distance.a_paris(float(donnee[36].split(",")[0]),float(donnee[36].split(",")[1]))<d:
            compteur+=1
    return compteur

#####################################################################  
        
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)