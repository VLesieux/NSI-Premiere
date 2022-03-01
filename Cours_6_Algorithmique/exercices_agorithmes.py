debuts=[8,12,9,14,11]

fins=[13,17,11,16,12]


def prochaine(horaires_debut,horaires_fin,h):
    """
    Renvoie l'indice de la séance qui commence après h
    et qui se termine le plus tôt dans la journée
    param : horaires_debut : list
    param : horaires_fin : list
    return : int
    >>> prochaine(debuts,fins,11)
    4
    """
    liste=[]
    for i in range(len(horaires_debut)):
        if (horaires_debut[i]-h)>=0:
            liste.append((i,horaires_fin[i]))
    if len(liste)>0:
        minimum=liste[0][1]
        indice=0
        for j in range(len(liste)):
            if liste[j][1]<=minimum:
                minimum=liste[j][1]
                indice=j        
        return liste[indice][0]
    else:
        return None
    
def selection(debut,fin,horaires_debut,horaires_fin):
    """
    Renvoie les indices de activités selon l'algorithme glouton
    param : debut : int
    param : fin : int
    return : list
    >>> selection(8,16,debuts,fins)
    [2, 4, 3]
    """
    resultat=[]
    h=debut
    while not prochaine(horaires_debut,horaires_fin,h)==None and fins[prochaine(horaires_debut,horaires_fin,h)]<=fin:
        resultat.append(prochaine(horaires_debut,horaires_fin,h))
        h=fins[prochaine(horaires_debut,horaires_fin,h)]
    return resultat
    
        
        
    
    
prochaine(debuts,fins,8)












if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)