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
    bases=['A','C','G','T']
    for caractere in chaine:
        if caractere not in bases:
            return False
    return True


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


def baseComplementaire(base,type_molecule):
    """
    Renvoie la base complémentaire dans chaine qui est soit 'ADN', soit 'ARN'
    param : base : str
    param : type_molecule : str
    return : str
    >>> baseComplementaire('G','ADN')
    'C'
    >>> baseComplementaire('A','ARN')
    'U'
    """
    if type_molecule=='ADN':
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
    extrait=sequence[debut-1:fin]
    resultat=''
    for caractere in extrait:
        resultat+=baseComplementaire(caractere,'ARN')
    return resultat

codes={
('UUU','UUC') : 'F', 
('UUA','UUG','CUU','CUC','CUA','CUG') : 'L',    
('AUU','AUC','AUA') : 'I',     
('AUG') : 'M',     
('GUU','GUC','GUA','GUG') : 'V',     
('UCU','UCC','UCA','UCG','AGU','AGC') : 'S',        
('CCU','CCC','CCA','CCG') : 'P',           
('ACU','ACC','ACA','ACG') : 'T',       
('GCU','GCC','GCA','GCG') : 'A',       
('UAU','UAC') : 'Y',      
('UAA','UAG','UGA') : '*',#ces codons stop ont pour rôle de signaler la fin du gène lors de la traduction          
('CAU','CAC') : 'H',      
('CAA','CAG') : 'O',      
('AAU','AAC') : 'N',          
('AAA','AAG') : 'K',      
('GAU','GAC') : 'D',       
('GAA','GAG') : 'E',        
('UGU','UGC') : 'C',       
('UGG') : 'W',        
('CGU','CGC','CGA','CGG','AGA','AGG') : 'R',         
('GGU','GGC','GGA','GGG') : 'G'
}
    
def traduit(sequence):
    """
    Renvoie le code génétique de la séquence ARN
    param : str
    return : str
    >>> traduit('AUGCGAAGCCGAAAGAACACCGGCUAA')
    'MRSRKNTG*'
    """
    resultat=""
    multiple=len(sequence)//3
    for i in  range(multiple):
        morceau=sequence[i*3:i*3+3]
        for cle,valeur in codes.items():
            if morceau in cle:
                resultat+=valeur
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


def sont_complementaires(brin1, brin2):
    """
    Vérifie si deux séquences ADN sont complémentaires et antiparallèles.

    Deux brins sont complémentaires si :
    - chaque base de l'un correspond à la base complémentaire de l'autre
      (A<->T et C<->G),
    - et s'ils sont orientés en sens opposé (antiparallèles).

    param : brin1 : str
    param : brin2 : str
    return : bool

    >>> sont_complementaires("ATGC", "GCAT")
    True
    >>> sont_complementaires("ATGC", "TACG")  # pas antiparallèles
    False
    """

    # Comparaison stricte avec le brin fourni
    return brin2 == replique(brin1)








if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)