
lettres=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]
equivalence={}

def conversion_binaire_decimal(mot_binaire):
    """
    Convertir un mot_binaire en décima
    Exemples:
    >>> conversion_binaire_decimal("00101")
    5
    """
    valeur=0
    mot_binaire_renverse=mot_binaire[::-1]
    for i in range(len(mot_binaire)):       
        if mot_binaire_renverse[i]=="1":
            valeur+=2**i
    return valeur
        
def conversion_decimal_binaire_6bits(dec):
    """
    Convertit un nombre décimal en binaire sur 6 bits
    param: dec : int
    return : str
    Exemples:
    >>> conversion_decimal_binaire_6bits(3)
    '000011'
    """
    resultat=""
    dividende=dec
    quotient=dividende//2
    reste=dividende%2
    resultat+=str(reste)
    while quotient>0:
        dividende=quotient
        quotient=dividende//2
        reste=dividende%2
        resultat+=str(reste)
    complet="0"*(6-len(resultat))
    return complet+resultat[::-1]

def conversion_decimal_binaire_8bits(dec):
    """
    Convertit un nombre décimal en binaire sur 8 bits
    param: dec : int
    return : str
    Exemples:
    >>> conversion_decimal_binaire_8bits(3)
    '00000011'
    """
    resultat=""
    dividende=dec
    quotient=dividende//2
    reste=dividende%2
    resultat+=str(reste)
    while quotient>0:
        dividende=quotient
        quotient=dividende//2
        reste=dividende%2
        resultat+=str(reste)
    complet="0"*(8-len(resultat))
    return complet+resultat[::-1]

for i in range(len(lettres)):
    equivalence[lettres[i]]=conversion_decimal_binaire_6bits(i)

def get_in_dictionary(sixtet):
    """
    renvoie le symbole associé au sixtet
    Exemple:
    >>> get_in_dictionary('000001')
    'B'
    """
    for cle,valeur in equivalence.items():
        if valeur==sixtet:
            return cle

def sequence_binaire(sequence_octets):
    """
    Réalise une séquence binaire à partir d'une séquence d'octets
    param: sequence_octets : tuple
    Exemples
    >>> sequence_binaire((105,86,66))
    '011010010101011001000010'
    """
    sequence=""
    for i in sequence_octets:
        sequence+=conversion_decimal_binaire_8bits(i)
    return sequence

def to_base64_slice(n_uplet):
    '''
    convertit le n_uplet d'octets en une chaîne constituée de symboles
    la méthode utilisée est la découpe (slice)
    :param triplet: (tuple ou list) une séquence d'octets
    :return: (str) la chaîne de symboles de la base 64 représentant le triplet d'octets
    :CU: les entiers de triplet tous compris entre 0 et 255
    :Exemple:
    
    >>> to_base64_slice((18, 184, 156))
    'Eric'
    >>> to_base64_slice((18, 184))
    'Erg='
    >>> to_base64_slice((18,))
    'Eg=='
    '''
    sequence=sequence_binaire(n_uplet)
    resultat=""
    reste=len(sequence)%6
    if reste>0:
        sequence+="0"*(6-reste)
    nombre_partage=len(sequence)//6
    for i in range(nombre_partage):
        resultat+=get_in_dictionary(sequence[6*i:6*(i+1)])
    if reste>0:
        resultat+="="*int((6-reste)/2)##indique le nombre de 0 ajouté 00 pour =
    return resultat

    
def to_base64_binaire(n_uplet):
    '''
    convertit le n_uplet d'octets en une chaîne constituée de symboles
    La méthode utilisée est le ET logique
    :param n_uplet: tuple
    :return: (str) la chaîne de symboles de la base 64 représentant le triplet d'octets
    :CU: les entiers de triplet tous compris entre 0 et 255
    :Exemple:
    
    >>> to_base64_binaire((18, 184, 156))
    'Eric'
    >>> to_base64_binaire((18, 184))
    'Erg='
    >>> to_base64_binaire((18,))
    'Eg=='
    '''
    sequence=sequence_binaire(n_uplet)
    reste=len(sequence)%6
    if reste>0:
        sequence+="0"*(6-reste)
    octet_decimal=conversion_binaire_decimal(sequence)
    n=0
    resultat=0
    code=""
    while (octet_decimal & (63<<n*6))>0:
        resultat=octet_decimal & (63<<n*6)
        resultat=resultat>>n*6
        code+=str(get_in_dictionary(conversion_decimal_binaire_6bits(resultat)))
        n+=1
    if reste>0:
        code=code[::-1]
        code+="="*int((6-reste)/2)
        return code
    return code[::-1]
  

def from_base64(b64_string):
    """
    Renvoie un tuple d'octets à partir d'une chaîne de caractère formée de symboles
    La méthode utilisée est le ET logique
    :param : (str)
    :return: (str) 
    :Exemple:
    >>> from_base64('Eric')
    (18, 184, 156)
    >>> from_base64('Erg=')
    (18, 184)
    >>> from_base64('Eg==')
    (18,)
    """
    sequence=""
    for i in b64_string:
        if i !="=":
            sequence+=equivalence[i]
        else:
            sequence=sequence[:-2]
    octet_decimal=conversion_binaire_decimal(sequence)
    n=0
    resultat=0
    code=[]
    while (octet_decimal & (255<<n*8))>0:
        resultat=octet_decimal & (255<<n*8)
        resultat=resultat>>n*8
        code.append(resultat)
        n+=1
    code.reverse()
    code=tuple(code)
    return code

         
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
