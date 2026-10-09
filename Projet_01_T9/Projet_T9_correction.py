t9 = "22233344455566677778889999"
#     abcdefghijklmnopqrstuvwxyz


### À faire 1

def lettre_chiffre(x):
    """
    Renvoie la touche du clavier T9 correspondant à la lettre x.

    >>> lettre_chiffre("a")
    '2'
    >>> lettre_chiffre("c")
    '2'
    >>> lettre_chiffre("d")
    '3'
    >>> lettre_chiffre("o")
    '6'
    >>> lettre_chiffre("s")
    '7'
    >>> lettre_chiffre("z")
    '9'
    """
    assert "a" <= x <= "z"
    return t9[ord(x)-ord("a")]
    

### À faire 2

def mot_code(mot):
    """
    Renvoie le code T9 correspondant à mot.

    >>> mot_code("bonjour")
    '2665687'
    >>> mot_code("salut")
    '72588'
    >>> mot_code("chat")
    '2428'
    >>> mot_code("python")
    '798466'
    >>> mot_code("oui")
    '684'
    """
    resultat=''
    for lettre in mot:
        resultat+=lettre_chiffre(lettre)
    return resultat
        


dico_test = [
    ("bonjour", 100),
    ("bonsoir", 60),
    ("bon", 40),
    ("comme", 80),
    ("comment", 50),
    ("connu", 20),
    ("chat", 70),
    ("chien", 90)
]


### À faire 3

def prefixes(mot):
    """
    Renvoie la liste des préfixes non vides de mot.

    >>> prefixes("chat")
    ['c', 'ch', 'cha', 'chat']
    >>> prefixes("bon")
    ['b', 'bo', 'bon']
    >>> prefixes("a")
    ['a']
    """
    resultat=[]
    parties=""
    for i in range(len(mot)):
        parties+=mot[i]
        resultat.append(parties)
    return resultat


dico = [
    ("bonjour", 100),
    ("bonsoir", 60),
    ("bon", 40)
]

### À faire 4

def frequences_prefixes(dico):
    """
    Renvoie un dictionnaire associant à chaque préfixe
    le poids total des mots possédant ce préfixe.

    >>> dico = [("bonjour", 100), ("bonsoir", 60), ("bon", 40)]
    >>> freq = frequences_prefixes(dico)
    >>> freq["b"]
    200
    >>> freq["bo"]
    200
    >>> freq["bon"]
    200
    >>> freq["bonj"]
    100
    >>> freq["bons"]
    60
    >>> freq["bonjour"]
    100
    """
    freq = {}
    for element in dico:
        for prefixe in prefixes(element[0]):
            if freq.get(prefixe):
                freq[prefixe]+=element[1]
            else:
                freq[prefixe]=element[1]
    return freq


### À faire 5

def propositions(freq):
    """
    Renvoie un dictionnaire associant à chaque code T9
    le préfixe de poids maximal.

    >>> freq = {"b": 200, "bo": 200, "bon": 200, "con": 20}
    >>> prop = propositions(freq)
    >>> prop["2"]
    'b'
    >>> prop["26"]
    'bo'
    >>> prop["266"]
    'bon'
    """
    prop = {}
    

    for prefixe in freq:
        code = mot_code(prefixe)
        
        if prop.get(code):
            valeur=freq[prefixe]
            if freq[prefixe]>valeur:
                prop[code]=prefixe
        else:
            prop[code]=prefixe

    return prop

### À faire 6

def predictive_text(dico):
    """
    Construit le dictionnaire des prédictions T9.

    >>> dico = [("bonjour", 100), ("bonsoir", 60), ("bon", 40), ("connu", 20)]
    >>> prop = predictive_text(dico)
    >>> prop["2"]
    'b'
    >>> prop["26"]
    'bo'
    >>> prop["266"]
    'bon'
    >>> prop["2665"]
    'bonj'
    >>> prop["26656"]
    'bonjo'
    >>> prop["2665687"]
    'bonjour'
    """
    frequences=frequences_prefixes(dico)
    return propositions(frequences)


### À faire 7


def propose(prop, seq):
    """
    Renvoie la proposition correspondant à seq.
    Renvoie None si aucune proposition n'existe.

    >>> dico = [("bonjour", 100), ("bonsoir", 60), ("bon", 40), ("connu", 20)]
    >>> prop = predictive_text(dico)
    >>> propose(prop, "2")
    'b'
    >>> propose(prop, "26")
    'bo'
    >>> propose(prop, "266")
    'bon'
    >>> propose(prop, "2665")
    'bonj'
    >>> propose(prop, "26656")
    'bonjo'
    >>> propose(prop, "266568")
    'bonjou'
    >>> propose(prop, "2665687")
    'bonjour'
    >>> propose(prop, "999999") is None
    True
    """
    if prop.get(seq):
        return prop[seq]
    else:
        return None

    
dico = [
    ("bonjour", 100),
    ("bonsoir", 60),
    ("bon", 40),
    ("comme", 80),
    ("comment", 50),
    ("connu", 20),
    ("chat", 70),
    ("chien", 90)
]    
    
# >>> prop = predictive_text(dico)
# >>> propose(prop, "2")
# 'b'
# >>> propose(prop, "26")
# 'bo'
# >>> propose(prop, "266")
# 'bon'
# >>> propose(prop, "2665")
# 'bonj'
# >>> propose(prop, "26656")
# 'bonjo'
# >>> propose(prop, "266568")
# 'bonjou'
# >>> propose(prop, "2665687")
# 'bonjour'

### À faire 8

def affiche_saisie(prop, seq):
    """
    Affiche les propositions successives du système T9.

    >>> dico = [("bonjour", 100), ("bonsoir", 60), ("bon", 40), ("connu", 20)]
    >>> prop = predictive_text(dico)
    >>> affiche_saisie(prop, "2665687")
    2 -> b
    26 -> bo
    266 -> bon
    2665 -> bonj
    26656 -> bonjo
    266568 -> bonjou
    2665687 -> bonjour
    """
    recherche=""
    for element in seq:
        recherche+=element
        print(f"{recherche} -> {propose(prop, recherche)}")

if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)