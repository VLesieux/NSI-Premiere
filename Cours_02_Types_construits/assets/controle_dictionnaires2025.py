def fusion_filtre(d1, d2, s):
    """
    Fusionne deux dictionnaires (additionne les valeurs des clés communes)
    et filtre les valeurs strictement supérieures à un seuil s.

    Params :
      d1 : dict[str, int]
      d2 : dict[str, int]
      s  : int (seuil)

    Return :
      dict[str, int] contenant uniquement les clés dont la valeur est > s

    >>> fusion_filtre({"a": 3, "b": 7}, {"b": 4, "c": 2}, 5)
    {'b': 11}
    >>> fusion_filtre({"x": 1}, {"y": 10, "x": 2}, 2)
    {'x': 3, 'y': 10}
    >>> fusion_filtre({"m": 5}, {"n": 1, "m": 1}, 5)
    {'m': 6}
    >>> fusion_filtre({}, {"p": 9, "q": 2}, 3)
    {'p': 9}
    """
    # Étape 1 : fusion (somme des valeurs pour les clés communes)
    
    fusion = d1.copy()
    ###########A compléter 1 : parcours des cles et valeurs du dictionnaire d2###########################
        fusion[cle] = fusion.get(cle, 0) + val
    #########fusion.get(cle, 0) renvoie 0 si cle n'existe pas dans fusion################################
        
    # Étape 2 : filtrage strict (> s). On renvoie un nouveau dict construit par compréhension.
    ###########A compléter 2#############################################################################


def somme_scores(liste_dicts):
    """
    Calcule la somme des scores pour chaque nom.
    param : liste_dicts : list
    return : dict[str,int]
    >>> somme_scores([{"Alice": 5}, {"Bob": 3}, {"Alice": 2}, {"Bob": 7}])
    {'Alice': 7, 'Bob': 10}
    >>> somme_scores([])
    {}
    """
    resultat = {}
   ###########A compléter 3 : parcours les éléments de liste_dicts###########################
   ###########A compléter 4 : parcours les nom et scores des dictionnaires###########################
            resultat[nom] = resultat.get(nom, 0) + score#resultat.get(nom, 0) renvoie 0 si nom n'est pas une clé de resultat
    return resultat

def filtre_tuple(t, seuil):
    """
    Renvoie un tuple avec les valeurs supérieures au seuil.
    param : t : tuple
    param : seuil : int
    >>> filtre_tuple((1, 5, 8, 2, 10), 5)
    (8, 10)
    >>> filtre_tuple((0, -1, -5), 0)
    ()
    """
    ###########A compléter 5 : renvoie un tuple créé par compréhension###########################
    #### utiliser tuple() qui transforme une liste créée par compréhension en tuple


def inverse_dict(d):
    """
    Inverse un dictionnaire (clé <-> valeur).
    param : dict[str,int]
    return : dict[int,str]
    >>> inverse_dict({"a": 1, "b": 2, "c": 3})
    {1: 'a', 2: 'b', 3: 'c'}
    """
    ###########A compléter 6 : renvoie un dictionnaire créé par compréhension###########################

def compte_mots(phrase):
    """
    Renvoie un dictionnaire avec les fréquences de chaque mot.
    param : str
    return : dict[str,int]
    >>> compte_mots("Le chat dort et le chien dort")
    {'le': 2, 'chat': 1, 'dort': 2, 'et': 1, 'chien': 1}
    >>> compte_mots("Python python PYTHON")
    {'python': 3}
    """
    mots = phrase.lower().split(' ')#met le texte en minuscule avec la méthode lower() puis transforme en liste
    #avec la méthode split qui utilise l'espace comme séparateur
    d = {}
    ###########A compléter 7 : parcours les mot de mots###########################
        d[mot] = d.get(mot, 0) + 1#d.get(mot, 0) renvoie 0 si mot n'est pas une clé de d
    return d

def paires_consecutives(liste):
    """
    Renvoie les paires d'éléments consécutifs dans la liste.
    param : liste
    return : liste
    >>> paires_consecutives([1, 2, 3, 4])
    [(1, 2), (2, 3), (3, 4)]
    >>> paires_consecutives([5, 7, 8, 9, 11])
    [(7, 8), (8, 9)]
    >>> paires_consecutives([7])
    []
    """
    ###########A compléter 8 : renvoie une liste créée par compréhension###########################

def cles_max(d):
    """
    Renvoie une liste avec la ou les clés ayant la valeur maximale.
    param : d : dict[str,int]
    return : list
    >>> cles_max({"a": 3, "b": 7, "c": 7, "d": 2})
    ['b', 'c']
    >>> cles_max({"x": 1})
    ['x']
    """
    ###########A compléter 9 : cherche le max des valeurs de d en utilisant max()###########################
    ###########A compléter 10 : renvoie une liste créée par compréhension###########################
    

if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)