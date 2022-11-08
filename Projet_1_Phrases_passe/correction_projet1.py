from liste_7776_mots import LISTE_MOTS

import random

#À faire n°1************************************************
#>>> type(LISTE_MOTS)
#<class 'tuple'>

#À faire n°2************************************************
#>>> len(LISTE_MOTS)
#7776

#À faire n°3************************************************
#
#Affirmation n°1
#>>> all(type(element)==str for element in LISTE_MOTS)
#True

#Affirmation n°2
#>>> all(all(caractere.lower() not in accents for caractere in element) for element in LISTE_MOTS)
#True

#Affirmation n°3
def est_unique(mot,n_uplet):
    """
    Renvoie True si mot est présent une seule fois dans le n_uplet, False sinon
    param : mot : str
    param : n_uplet : tuple
    return : bool
    >>> est_unique("pas",("pas","pas","pois"))
    False
    >>> est_unique("pas",("pas","pis","pois"))
    True
    """
    compteur=0
    for element in n_uplet:
        if mot==element:
            compteur+=1
    return compteur==1

#>>> all([est_unique(mot,LISTE_MOTS) for mot in LISTE_MOTS])
#True


#À faire n°4************************************************
#>>> min(len(mot) for mot in LISTE_MOTS)
#4
#>>> max(len(mot) for mot in LISTE_MOTS)
#9

#À faire n°5************************************************

def description(n_uplet):
    print(n_uplet[0]+"\n")
    print(n_uplet[7775]+"\n")
    print(n_uplet[2094]+"\n")


#À faire n°6************************************************

def en_nombre(sequence):
    """
    Transforme une séquence de 5 lancers de dé en un nombre avec un décalage de 1
    param : sequence : str
    return : int
    >>> en_nombre('11111')
    0
    >>> en_nombre('66666')
    7775
    >>> en_nombre('24521')
    2094
    """
    valeur=0
    for i in range(5):
        valeur+=(int(sequence[-1-i])-1)*(6**i)#le (-1-i) s'explique par la lecture de droite à gauche    
    return valeur


#À faire n°7************************************************

def conversion_decimal_binaire(dec):
    """
    Envoie le code binaire correspondant à dec
    param : dec : int
    return : str
    >>> conversion_decimal_binaire(145)
    '10010001'
    """
    code=''
    while dec!=0:
        code=str(dec%2)+code
        dec=dec//2
    return code


def lancer_de_des(dec):
    """
    Envoie la séquence de dé correspondante à dec
    param : dec : int
    return : str
    >>> lancer_de_des(7768)
    '66655'
    """
    code=''
    while dec!=0:
        code=str(dec%6+1)+code
        dec=dec//6
    return code
   

#À faire n°8************************************************

def donne_mot(sequence):
    """
    Envoie le mot correspondant à la séquence
    param : sequence : str
    return : str
    >>> donne_mot('11111')
    'montes'
    >>> donne_mot('66666')
    'tour'
    >>> donne_mot('24521')
    'morigener'
    """
    return LISTE_MOTS[en_nombre(sequence)]


#À faire n°9************************************************

def genere_n_sequences_alea(n):
    """
    Renvoie une chaîne de caractères constituée de n séquences de 5 lancers de dé
    """
    sequence=""
    for i in range(5*n):
        sequence=sequence+str(random.randint(1,5))
    return sequence

#À faire n°10************************************************
    
def genere_phrase_passe(sequence):
    """
    Renvoie les mots correspondants à la sequence
    param : str
    return : str
    >>> genere_phrase_passe('111116666624521')
    'montes-tour-morigener'
    >>> genere_phrase_passe('1141116666624521')
    la longueur de la chaîne doit être un multiple de 5
    """
    code=""
    if len(sequence)%5==0:
        n=len(sequence)//5
        for i in range(1,n+1):
            code=code+'-'+donne_mot(sequence[0*i:5*i])
        code=code[1:len(code)]#retirer le premier tiret
        return code
    else:
        print("la longueur de la chaîne doit être un multiple de 5")

#À faire n°11************************************************
        
caracteres_non_accentues=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
  
def est_lettre(caractere):
    """
    Renvoie True si le caractère est non accentué, False sinon
    param : caractere : str
    return : bool
    >>> est_lettre('a')
    True
    >>> est_lettre('B')
    True
    >>> est_lettre('1')
    False
    """
    return (caractere in caracteres_non_accentues or caractere.lower() in caracteres_non_accentues)

#À faire n°12************************************************

def perturbe_chaine(chaine):
    """
    Renvoie la chaîne perturbée avec une chance sur deux minuscules ou minuscule
    """
    resultat=""
    for caractere in chaine:
        if random.randint(0,1)==0:
            resultat+=caractere
        else:
            resultat+=caractere.upper()
    return resultat

#À faire n°13************************************************
def genere_phrase_passe2(sequence):
    """
    Renvoie les mots correspondants à la sequence
    param : str
    return : str
    >>> genere_phrase_passe('1141116666624521')
    la longueur de la chaîne doit être un multiple de 5   
    """
    code=""
    if len(sequence)%5==0:
        n=len(sequence)//5
        for i in range(1,n+1):
            code=code+'-'+donne_mot(sequence[0*i:5*i])
        code=code[1:len(code)]
        return perturbe_chaine(code)
    else:
        print("la longueur de la chaîne doit être un multiple de 5")

#À faire n°14************************************************
EQUIVALENTS = {
    'a' : '@',
    'b' : '8',
    'e' : '3',
    'i' : '1',
    'o' : '0'
}

def perturbe_chaine2(s):
    """
    Renvoie la chaîne perturbée avec une chance sur deux minuscules ou minuscule
    et utilisation de caractères particuliers
    """
    resultat=""
    for caractere in s:
        if random.randint(0,1)==0:
            if caractere in EQUIVALENTS:
                if random.randint(0,1)==0:
                    resultat+=caractere
                else:
                    resultat+=EQUIVALENTS[caractere]
            else: resultat+=caractere
        else:
            resultat+=caractere.upper()
    return resultat

#À faire n°15************************************************
def genere_phrase_passe3(sequence):
    """
    Renvoie les mots correspondants à la sequence
    param : str
    return : str
    >>> genere_phrase_passe('1141116666624521')
    la longueur de la chaîne doit être un multiple de 5   
    """
    code=""
    if len(sequence)%5==0:
        n=len(sequence)//5
        for i in range(1,n+1):
            code=code+'-'+donne_mot(sequence[0*i:5*i])
        code=code[1:len(code)]
        return perturbe_chaine2(code)
    else:
        print("la longueur de la chaîne doit être un multiple de 5")


if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)