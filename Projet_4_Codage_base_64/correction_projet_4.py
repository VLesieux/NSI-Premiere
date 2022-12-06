def conversion_binaire_decimal(mot_binaire):
    """
    Renvoie la valeur décimale d'un mot binaire
    param : mot_binaire
    return : int
    >>> conversion_binaire_decimal("00101")
    5
    """
    resultat=0
    n=len(mot_binaire)
    for i in range(n):
        resultat+=int(mot_binaire[n-i-1])*2**i
    return resultat


def conversion_decimal_binaire_6bits(nombre):
    """
    Renvoie le code binaire sur 6 bits
    param : dec : int
    return : str
    >>> conversion_decimal_binaire_6bits(3)
    '000011'    
    """
    resultat=""
    while nombre !=0:
        resultat=str(nombre%2)+resultat
        nombre=nombre//2
    resultat="0"*(6-len(resultat))+resultat
    return resultat
        
        
def conversion_decimal_binaire_8bits(nombre):
    """
    Renvoie le code binaire sur 8 bits
    param : dec : int
    return : str
    >>> conversion_decimal_binaire_8bits(3)
    '00000011'    
    """
    resultat=""
    while nombre !=0:
        resultat=str(nombre%2)+resultat
        nombre=nombre//2
    resultat="0"*(8-len(resultat))+resultat
    return resultat

lettres=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]

equivalence={lettres[i]:conversion_decimal_binaire_6bits(i) for i in range(len(lettres))}

def get_in_dictionary(sixtet):
    """
    Renvoie la clé du dictionnaire à partir du sixtet
    param : str
    return : str
    >>> get_in_dictionary('000001')
    'B'
    """
    for cle, valeur in equivalence.items():
        if valeur==sixtet:
            return cle

def sequence_binaire(n_uplet):
    """
    Renvoie un mot binaire à partir d'un tuple d'octet
    param : n_uplet : tuple
    return : str
    >>> sequence_binaire((105,86,66))
    '011010010101011001000010'
    """
    resultat=""
    for nombre in n_uplet:
        resultat+=conversion_decimal_binaire_8bits(nombre)
    return resultat
        

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
    resultat=""
    sequence=sequence_binaire(n_uplet)
    if len(sequence)%6==0:
        n=len(sequence)//6
        for i in range(n):
            resultat+=get_in_dictionary(sequence[i*6:i*6+6])
    if len(sequence)%6==4:
        sequence=sequence+"00"
        n=len(sequence)//6
        for i in range(n):
            resultat+=get_in_dictionary(sequence[i*6:i*6+6])
        resultat=resultat+"="
    if len(sequence)%6==2:
        sequence=sequence+"0000"
        n=len(sequence)//6
        for i in range(n):
            resultat+=get_in_dictionary(sequence[i*6:i*6+6])
        resultat=resultat+"=="          
    return resultat
        
def to_base64_logique(n_uplet):
    '''
    convertit le tuple d'octets en une chaîne de symboles    
    :param n_uplet:  tuple : une séquence d'octets
    :return: str : la chaîne de symboles de la base 64 représentant le tuple d'octets
    :CU: les entiers du tuple tous compris entre 0 et 255
    :Exemples:
    >>> to_base64_logique((18, 184, 156))
    'Eric'
    >>> to_base64_logique((18, 184))
    'Erg='
    >>> to_base64_logique((18,))
    'Eg=='
    '''
    resultat=""
    sequence=sequence_binaire(n_uplet)
    if len(sequence)%6==0:
        n=len(sequence)//6
        for i in range(n):
            resultat=get_in_dictionary(conversion_decimal_binaire_6bits((conversion_binaire_decimal(sequence) & (63<<6*i))>>6*i))+resultat
    if len(sequence)%6==4:
        sequence=sequence+"00"
        n=len(sequence)//6
        for i in range(n):
            resultat=get_in_dictionary(conversion_decimal_binaire_6bits((conversion_binaire_decimal(sequence) & (63<<6*i))>>6*i))+resultat
        resultat=resultat+"="
    if len(sequence)%6==2:
        sequence=sequence+"0000"
        n=len(sequence)//6
        for i in range(n):
            resultat=get_in_dictionary(conversion_decimal_binaire_6bits((conversion_binaire_decimal(sequence) & (63<<6*i))>>6*i))+resultat
        resultat=resultat+"=="          
    return resultat    


def from_base64(b64_string):
    '''
    convertit une chaîne de symboles en un tuple d'octets
    :param : b64_string: (str) une chaîne de symboles de la base 64
    :return: (tuple) un tuple d'octets dont b64_string est la représentation en base 64
    :CU: les caractères de b64_string sont dans la table ou le symbole =
    :Exemple:
    >>> from_base64('Eric')
    (18, 184, 156)
    >>> from_base64('Erg=')
    (18, 184)
    >>> from_base64('Eg==')
    (18,)
    '''
    liste=[]
    sequence=''
    for caractere in b64_string:
        if caractere=='=':
            sequence=sequence[0:-2]
        else:
            sequence+=equivalence[caractere]   
    n=len(sequence)//8
    for i in range(n):
        prelevement=(conversion_binaire_decimal(sequence) & (255<<8*i))>>8*i#conversion de droite à gauche
        liste.append(prelevement)
    liste.reverse()
    return tuple(liste)
    
















if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)