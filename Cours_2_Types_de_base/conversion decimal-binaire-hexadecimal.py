def conversion_decimal_binaire(n):
    """
    Donne la représentation binaire du nombre entier décimal n
    param : n : int
    return : str
    >>> conversion_decimal_binaire(18)
    '10010'
    >>> conversion_decimal_binaire(141)
    '10001101'
    """
    resultat=""
    while n>0:
        resultat=str(n%2)+resultat
        n=n//2
    return resultat
        
def conversion_decimal_binaire_complet(n):
    """
    Donne la représentation binaire du nombre entier décimal n
    param : n : int
    return : str
    >>> conversion_decimal_binaire_complet(18)
    '00010010'
    >>> conversion_decimal_binaire_complet(141)
    '10001101'
    """
    resultat=""
    while n>0:
        resultat=str(n%2)+resultat
        n=n//2
    if len(resultat)%8>0:
        resultat='0'*(8-len(resultat)%8)+resultat
    return resultat
#nombre=input("Quel est le nombre dont vous voulez connaître la représentation binaire ? ")
#
#print("La représentation binaire de",nombre,"est : ",conversion_decimal_binaire(int(nombre)))


def conversion_binaire_decimal(mot):
    """
    Donne la représentation binaire du nombre entier décimal n
    param : n : int
    return : str
    >>> conversion_binaire_decimal('110011')
    51
    >>> conversion_binaire_decimal('1010101')
    85
    """
    resultat=0
    for i in range(len(mot)):
        resultat+=int(mot[-1-i])*2**i
    return resultat

def conversion_decimal_hexadecimal(n):
    """
    Donne la représentation hexadécimal du nombre entier décimal n
    param : n : int
    return : str
    >>> conversion_decimal_hexadecimal(18)
    '12'
    >>> conversion_decimal_hexadecimal(141)
    '8d'
    """
    resultat=""
    liste_remplaçant=["a","b","c","d","e"]
    while n>0:
        if n%16>=10:
            resultat=liste_remplaçant[n%16-10]+resultat
        else:
            resultat=str(n%16)+resultat        
        n=n//16
    return resultat


def conversion_hexadecimal_decimal(mot):
    """
    Donne la représentation décimale du mot hexadécimal
    param : mot : str
    return : int
    >>> conversion_hexadecimal_decimal('ae')
    174
    >>> conversion_hexadecimal_decimal('34a')
    842
    """
    resultat=0
    liste_remplaçant=["a","b","c","d","e"]
    for i in range(len(mot)):
        if mot[-1-i] in liste_remplaçant:
            resultat+=(liste_remplaçant.index(mot[-1-i])+10)*16**i
        else:
            resultat+=int(mot[-1-i])*16**i
    return resultat

def conversion_binaire_hexadecimal(mot):
    """
    Donne la représentation hexadécimale d'un mot binaire
    param: str
    return : str
    >>> conversion_binaire_hexadecimal('101101001')
    '169'
    >>> conversion_binaire_hexadecimal('110111')
    '37'
    """
    if len(mot)%4>0:
        mot='0'*(4-len(mot)%4)+mot
    p=len(mot)//4
    resultat=''
    for i in range(p):
        resultat=resultat+conversion_decimal_hexadecimal(conversion_binaire_decimal(mot[4*i:4*i+4]))
    return resultat

def conversion_hexadecimal_binaire(mot):
    """
    Donne la représentation binaire d'un mot hexadécimale
    param: str
    return : str
    >>> conversion_hexadecimal_binaire('169')
    '101101001'
    >>> conversion_hexadecimal_binaire('37')
    '110111'
    """
    resultat=conversion_decimal_binaire(conversion_hexadecimal_decimal(mot))
    return resultat


def encodage_texte_ascII_binaire(texte):
    """
    Code un texte ascII en binaire
    param : texte : str
    return : str
    >>> encodage_texte_ascII_binaire("vive la nsi !")
    '01110110011010010111011001100101001000000110110001100001001000000110111001110011011010010010000000100001'
    """
    resultat=""
    for caractere in texte:
        resultat+=conversion_decimal_binaire_complet(ord(caractere))
    return resultat
        
def decodage_binaire_texte_ascII(code_binaire):
    """
    Décode Code un texte ascII en binaire
    param : texte : str
    return : str
    >>> decodage_binaire_texte_ascII('01110110011010010111011001100101001000000110110001100001001000000110111001110011011010010010000000100001')
    'vive la nsi !'
    """
    resultat=''
    for i in range(len(code_binaire)//8):
        resultat+=chr(conversion_binaire_decimal(code_binaire[i*8:i*8+8]))   
    return resultat



if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True) 