def fusion_filtre(d1, d2, s):
    """
    Fusionne deux dictionnaires (additionne les valeurs des clés communes)
    et filtre les valeurs strictement supérieures à un seuil s.

    Paramètres :
      d1 : dict[str, int]
      d2 : dict[str, int]
      s  : int (seuil)

    Retour :
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
    for cle, val in d2.items():
        fusion[cle] = fusion.get(cle, 0) + val

    # Étape 2 : filtrage strict (> s). On construit un nouveau dict (sans muter pendant l'itération).
    return {cle: val for cle, val in fusion.items() if val > s}


def somme_scores(liste_dicts):
    """
    Calcule la somme des scores pour chaque nom.

    >>> somme_scores([{"Alice": 5}, {"Bob": 3}, {"Alice": 2}, {"Bob": 7}])
    {'Alice': 7, 'Bob': 10}
    >>> somme_scores([])
    {}
    """
    resultat = {}
    for d in liste_dicts:
        for nom, score in d.items():
            resultat[nom] = resultat.get(nom, 0) + score
    return resultat

def filtre_tuple(t, seuil):
    """
    Renvoie un tuple avec les valeurs supérieures au seuil.

    >>> filtre_tuple((1, 5, 8, 2, 10), 5)
    (8, 10)
    >>> filtre_tuple((0, -1, -5), 0)
    ()
    """
    return tuple(x for x in t if x > seuil)


def inverse_dict(d):
    """
    Inverse un dictionnaire (clé <-> valeur).

    >>> inverse_dict({"a": 1, "b": 2, "c": 3})
    {1: 'a', 2: 'b', 3: 'c'}
    """
    return {v: k for k, v in d.items()}

def compte_mots(phrase):
    """
    Renvoie un dictionnaire avec les fréquences de chaque mot.

    >>> compte_mots("Le chat dort et le chien dort")
    {'le': 2, 'chat': 1, 'dort': 2, 'et': 1, 'chien': 1}
    >>> compte_mots("Python python PYTHON")
    {'python': 3}
    """
    mots = phrase.lower().split(' ')
    d = {}
    for mot in mots:
        d[mot] = d.get(mot, 0) + 1
    return d

def paires_consecutives(liste):
    """
    Renvoie les paires d'éléments consécutifs dans la liste.
    param : liste
    return : liste
    >>> paires_consecutives([1, 2, 3, 4])
    [(1, 2), (2, 3), (3, 4)]
    >>> paires_consecutives([7])
    []
    """
    return [(liste[i], liste[i+1]) for i in range(len(liste)-1)]

def cles_max(d):
    """
    Renvoie une liste des clés ayant la valeur maximale.
    para

    >>> cles_max({"a": 3, "b": 7, "c": 7, "d": 2})
    ['b', 'c']
    >>> cles_max({"x": 1})
    ['x']
    """
    if not d:
        return []
    max_val = max(d.values())
    return [k for k, v in d.items() if v == max_val]
    

if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)