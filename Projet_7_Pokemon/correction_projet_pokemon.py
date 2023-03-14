import csv

def lecture(text):
    '''
    Renvoie une table à partir du fichier csv
    param : fichier : csv file
    return : list
    >>> lecture('pokemon.csv')[0]
    ['Clic', '60', '80', '95', '50', 'Acier']
    '''
    file=open(text,'r')
    table=[]
    for ligne in file:
        table.append(ligne.rstrip().split(';'))
    file.close
    del table[0]
    return table

def distance(p1,p2):
    '''
    Renvoie la distance entre deux pokemons p1 et p2
    param : pokemon1 : list
    param : pokemon2 : list
    return : float
    >>> distance(['Clic', '60', '80', '95', '50', 'Acier'],['Tic', '40', '55', '70', '30', 'Acier'])
    45.27692569068709
    '''
    return ((int(p1[1])-int(p2[1]))**2+(int(p1[2])-int(p2[2]))**2+(int(p1[3])-int(p2[3]))**2+(int(p1[4])-int(p2[4]))**2)**0.5

def critere(donnee):
    """
    Renvoie la deuxième valeur de la donnée
    param : donnee : tuple
    return : int
    >>> critere((42,15))
    15
    """
    return donnee[1]

def K_plus_proches_voisins(text,p,k):
    '''
    Renvoie la liste des k plus proches voisins de pokemon
    param : text : file
    param : p : list
    param : k : int
    return : list formée des tuples (indices,distance)
    >>> K_plus_proches_voisins('pokemon.csv',['Tic', '40', '55', '70', '30', 'Acier'],3)
    [(42, 16.09347693943108), (274, 17.635192088548397), (44, 18.303005217723125)]
    '''
    liste=[ (i,distance(lecture(text)[i],p)) for i in range(len(lecture(text)))]
    liste_triee=sorted(liste,key=critere)
    resultat=[liste_triee[i] for i in range(k+1)]
    del resultat[0]
    return resultat


def renvoie_type(text,p,k):
    '''
    Renvoie le type correspondant à p
    param : text : file
    param : p : list
    param : k : int
    return : str
    >>> renvoie_type('pokemon.csv',['Krabby','30','105','90','50','Eau'],20)
    'Eau'
    '''
    types=['Acier','Combat','Dragon','Eau','Electrik','Fée','Feu','Glace','Insecte','Normal','Plante','Poison','Psy','Roche','Sol','Spectre','Ténèbres','Vol']
    comptes=[0 for i in range(len(types))]
    i=0
    for type_pokemon in types:
        for valeur in K_plus_proches_voisins(text,p,k):
            if lecture(text)[valeur[0]][5]==type_pokemon:
                comptes[i]+=1
        i+=1
    return types[comptes.index(max(comptes))]

def creation_dictionnaire(text):
    """
    Renvoie un dictionnaire dont la clé est le nom du pokemon
    param: text : fichier
    return : dict
    >>> creation_dictionnaire('pokemon.csv')['Clic']
    ('60', '80', '95', '50', 'Acier')    
    """
    liste=lecture(text)
    dictionnaire={liste[i][0]:(liste[i][1],liste[i][2],liste[i][3],liste[i][4],liste[i][5]) for i in range(len(liste))}
    return dictionnaire

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)