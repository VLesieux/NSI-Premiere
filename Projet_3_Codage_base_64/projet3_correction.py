def conversion_binaire_decimal(mot_binaire):
    """
    Renvoie la valeur dÃ©cimale d'un mot binaire
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

def get_in_dictionary_methode1(sixtet):
    """
    Renvoie la clÃ© du dictionnaire Ã  partir du sixtet
    param : str
    return : str
    >>> get_in_dictionary_methode1('000001')
    'B'
    """
    for cle, valeur in equivalence.items():
        if valeur==sixtet:
            return cle

def get_in_dictionary_methode2(sixtet):
    """
    Renvoie la clÃ© du dictionnaire Ã  partir du sixtet
    param : str
    return : str
    >>> get_in_dictionary_methode2('000001')
    'B'
    """
    return lettres[conversion_binaire_decimal(sixtet)]

def sequence_binaire(n_uplet):
    """
    Renvoie un mot binaire Ã  partir d'un tuple d'octet
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
    convertit le tuple d'octets en une chaÃ®ne de symboles en utilisant le dÃ©coupage (slice)    
    :param n_uplet:  tuple : une sÃ©quence d'octets
    :return: str : la chaÃ®ne de symboles de la base 64 reprÃ©sentant le tuple d'octets
    :CU: les entiers du tuple tous compris entre 0 et 255
    :Exemples:
    >>> to_base64_slice((18, 184, 156))
    'Eric'
    >>> to_base64_slice((18, 184))
    'Erg='
    >>> to_base64_slice((18,))
    'Eg=='
    '''
    sequence=sequence_binaire(n_uplet)
    code=""
    reste=len(sequence)%6
    if reste==0:
        n=len(sequence)//6
        for i in range(n):
            code=code+get_in_dictionary_methode2(sequence[i*6:i*6+6])
    if reste==2:
        sequence=sequence+"0000"
        n=len(sequence)//6
        for i in range(n):
            code=code+get_in_dictionary_methode2(sequence[i*6:i*6+6])
        code=code+"=="
    if reste==4:
        sequence=sequence+"00"
        n=len(sequence)//6
        for i in range(n):
            code=code+get_in_dictionary_methode2(sequence[i*6:i*6+6])
        code=code+"="
    return code
            
    
def recup_sextet(i,sequence):
    """
    >>> recup_sextet(0,"000101")
    '000101'
    >>> recup_sextet(1,"000111000101")
    '000111'    
    """
    return conversion_decimal_binaire_6bits((63<<6*i & conversion_binaire_decimal(sequence))>>6*i)
    



def to_base64_logique(n_uplet):
    '''
    convertit le tuple d'octets en une chaÃ®ne de symboles en utilisant l'opÃ©rateur logique & et le dÃ©calage des bits avec << ou >>
    :param n_uplet:  tuple : une sÃ©quence d'octets
    :return: str : la chaÃ®ne de symboles de la base 64 reprÃ©sentant le tuple d'octets
    :CU: les entiers du tuple tous compris entre 0 et 255
    :Exemples:
    >>> to_base64_logique((18, 184, 156))
    'Eric'
    >>> to_base64_logique((18, 184))
    'Erg='
    >>> to_base64_logique((18,))
    'Eg=='
    '''
    sequence=sequence_binaire(n_uplet)
    code=""
    reste=len(sequence)%6
    if reste==0:
        n=len(sequence)//6
        for i in range(n):
            code=get_in_dictionary_methode2(recup_sextet(i,sequence))+code
    if reste==2:
        sequence=sequence+"0000"
        n=len(sequence)//6
        for i in range(n):
            code=get_in_dictionary_methode2(recup_sextet(i,sequence))+code
        code=code+"=="
    if reste==4:
        sequence=sequence+"00"
        n=len(sequence)//6
        for i in range(n):
            code=get_in_dictionary_methode2(recup_sextet(i,sequence))+code
        code=code+"="
    return code



# 
# 
def from_base64(b64_string):
    '''
    convertit une chaÃ®ne de symboles en un tuple d'octets en utilisant l'opÃ©rateur logique & et le dÃ©calage des bits avec << ou >>
    :param : b64_string: (str) une chaÃ®ne de symboles de la base 64
    :return: (tuple) un tuple d'octets dont b64_string est la reprÃ©sentation en base 64
    :CU: les caractÃ¨res de b64_string sont dans la table ou le symbole =
    :Exemple:
    >>> from_base64('Eric')
    (18, 184, 156)
    >>> from_base64('Erg=')
    (18, 184)
    >>> from_base64('Eg==')
    (18,)
    '''
    sequence=""
    for caractere in b64_string:
        if caractere=='=':
            sequence=sequence[0:-2]
        else:
            sequence=sequence+equivalence[caractere]
    octets=[]
    n=len(sequence)//8
    for i in range(n):
        octets.append(conversion_binaire_decimal(sequence[i*8:i*8+8]))
    return tuple(octets)
    
def recup_octet(i,sequence):
    """
    >>> recup_octet(0,"00000101")
    '00000101'
    >>> recup_octet(1,"0000000111000101")
    '00000001'    
    """
    return conversion_decimal_binaire_8bits((255<<8*i & conversion_binaire_decimal(sequence))>>8*i)            

def from_base64_logique(b64_string):
    '''
    convertit une chaÃ®ne de symboles en un tuple d'octets en utilisant l'opÃ©rateur logique & et le dÃ©calage des bits avec << ou >>
    :param : b64_string: (str) une chaÃ®ne de symboles de la base 64
    :return: (tuple) un tuple d'octets dont b64_string est la reprÃ©sentation en base 64
    :CU: les caractÃ¨res de b64_string sont dans la table ou le symbole =
    :Exemple:
    >>> from_base64_logique('Eric')
    (18, 184, 156)
    >>> from_base64_logique('Erg=')
    (18, 184)
    >>> from_base64_logique('Eg==')
    (18,)
    '''
    sequence=""
    for caractere in b64_string:
        if caractere=='=':
            sequence=sequence[0:-2]
        else:
            sequence=sequence+equivalence[caractere]
    octets=[]
    n=len(sequence)//8
    for i in range(n):
        octets.append(conversion_binaire_decimal(recup_octet(i,sequence)))
    octets=octets[::-1]
    return tuple(octets)
        
















if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)