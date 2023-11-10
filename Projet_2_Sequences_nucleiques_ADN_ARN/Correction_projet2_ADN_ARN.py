bases=["A", "C", "G", "T"]


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
    return all(caractere in bases for caractere in chaine)


complement_ADN={ 
    'A':'T',
    'T':'A',
    'G':'C',
    'C':'G'  
    }

complement_ARN={
    'A':'U',
    'T':'A',
    'G':'C',
    'C':'G'        
    }



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
    if chaine=='ADN':
        return complement_ADN[base]
    else:
        return complement_ARN[base]
    
def transcrit(sequence,debut,fin):
    """
    Renvoie l'ARN construit à partir de la sous-séquence d'ADN comprise entre les deux positions
    passées en paramètres incluses, attention numérotation à partir de 1
    param : sequence : str
    param : debut : int
    param : fin : int
    return : str
    >>> transcrit('TTCTTCTTCGTACTTTGTGCTGGCCTCCACACGATAATCC',4,23)
    'AAGAAGCAUGAAACACGACC'
    """
    resultat=""
    for caractere in sequence[debut-1:fin]:
        resultat+=baseComplementaire(caractere,'ARN')
    return resultat


code={
'F'   : ('UUU','UUC'),
'L'   : ('UUA','UUG','CUU','CUC','CUA','CUG'),
'I'   : ('AUU','AUC','AUA'),      
'M' : ('AUG'),      
'V' : ('GUU','GUC','GUA','GUG'),      
'S' : ('UCU','UCC','UCA','UCG','AGU','AGC'),        
'P' : ('CCU','CCC','CCA','CCG'),          
'T' : ('ACU','ACC','ACA','ACG'),        
'A' : ('GCU','GCC','GCA','GCG'),   
'Y' : ('UAU','UAC'),   
'*' : ('UAA','UAG','UGA'), #ces codons stop ont pour rôle de signaler la fin du gène lors de la traduction          
'H': ('CAU','CAC'),       
'O' : ('CAA','CAG'),       
'N': ('AAU','AAC'),        
'K':('AAA','AAG'),      
'D' : ('GAU','GAC'),       
'E':('GAA','GAG'),        
'C':('UGU','UGC'),        
'W' :('UGG'),        
'R':('CGU','CGC','CGA','CGG','AGA','AGG'),          
'G':('GGU','GGC','GGA','GGG') 
    }
    


def traduit(sequence):
    """
    Renvoie le code génétique de la séquence ARN
    param : str
    return : str
    >>> traduit('AUGCGAAGCCGAAAGAACACCGGCUAA')
    'MRSRKNTG*'
    """
    resultat=''
    n=len(sequence)//3
    for i in range(n):
        for cle,val in code.items():
            if sequence[3*i:3*i+3] in val:
                resultat+=cle
    return resultat
            

def replique(sequence):
    """
    Renvoie la sequence ADN complémentaire et inversée de la séquence ADN
    param : sequence : str
    return : str
    >>> replique('ACTG')
    'CAGT'
    """
    resultat=''
    for caractere in sequence:
        resultat+=baseComplementaire(caractere,'ADN')
    return resultat[::-1]









if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)