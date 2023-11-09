from liste_7776_mots import LISTE_MOTS
#print("LISTE_MOTS est de type tuple ",type(LISTE_MOTS))
#print("Nombre de mots dans LISTE_MOTS ",len(LISTE_MOTS))
#print("Tous les éléments sont des chaînes :",all(type(mot)==str for mot in LISTE_MOTS))
#accents=["é","ê","à","û","ô","î","â","ù"]
#print("Les mots ne contiennent pas de caractères accentués :",all((all(caractere.lower() not in accents for caractere in mot) for mot in LISTE_MOTS)))


def est_unique(mot,n_uplet):
    """
    Renvoie True si mot est present une seule fois dans n_uplet
    >>> est_unique("pas",("pas","pas","pois"))
    False
    >>> est_unique("pas",("pas","pis","pois"))
    True
    """
    compteur=0
    for composant in n_uplet:
        if composant==mot:
            compteur+=1
    if compteur>1:
        return False
    return True
    
#print("Les mots ne se trouvent qu'une seule fois dans la liste : ",all(est_unique(mot,LISTE_MOTS) for mot in LISTE_MOTS))    
#    
#
#print("nombre de caractères du mot le plus court :",min([len(mot) for mot in LISTE_MOTS]))
#
#print("nombre de caractères du mot le plus long :",max([len(mot) for mot in LISTE_MOTS]))


def description(n_uplet):
    """
    Imprime le premier mot de cet n_uplet, le dernier et celui d'indice 2094
    >>> description(LISTE_MOTS)
    0 : montes
    7775 : tour
    2094 : morigener    
    """
    chaine="0 : "+n_uplet[0]+"\n"+str(len(n_uplet)-1)+" : "+n_uplet[len(n_uplet)-1]+"\n"+"2094 : "+n_uplet[2094]
    print(chaine)


def en_nombre(sequence):
    """
    Renvoie le nombre associé à sequence
    param: sequence : str
    return : int
    >>> en_nombre('11111')
    0
    >>> en_nombre('66666')
    7775
    >>> en_nombre('24521')
    2094
    """
    resultat=0
    for indice in range(len(sequence)):
        resultat+=(int(sequence[indice])-1)*6**(len(sequence)-1-indice)
    return resultat


def conversion_dans_base(n,b):
    """
    Convertit n dans la base b
    param : n : int
    param : b : int
    return : str
    >>> conversion_dans_base(10,2)
    '1010'
    """
    resultat=""
    while n>0:
        resultat=str(n%b)+resultat
        n=n//b
    return resultat

def lancer_de_des(nombre):
    """
    Renvoie la séquence de dés
    param : int
    return : str
    >>> lancer_de_des(7768)
    '66655'                             
    """
    conversion=conversion_dans_base(nombre,6)
    resultat=""
    for caractere in conversion:
        resultat+=str(int(caractere)+1)
    return resultat

def donne_mot(sequence):
    """
    renvoie le mot correspondant à la séquence de dés
    param: sequence : str
    return: str
    >>> donne_mot('11111')
    'montes'
    >>> donne_mot('66666')
    'tour'
    >>> donne_mot('24521')
    'morigener'        
    """
    return LISTE_MOTS[en_nombre(sequence)]

import random

def genere_n_sequences_alea(n):
    """
    Renvoie n sequences de lancer de 5 dés
    param : n : int
    return : str
    """
    resultat=""
    for i in range(5*n):
        resultat+=str(random.randint(1,6))
    return resultat
        
def genere_phrase_passe(sequence):
    """
    Renvoie des mots séparés par des -
    param : sequence : str
    return : str
    >>> genere_phrase_passe('111116666624521')
    'montes-tour-morigener'
    >>> genere_phrase_passe('1141116666624521')
    'la longueur de la chaîne doit être un multiple de 5'   
    """
    if len(sequence)%5 !=0:
        return 'la longueur de la chaîne doit être un multiple de 5'
    n=len(sequence)//5
    resultat=''
    for i in range(n):
        resultat=resultat+'-'+donne_mot(sequence[5*i:5*i+5])
    return resultat[1:len(resultat)]
    

caracteres_non_accentues=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def est_lettre(caractere):
    """
    Renvoie True si le caractere est non accentué sinon False
    param : caractere: str
    return: bool
    >>> est_lettre('a')
    True
    >>> est_lettre('B')
    True
    >>> est_lettre('1')
    False    
    """
    return caractere.lower() in caracteres_non_accentues
    
def perturbe_chaine(chaine):
    """
    renvoie la chaîne obtenue en changeant aléatoirement ou pas (une chance sur deux)
    chacune des lettres de chaine en sa majuscule ou minuscule
    param : chaine :str
    return : str
    """
    resultat=''
    for caractere in chaine:
        if random.randint(0,1)==1:
            resultat+=caractere.upper()
        else:
            resultat+=caractere
    return resultat

def genere_phrase_passe2(sequence):
    """
    Renvoie des mots séparés par des -
    param : sequence : str
    return : str
    """
    if len(sequence)%5 !=0:
        return 'la longueur de la chaîne doit être un multiple de 5'
    n=len(sequence)//5
    resultat=''
    for i in range(n):
        resultat=resultat+'-'+perturbe_chaine(donne_mot(sequence[5*i:5*i+5]))
    return resultat[1:len(resultat)]

EQUIVALENTS = {
    'a' : '@',
    'b' : '8',
    'e' : '3',
    'i' : '1',
    'o' : '0'
}

def perturbe_chaine2(chaine):
    """
    renvoie la chaîne obtenue en changeant aléatoirement ou pas (une chance sur deux)
    chacune des lettres de chaine en sa majuscule ou minuscule
    param : chaine :str
    return : str
    """
    resultat=''
    for caractere in chaine:
        if random.randint(0,1)==1:
            resultat+=caractere.upper()
        else:
            if caractere in EQUIVALENTS:
                resultat+=EQUIVALENTS[caractere]
            else:
                resultat+=caractere
    return resultat


def genere_phrase_passe3(sequence):
    """
    Renvoie des mots séparés par des -
    param : sequence : str
    return : str
    """
    if len(sequence)%5 !=0:
        return 'la longueur de la chaîne doit être un multiple de 5'
    n=len(sequence)//5
    resultat=''
    for i in range(n):
        resultat=resultat+'-'+perturbe_chaine2(donne_mot(sequence[5*i:5*i+5]))
    return resultat[1:len(resultat)]

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)