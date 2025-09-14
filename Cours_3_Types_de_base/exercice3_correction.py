def conversion_decimal_binaire(n):
    """
    (1) Donne la représentation binaire du nombre entier décimal n
    param : n : int
    return : str
    >>> conversion_decimal_binaire(18)
    '10010'
    >>> conversion_decimal_binaire(141)
    '10001101'
    """
    resultat=""
    while n!=0:#aussi longtemps que le quotient est non nul
        r=n%2#on calcule le reste de la division euclidienne par 2
        n=n//2#le quotient de la division euclidienne par 2 devient le nouveau dividende
        resultat=str(r)+resultat#les restes 0 ou 1 sont accolés à gauche en tant que chaîne de caractères
    return resultat
#     

def conversion_binaire_decimal(mot):
    """
    (2) Donne la valeur décimale d'un mot binaire
    param : n : int
    return : str
    >>> conversion_binaire_decimal('110011')
    51
    >>> conversion_binaire_decimal('1010101')
    85
    """
    resultat=0
    for k in range (len(mot)) :
        resultat+= int(mot[-1-k])*2**k#on multiplie la valeur du bit par la puissance de 2 correspondant à sa position
        #on numérote les indices des caractères de droite à gauche en décroissant à partir de -1
    return resultat


liste_remplaçant=["a","b","c","d","e","f"]
# 
def conversion_decimal_hexadecimal(n):
    """
    (3) Donne la représentation hexadécimale d'un nombre décimal n
    param : n : int
    return : str
    >>> conversion_decimal_hexadecimal(18)
    '12'
    >>> conversion_decimal_hexadecimal(141)
    '8d'
    """
    resultat=""
    while n!=0:#même principe que la conversion en binaire mais cette fois on est en base 16
        r=n%16
        n=n//16
        if r<=9:
            resultat=str(r)+resultat
        else:#il faut remplacer par le caractère équivalent 10->A, 11->B... en cherchant dans la liste_remplaçant
            resultat=liste_remplaçant[r-10]+resultat
    return resultat
# 
# 
def conversion_hexadecimal_decimal(mot):
    """
    (4) Donne la valeur décimale d'un mot hexadécimal
    param : mot : str
    return : int
    >>> conversion_hexadecimal_decimal('ae')
    174
    >>> conversion_hexadecimal_decimal('34a')
    842
    """
    resultat=0
    for k in range (len(mot)):#même principe que la conversion binaire décimal mais en base 16
        if mot[-1-k] not in liste_remplaçant : 
            resultat+= int(mot[-1-k])*16**k
        else:#si on a affaire à une lettre, il faut aller chercher son équivalent dans la liste_remplaçant
            resultat+=(10+liste_remplaçant.index(mot[-1-k]))*16**k
    return resultat

def conversion_binaire_hexadecimal_v1(mot):#la première version consiste à utiliser les deux fonctions précédentes
    #on transforme le binaire en décimal puis on transforme le décimal en hexadécimal
    """
    (5) Donne la représentation hexadécimale d'un mot binaire
    param: str
    return : str
    >>> conversion_binaire_hexadecimal_v1('101101001')
    '169'
    >>> conversion_binaire_hexadecimal_v1('110111')
    '37'
    >>> conversion_binaire_hexadecimal_v1('11111101')
    'fd'
    """
    return conversion_decimal_hexadecimal(conversion_binaire_decimal(mot))

def conversion_binaire_hexadecimal_v2(mot):#cette deuxième version consiste à faire des groupements de 4 bits
    #à chaque groupement on associe un code hexadécimal
    """
    (5) Donne la représentation hexadécimale d'un mot binaire
    param: str
    return : str
    >>> conversion_binaire_hexadecimal_v2('101101001')
    '169'
    >>> conversion_binaire_hexadecimal_v2('110111')
    '37'
    >>> conversion_binaire_hexadecimal_v2('11111101')
    'fd'
    """
    resultat=""
    if len(mot)%4!=0:#il faut éventuellement rajouter des 0 à gauche pour disposer d'un nombre entier de paquets de 4 bits
        mot="0"*(4-len(mot)%4)+mot
    for n in range(len(mot)//4):#la variable n parcourt le nombre de groupes de paquets de 4
        if conversion_binaire_decimal(mot[n*4:n*4+4])>=10:#changer par la lettre si la valeur de la conversion est >=10
            resultat=resultat+liste_remplaçant[conversion_binaire_decimal(mot[n*4:n*4+4])-10]
        else:
            resultat=resultat+str(conversion_binaire_decimal(mot[n*4:n*4+4]))
    return resultat
    
        

def conversion_hexadecimal_binaire(mot):#chaque caractere du code hexadecimal est transformé en un paquet de 4 bits avec ajouts de 0 si nécessaire
    """
    (6) Donne la représentation binaire d'un mot hexadécimal
    param: str
    return : str
    >>> conversion_hexadecimal_binaire('169')
    '000101101001'
    >>> conversion_hexadecimal_binaire('37')
    '00110111'
    >>> conversion_hexadecimal_binaire('fd')
    '11111101'
    """
    resultat=""
    for caractere in mot:
        if caractere not in liste_remplaçant:#il faut alors ajouter des 0 pour faire des paquets de 4 bits si nécessaire (si le code est strictement inférieur à 8)
            resultat=resultat+"0"*(4-len(conversion_decimal_binaire(int(caractere))))+conversion_decimal_binaire(int(caractere))
        else:
            resultat=resultat+conversion_decimal_binaire(int(liste_remplaçant.index(caractere)+10))
    return resultat
#     

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True) 