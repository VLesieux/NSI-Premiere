def conversion_binaire_decimal(mot_binaire):
    """
    donne la valeur décimale d'un mot binaire
    param : str
    return : int
    >>> conversion_binaire_decimal("00101")
    5
    """
    code=mot_binaire[::-1]
    decimal=0
    for i in range(len(code)):
        decimal+=int(code[i])*2**i
    return decimal

def conversion_decimal_binaire_6bits(dec):
    """
    écrit un nombre décimal sur 6 bits
    param : int
    return : str
    >>> conversion_decimal_binaire_6bits(3)
    '000011'
    """
    if dec==0:
        return "000000"
    b=""
    while dec!=0:
        r=dec%2
        dec=dec//2
        b=str(r)+b#on ajoute le reste à la chaîne
    b="0"*(6-len(b))+b  
    return b

def conversion_decimal_binaire_8bits(dec):
    """
    écrit un nombre décimal sur 6 bits
    param : int
    return : str
    >>> conversion_decimal_binaire_8bits(3)
    '00000011'
    """
    if dec==0:
        return "00000000"
    b=""
    while dec!=0:
        r=dec%2
        dec=dec//2
        b=str(r)+b#on ajoute le reste à la chaîne
    b="0"*(8-len(b))+b  
    return b


lettres=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]

equivalence={lettres[i]:conversion_decimal_binaire_6bits(i) for i in range(len(lettres))}


def get_in_dictionary(sixtet):
    """
    renvoie le caractère associé au sixtet
    param : str
    return : str
    >>> get_in_dictionary('000001')
    'B'
    """
    for cle,val in equivalence.items():
        if val==sixtet:
            return cle

def sequence_binaire(n_uplet):
    """
    renvoie une sequence binaire
    param : tuple
    return : str
    >>> sequence_binaire((105,86,66))
    '011010010101011001000010'
    """
    code=""
    for decimal in n_uplet:
        code+=conversion_decimal_binaire_8bits(decimal)
    return code

def to_base64_slice(n_uplet):
    '''
    convertit le tuple d'octets en une chaîne de symboles
    :param n_uplet:  tuple : une séquence d'octets
    :return: str : la chaîne de symboles de la base 64 représentant le tuple d'octets
    :CU: les entiers du tuple tous compris entre 0 et 255
    :Exemples:
    >>> to_base64_slice((18, 184, 156))
    'Eric'
    >>> to_base64_slice((18, 184))
    'Erg='
    >>> to_base64_slice((18,))
    'Eg=='
    '''
    code=sequence_binaire(n_uplet)
    n=len(code)//6
    reste=len(code)%6
    resultat=""
    if reste==4:
        code=code+"00"
        n=len(code)//6
        for i in range(n):
            partie=code[i*6:i*6+6]
            resultat+=get_in_dictionary(partie)       
        resultat=resultat+"="
    if reste==2:
        code=code+"0000"
        n=len(code)//6
        for i in range(n):
            partie=code[i*6:i*6+6]
            resultat+=get_in_dictionary(partie)       
        resultat=resultat+"==" 
    if reste==0:
        for i in range(n):
            partie=code[i*6:i*6+6]
            resultat+=get_in_dictionary(partie)        
    return resultat
        
def to_base64(n_uplet):
    '''
    convertit le tuple d'octets en une chaîne de symboles
    :param n_uplet:  tuple : une séquence d'octets
    :return: str : la chaîne de symboles de la base 64 représentant le tuple d'octets
    :CU: les entiers du tuple tous compris entre 0 et 255
    :Exemples:
    >>> to_base64((18, 184, 156))
    'Eric'
    >>> to_base64((18, 184))
    'Erg='
    >>> to_base64((18,))
    'Eg=='
    '''    
    code=sequence_binaire(n_uplet)
    reste=len(code)%6
    resultat=""
    if reste==4:
        code=code+"00"
        n=len(code)//6
        for i in range(n):
            partie=conversion_decimal_binaire_6bits((conversion_binaire_decimal(code) & (63<<6*(n-1-i)))>>6*(n-1-i))
            resultat+=get_in_dictionary(partie)       
        resultat=resultat+"="
    if reste==2:
        code=code+"0000"
        n=len(code)//6
        for i in range(n):
            partie=conversion_decimal_binaire_6bits((conversion_binaire_decimal(code) & (63<<6*(n-1-i)))>>6*(n-1-i))
            resultat+=get_in_dictionary(partie)       
        resultat=resultat+"==" 
    if reste==0:
        n=len(code)//6
        for i in range(n):
            partie=conversion_decimal_binaire_6bits((conversion_binaire_decimal(code) & (63<<6*(n-1-i)))>>6*(n-1-i))
            resultat+=get_in_dictionary(partie)        
    return resultat    


def from_base64(b64_string):
    '''
    convertit une chaîne de symboles en un tuple d'octets    
    :param : b64_string: (str) une chaîne de symboles de la base 64
    :return: (tuple) un tuple d'octets dont b64_string est la représentation en base 64
    :CU: les caractères de b64_string sont dans la table ou le symbole =
    >>> from_base64('Eric')
    (18, 184, 156)
    >>> from_base64('Erg=')
    (18, 184)
    >>> from_base64('Eg==')
    (18,)
    '''
    code=""
    for caractere in b64_string:
        if caractere!="=":
            code=code+equivalence[caractere]
        else:
            code=code[0:-2]
    n=len(code)//8
    liste=[]
    for i in range(n):
        partie=(conversion_binaire_decimal(code) & (255<<8*(n-1-i)))>>8*(n-1-i)
        liste.append(partie)
    return tuple(liste)
        



    
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)