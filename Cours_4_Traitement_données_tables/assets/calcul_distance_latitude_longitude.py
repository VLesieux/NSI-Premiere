import math

R=6378137
PI=math.pi

def conversion_degre_radian(angle):
    """
    Convertit un angle exprimé en degré en radian
    >>> conversion_degre_radian(180)
    3.141592653589793
    """
    
    return angle*PI/180

def calcul_distance_a_vol_d_oiseau(A,B):
    """
    Calcul la distance entre deux points A et B à partir de leurs coordonnées géographiques
    param : A : tuple
    param : B : tuple
    return : float
    >>> calcul_distance_a_vol_d_oiseau((48.858370,2.294481),(48.873792,2.295028))
    1717.236416494379
    """
    dλ=conversion_degre_radian(B[1])-conversion_degre_radian(A[1])
    S=math.acos(math.sin(conversion_degre_radian(A[0]))*math.sin(conversion_degre_radian(B[0]))+math.cos(conversion_degre_radian(A[0]))*math.cos(conversion_degre_radian(B[0]))*math.cos(dλ))
    d=6378137*S
    return d

def a_paris(A):
    liste=A.split(',')
    couple=(float(liste[0]),float(liste[1]))
    return calcul_distance_a_vol_d_oiseau(couple,(48.856614,2.3522219))


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)