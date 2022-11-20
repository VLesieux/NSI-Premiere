import random
bases=['A','T','G','C']

#####################################Question 1#############################
def estADN(chaine):
    """
    Renvoie True si la chaine contient les bases A, C, G, et T, False sinon, True si vide
    param : chaine : str
    return : bool
    >>> estADN('ATGCGATC')
    True
    >>> estADN('ACKT')
    False
    >>> estADN('')
    True    
    """
    if chaine=='':
        return True
    return all((caractere in bases) for caractere in chaine)

#def genereADN(n):
#    """
#    Génère une séquence aléatoire ADN de taille n
#    param : n : int
#    return : str
#    """
#    sequence=""
#    for i in range(n):
#        sequence+=bases[random.randint(0,3)]
#    return sequence
    
#####################################Question 2#############################

def baseComplementaire(base,chaine):
    """
    Renvoie la base complémentaire dans chaine qui est soit 'ADN', soit 'ARN'
    param : base : str
    param : chaine : str
    return : str
    >>> baseComplementaire('G','ADN')
    'C'
    >>> baseComplementaire('A','ARN')
    'U'
    """
    vers_ARN={"A":"U","T":"A","G":"C","C":"G"}
    vers_ADN={"T":"A","A":"T","C":"G","G":"C"}
    if chaine=='ADN':
        return vers_ADN[base]
    else:
        return vers_ARN[base]
    
#####################################Question 3#############################
    
def transcrit(sequence,debut,fin):
    """
    Renvoie l'ARN construit à partir de la sous-séquence d'ADN comprise entre les deux positions
    passées en paramètres incluses.
    param : sequence : str
    param : debut : int
    param : fin : int
    return : str
    >>> transcrit('TTCTTCTTCGTACTTTGTGCTGGCCTCCACACGATAATCC',4,23)
    'AAGAAGCAUGAAACACGACC'
    """
    partie=sequence[debut-1:fin]
    resultat=''
    for caractere in partie:
        resultat+= baseComplementaire(caractere,'ARN')
    return resultat

#####################################Question 4#############################

def traduit(sequence):
    """
    Renvoie le code génétique de la séquence ARN
    param : str
    return : str
    >>> traduit('AUGCGAAGCCGAAAGAACACCGGCUAA')
    'MRSRKNTG*'
    """
    code={
    'F':('UUU','UUC'),
    'L':('UUA','UUG','CUU','CUC','CUA','CUG'),
    'I':('AUU','AUC','AUA'),
    'M':('AUG'),
    'V':('GUU','GUC','GUA','GUG'),
    'S':('UCU','UCC','UCA','UCG','AGU','AGC'),
    'P':('CCU','CCC','CCA','CCG'),
    'T':('ACU','ACC','ACA','ACG'),
    'A':('GCU','GCC','GCA','GCG'),
    'Y':('UAU','UAC'),
    '*':('UAA','UAG','UGA'),
    'H':('CAU','CAC'),
    'O':('CAA','CAG'),
    'N':('AAU','AAC'),
    'K':('AAA','AAG'),
    'D':('GAU','GAC'),
    'E':('GAA','GAG'),
    'C':('UGU','UGC'),
    'W':('UGG'),
    'R':('CGU','CGC','CGA','CGG','AGA','AGG'),
    'G':('GGU','GGC','GGA','GGG') 
    }
    
    n=len(sequence)//3
    resultat=''
    for i in range(n):
        for cle,val in code.items():
            if sequence[i*3:(i+1)*3] in val:
                resultat+=cle
    return resultat
        
#####################################Question 5#############################

def replique(sequence):
    """
    Renvoie la sequence ADN complémentaire et inversée de la séquence
    param : sequence : str
    return : str
    >>> replique('ACTG')
    'CAGT'
    """
    resultat=''
    for caractere in sequence:
        resultat=baseComplementaire(caractere,'ADN')+resultat
    return resultat

##################################################################
if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)