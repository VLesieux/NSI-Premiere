debuts=[8,12,9,14,11]
fins=[13,17,11,16,12]
activites=['A','B','C','D','E']

def prochaine(horaires_debut,horaires_fin,h):
    """
    Renvoie l'indice de la séance qui commence après h et qui se termine le plus tôt dans la journée
    param : horaires_debut : list
    param : horaires_fin : list
    return : int
    >>> prochaine(debuts,fins,12)
    3
    >>> prochaine(debuts,fins,17)
    'Impossible'
    """
    resultat=[i for i in range(len(activites)) if horaires_debut[i]>=h]
    if len(resultat)==1:
        return resultat[0]
    elif len(resultat)>1:
        choix=horaires_fin.index(min([horaires_fin[i] for i in resultat]))
        return choix
    else:
        return 'Impossible'
    
def selection(debut,fin,horaires_debut,horaires_fin):
    """
    Renvoie la liste des noms des activités selon l'algorithme glouton
    param : debut : int
    param : fin : int
    return : list
    >>> selection(8,18,debuts,fins)
    ['C', 'E', 'D']
    >>> selection(11,16,debuts,fins)
    ['E', 'D']
    """
    resultat=[]
    h=debut
    while prochaine(horaires_debut,horaires_fin,h) !='Impossible' and horaires_fin[prochaine(horaires_debut,horaires_fin,h)]<=fin:
        resultat.append(activites[prochaine(horaires_debut,horaires_fin,h)])
        h=horaires_fin[prochaine(horaires_debut,horaires_fin,h)]
    return resultat

















if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)