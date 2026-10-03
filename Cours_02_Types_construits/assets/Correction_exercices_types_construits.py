####################################exercice 1####################
def separe(t):
    """
    Renvoie une liste de nbre pairs et une liste de nbre impaires
    param : t : tuple
    return : tuple
    >>> separe((5,8,2,9,6))
    ([8, 2, 6], [5, 9])
    """
    pairs=[]
    impairs=[]
    for element in t:
        if element%2==0:
            pairs.append(element)
        else:
            impairs.append(element)
    return pairs, impairs

####################################exercice 2####################

def produit(nombres,n):
    """
    Renvoie la liste obtenue en multipliant par n toutes les valeurs de nombres
    param : nombres : list
    param : n: int
    return : list
    >>> produit([3,7,4],2)
    [6, 14, 8]
    """
    return [element*n for element in nombres]



####################################exercice 4####################


def maxi(valeurs):
    """
    Renvoie le maximum d'une liste valeurs
    param : valeurs : tuple
    return : int
    >>> maxi((7,18,9,2))
    18
    """
    return tuple(sorted(valeurs))[-1]


####################################exercice 5####################

positions={}
positions[(48.853585,2.301490)]="Paris"
positions[(11.611358,43.147752)]="Djibouti"
positions[(43.70000,7.250000)]="Nice"

def renvoie_position(position,dictionnaire):
    """
    Renvoie la ville à partir de position avec une précision au dix-millième de degré
    param : position : tuple
    param : dictionnaire : dic
    return : str
    >>> renvoie_position((11.611377,43.147762),positions)
    'Djibouti'
    >>> renvoie_position((11.611368,43.14798),positions)
    'Position inconnue'
    """
    for cle,val in dictionnaire.items():
        if abs(position[0]-cle[0])*10000<1 and abs(position[1]-cle[1])*10000<1:
            return val
    return 'Position inconnue'

####################################exercice 6####################
def stat(texte):
    """
    Renvoie les nombres d'occurence de chaque lettre du texte sous forme de dictionnaire
    param : string
    return : dic
    >>> stat("ceci est un texte")
    {'c': 2, 'e': 4, 'i': 1, 's': 1, 't': 3, 'u': 1, 'n': 1, 'x': 1}
    """
    stat={}
    for caractere in texte:
        if caractere not in (' ',',',':'):
            if stat.get(caractere):
                stat[caractere]+=1
            else:
                stat[caractere]=1
    return stat


dictionnaire_a_f={"yes":"oui","no":"non"}
liste_a_f=[["yes","oui"],["no","non"]]

####################################exercice 7####################

def recherche1(liste_voca,k):
    """
    Renvoie l'élément[1] de liste dont element[0]=k
    param : liste_a_f : list
    param : k : str
    return : str
    recherche1(liste_a_f,"no")
    "non"
    """
    for element in liste_voca:
        if element[0]==k:
            return element[1]

def recherche2(dictionnaire_voca,k):
    """
    Renvoie la clé associée à la valeur k
    param : dictionnaire_voca : dic
    param : k : str
    return : str
    recherche2(dictionnaire_a_f,"no")
    "non"
    recherche2(dictionnaire_a_f,"inconnu")
    """
    for cle,valeur in dictionnaire_voca.items():
        if valeur==k:
            return cle
    return dictionnaire_voca.get(k)

#liste=[[i,i] for i in range(10**6)]
#
#
#from random import shuffle
#
#shuffle(liste)
#
#dico=dict(liste)
#
#from time import time
#
#st=time()
#
#recherche1(liste,13)
#
#print(time()-st)
#
#
#st=time()
#
#recherche2(dico,13)
#
#print(time()-st)

####################################exercice 8####################
valeurs={
1 : ('E','A','I','N','O','R','S','T','U','L'),
2 : ('D','M', 'G'),
3 : ('B','C', 'P'),
4 : ('F','H', 'V'),
8  : ('J','Q'),
10 : ('K','W','X','Y','Z')
}

def points(mot):
    """
    Renvoie la valeur d'un mot dont la sixième lettre compte triple
    param : mot : str
    return : int
    >>> points('CASSER')
    10
    >>> points('RESSAC')
    14
    >>> points('ECRASES')
    13
    """
    resultat=0
    for caractere in mot:
        for cle,valeur in valeurs.items():
            if caractere in valeur:
                if caractere==mot[5]:
                    resultat+=cle*3
                else:
                    resultat+=cle
    return resultat

                

def classement_mots(possibles):
    """
    Renvoie un dictionnaire avec les valeurs des possibles dans l'ordre décroissant
    param : possibles : tuple
    return : int
    >>> classement_mots(("CASSER","RESSAC","ECRASES"))
    {'RESSAC': 14, 'ECRASES': 13, 'CASSER': 10}
    """
    liste=[]
    for mot in possibles:
        liste.append(points(mot))
    liste.sort()
    liste.reverse()
    dictionnaire={}
    for valeur in liste:
        for mot in possibles:
            if points(mot)==valeur:
                dictionnaire[mot]=valeur
    return dictionnaire
        
####################################exercice 9####################

dictionnaire_points={"A": (-2,4), "B": (1,-2), "C": (3,7), "D": (5,-3)}

def distance_entre_deux_points(point1,point2):
    """
    Renvoie la distance entre point1 et point2
    param : point1 : tuple
    param : point2 : tuple
    return : float
    >>> distance_entre_deux_points((1,1),(4,5))
    5.0
    """
    return ((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)**0.5

def calcul_distance_totale(dictionnaire):
    """
    Renvoie la distance totale pour une série de points fournie dans un dictionnaire
    param : dictionnaire : dict
    return : float
    >>> calcul_distance_totale(dictionnaire_points)
    26.125787416977825
    """
    resultat=0
    points=[]
    for cle in dictionnaire.keys():
        points.append(dictionnaire[cle])
    for i in range(len(points)-1):
        resultat+=distance_entre_deux_points(points[i],points[i+1])
    return resultat

####################################exercice 10####################

########question 1################

tailles=['XS', 'S', 'M', 'L', 'XL', 'XXL']
prix=[8+2*i for i in range(len(tailles))]

marchandises={tailles[i]:str(prix[i])+' €' for i in range(len(tailles))}

########question 2################

prix=[0]*len(tailles)
prix[0]=8
for i in range(len(tailles)-1):
    prix[i+1]=round(prix[i]+0.5*prix[i]**0.5,2)

marchandises={tailles[i]:str(prix[i])+' €' for i in range(len(tailles))}

########question 3################

quantites={'XS': 200, 'S': 350 , 'M': 125 , 'L': 370 , 'XL': 50 , 'XXL': 50}

marchandises={tailles[i]:prix[i] for i in range(len(tailles))}
prix_revient_commande=0

for cle in quantites.keys():
    for taille in tailles:
        if taille==cle:
            prix_revient_commande+=quantites[taille]*marchandises[taille]
print(prix_revient_commande)

if __name__ == '__main__':
  import doctest
  doctest.testmod(verbose=True)