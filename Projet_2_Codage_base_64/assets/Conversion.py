sequence_binaire=bin(12)+bin(133)+bin(4)+bin(32)+bin(178)+bin(200)+bin(44)+bin(177)
lettres=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","0","1","2","3","4","5","6","7","8","9","+","/"]
equivalence={}

def conversion_binaire_decimal(mot_binaire):
    valeur=0
    for i in range(len(mot_binaire)):
        mot_binaire_renverse=mot_binaire[::-1]
        if mot_binaire_renverse[i]=="1":
            valeur+=2**i
    return valeur
        
def conversion_decimal_binaire_6bits(dec):
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
#print(equivalence)

def get_in_dictionary(sixtet):
    for cle,valeur in equivalence.items():
        if valeur==sixtet:
            return cle
        
def sequence_binaire(sequence_octets):
    try:
        liste=list(sequence_octets)
        sequence=""
        for i in range(len(liste)):
            sequence+=conversion_decimal_binaire_8bits(int(liste[i]))
        return sequence   
    except TypeError:
        sequence=conversion_decimal_binaire_8bits(sequence_octets)
        return sequence

def to_base64_slice(triplet):
    '''
    convertit le triplet d'octets en une chaîne de quatre symboles
    
    :param triplet: (tuple ou list) une séquence d'octets
    :return: (str) la chaîne de symboles de la base 64 représentant le triplet d'octets
    :CU: 1 <= len(triplet) <= 3 et les entiers de triplet tous compris entre 0 et 255
    :Exemple:
    
    >>> to_base64_slice((18, 184, 156))
    'Eric'
    >>> to_base64_slice((18, 184))
    'Erg='
    >>> to_base64_slice((18,))
    'Eg=='
    '''
    sequence=sequence_binaire(triplet)
    resultat=""
    reste=len(sequence)%6
    if reste>0:
        sequence+="0"*(6-reste)
    nombre_partage=len(sequence)//6
    for i in range(nombre_partage):
        resultat+=str(get_in_dictionary(sequence[6*i:6*(i+1)]))
    if reste>0:
        resultat+="="*int((6-reste)/2)
    return resultat

#print(coder_base64_slice((18,184,156)))
    
def to_base64_binaire(triplet):
    '''
    convertit le triplet d'octets en une chaîne de quatre symboles
    
    :param triplet: (tuple ou list) une séquence d'octets
    :return: (str) la chaîne de symboles de la base 64 représentant le triplet d'octets
    :CU: 1 <= len(triplet) <= 3 et les entiers de triplet tous compris entre 0 et 255
    :Exemple:
    
    >>> to_base64_binaire((18, 184, 156))
    'Eric'
    >>> to_base64_binaire((18, 184))
    'Erg='
    >>> to_base64_binaire((18,))
    'Eg=='
    '''
    sequence=sequence_binaire(triplet)
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
    
    
#print(coder_base64_operation_logique((18,184,156)))    

def decoder_base64_operation_logique(b64_string):
    sequence=""
    for i in b64_string:
        if i !="=":
            sequence+=equivalence[i]
    for i in b64_string:
        if i =="=":
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

print(decoder_base64_operation_logique('Erg='))

#
#def  base64_encode(source):
#    '''
#        Encode a file in base64 and outputs the result on standard output.
#        :param source: (str) the source filename
#        :return: None
#        :side effect: print on the standard output the base64 encoded version of the content 
#                   of source file
#    '''



         
import doctest
doctest.testmod(verbose=False)