import csv

def lecture(text):
    '''
    Renvoie une table à partir du fichier csv
    param : fichier : csv file
    return : list
    >>> lecture('pokemon.csv')[0]
    ['Clic', '60', '80', '95', '50', 'Acier']
    '''
    pass

def distance(p1,p2):
    '''
    Renvoie la distance entre deux pokemons p1 et p2
    param : pokemon1 : list
    param : pokemon2 : list
    return : float
    >>> distance(['Clic', '60', '80', '95', '50', 'Acier'],['Tic', '40', '55', '70', '30', 'Acier'])
    45.27692569068709
    '''
    pass

def critere(donnee):
    """
    Renvoie la deuxième valeur de la donnée
    param : donnee : tuple
    return : int
    >>> critere((42,15))
    15
    """
    pass

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

def creation_dictionnaire(text):
    """
    Renvoie un dictionnaire dont la clé est le nom du pokemon
    param: text : fichier
    return : dict
    >>> creation_dictionnaire('pokemon.csv')['Clic']
    ('60', '80', '95', '50', 'Acier')    
    """

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)