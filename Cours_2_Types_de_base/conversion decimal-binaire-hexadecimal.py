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


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True) 