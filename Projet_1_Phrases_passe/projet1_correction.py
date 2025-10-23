from liste_7776_mots import LISTE_MOTS


################ A faire n°1 ###################
# >>> type(LISTE_MOTS)
# <class 'tuple'>

################ A faire n°2 ###################
# >>> len(LISTE_MOTS)
# 7776
################ A faire n°3 ###################
# >>> all([type(element)==str for element in LISTE_MOTS])
# True
accents=["é","ê","à","û","ô","î","â","ù"]
#all([all([element not in accents for element in LISTE_MOTS[i]])for i in range (7776)])

def est_unique(mot,n_uplet):
    """
    Renvoie True si mot est présent une et une seule fois dans n_uplet et False autrement
    param: mot : str
    param: n_uplet: tuple
    return: bool
    >>> est_unique("pas",("pas","pas","pois"))
    False
    >>> est_unique("pas",("pas","pis","pois"))
    True
    """
    nombre_d_apparition=0
    for element in n_uplet:
        if element==mot:
            nombre_d_apparition+=1
    return nombre_d_apparition==1
# >>> all([est_unique(mot,LISTE_MOTS) for mot in LISTE_MOTS])           
##############Afaire#n#4#########

max([len(element) for element in LISTE_MOTS])
min([len(element) for element in LISTE_MOTS])
# >>> max([len(element) for element in LISTE_MOTS])
# 9
# >>> min([len(element) for element in LISTE_MOTS])
# 4

##############Afaire#n#5#########

def description(n_uplet):
    print("0 : "+n_uplet[0]+"\n"
          "7775 : "+n_uplet[-1]+"\n"
          "2094 : "+n_uplet[2094])
    
    
##############Afaire#n#6#########

def en_nombre(cinq_lancers):
    """
    renvoie l'indice de position du mot correspondant
    param : cinq_lancers
    return : int
    >>> en_nombre('11111')
    0
    >>> en_nombre('66666')
    7775
    >>> en_nombre('24521')
    2094

    """
    nombre = int(cinq_lancers)-11111
    return int(str(nombre), 6)

def conversion_dans_base(n,b):
    """
    convertit un entier n en base b
    param : n: int
    param : b : int
    return : string
    exemples:
    >>> conversion_dans_base(3,2)
    '11'
    >>> conversion_dans_base(175,5)
    '1200'
    """
    if n==0:
        return "0"
    resultat=""
    while n!=0:
        r=n%b
        n=n//b
        resultat=str(r)+resultat#on ajoute le reste à la chaîne à gauche de celle-ci
    return resultat
##############Afaire#n#7#########
def lancer_de_des(dec):
    """
    renvoie la chaine de caracteres associe aux 5 lance de dés
    >>> lancer_de_des(7768)
    '66655'
    """
    conversion = int(conversion_dans_base(dec,6))
    return str(conversion + 11111)
    
##############Afaire#n#8#########
def donne_mot(sequence):
    """
    Renvoie le mot associé à la séquence
    >>> donne_mot('11111')
    'montes'
    >>> donne_mot('66666')
    'tour'
    >>> donne_mot('24521')
    'morigener'
    """
    return LISTE_MOTS[en_nombre(sequence)]

import random

##############Afaire#n#9#########
def genere_n_sequences_alea(n):
    """
    renvoie une chaîne de caractères constituée de n séquences de 5 lancers de dés.
    """
    chaine=''
    for i in range (5*n):
        chaine+=str(randint(1,6))
    return chaine

##############Afaire#n#10#########
def genere_phrase_passe(sequences_de_des):
    """
    Renvoie mots associés à chaques séquences
    >>> genere_phrase_passe('111116666624521')
    'montes-tour-morigener'
    >>> genere_phrase_passe('1141116666624521')
    'la longueur de la chaîne doit être un multiple de 5'
    """
    resultat=''
    if len(sequences_de_des)%5==0:
        nombre_sequences=len(sequences_de_des)//5
        for i in range (nombre_sequences):
            resultat+="-"+donne_mot(sequences_de_des[i*5:i*5+5])
        return resultat[1:len(resultat)]
    else :
        return 'la longueur de la chaîne doit être un multiple de 5'
        
    
    
    







if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
