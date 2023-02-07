def create (x, y, s):#crée un dictionnaire à partir d'un triplet
    """
    Renvoie un dictionnaire à partir d'un triplet
    :param x : float désigne la longueur du pétale
    :param y : float désigne la largeur du pétale
    :param s : str '0','1' ou '2' en fonction de l'espèce de l'iris
    :return: dict
    :Exemple:
    >>> create(1.5,2.4,'1')
    {'x': 1.5, 'y': 2.4, 's': '1'}
    """
    return {'x': x, 'y': y, 's': s}


def lecture_tableau(text):
    f=open(text,"r")
    champs=f.readline()# on lit la première ligne des entêtes
    lignes=f.readlines()# on lit ensuite les autres lignes
    donnees = dict([])#initialise un dictionnaire
    numero=0
    for ligne in lignes:#lecture du fichier
        donnees[numero]=create(ligne.rstrip('\n').split(";")[0], ligne.rstrip('\n').split(";")[1], ligne.rstrip('\n').split(";")[2])
        numero+=1
    return donnees#le dictionnaire associe un dictionnaire {x,y,s} à une clef qui est un numero

donnees=lecture_tableau('iris.csv')



def extraction(dic,grandeur,espece):
    """
    Renvoie une liste de données correspondant à la grandeur, longueur ou largeur, pour une espèce
    :param dic : dict
    :param grandeur : str
    :param espece : int 0, 1, 2 en fonction de l'espèce de l'iris
    :return: list
    :Exemple:
    >>> extraction({0: {'x': '1.4', 'y': '0.2', 's': '0'}, 1: {'x': '1.4', 'y': '0.8', 's': '0'}},'y',0)
    [0.2, 0.8]
    """
    liste=[]
    for i in range(len(dic)):
        if float(dic[i]['s'])==espece:
            liste.append(float(dic[i][grandeur]))
    return liste#renvoie les valeurs prises par la grandeur sous forme de liste


def distance(p,q):
    """
    Renvoie un doublet distance, label ; la distance est la distance euclidienne entre deux points du plan
    :param p : tuple du point demandé
    :param q : dictionnaire contenant toutes les données {'x': , 'y': , 's': }
    :return: tuple 
    :Exemple:
    >>> distance((0,0),{'x': '4', 'y': '3', 's': '0'})
    (5.0, '0')
    """
    distance=((float(q['x'])-p[0])**2+(float(q['y'])-p[1])**2)**0.5
    return (distance,q['s'])

def space(x):
    """
    permet de renvoyer la première valeur d'un doublet
    cette fonction sera utilisée pour ordonner une liste de doublet dans l'ordre croissant ou décroissant de la première valeur
    :param x : un doublet
    :return: float 
    :Exemple:
    >>> space((2.4,3.9))
    2.4
    >>> sorted([(2.2, 3.4),(1.2, 4.5)],key=space)
    [(1.2, 4.5), (2.2, 3.4)]
    >>> sorted([(2.2, 3.4),(1.2, 4.5)],key=space,reverse=True)
    [(2.2, 3.4), (1.2, 4.5)]
    """
    return x[0]

def amount(x):
    """
    permet de renvoyer la deuxième valeur d'un doublet
    cette fonction sera utilisée pour ordonner une liste de doublet dans l'ordre croissant ou décroissant de la deuxième valeur
    :param x : un doublet
    :return: float 
    :Exemple:
    >>> amount((2.4,3.9))
    3.9
    >>> sorted([(2.2, 3.4),(1.2, 4.5)],key=amount)
    [(2.2, 3.4), (1.2, 4.5)]
    >>> sorted([(2.2, 3.4),(1.2, 4.5)],key=amount,reverse=True)
    [(1.2, 4.5), (2.2, 3.4)]
    """    
    return x[1]

def caractere_le_plus_commun(liste):
    """
    Renvoie l'espèce la plus commune dans une liste de doublets (distance,espèce)
    :param liste : list
    :return: str 
    :Exemple:
    >>> caractere_le_plus_commun([(2,'0'),(1,'0'),(3,'1')])
    '0'
    >>> caractere_le_plus_commun([(2,'1'),(1,'2'),(3,'1')])
    '1'
    """
    liste_des_comptes=[len([element for element in liste if element[1]==str(i)]) for i in range(3)]
    return str(liste_des_comptes.index(max(liste_des_comptes)))
           
        
        
def proches_voisins(k,p,liste):
    """
    Renvoie la liste des k plus proches voisins
    :param p : le doublet des coordonnées du point considéré
    :param k : le nombre de voisins considérés
    :return: liste 
    :Exemple:
    >>> proches_voisins(3,(0,0),donnees)
    [(1.019803902718557, '0'), (1.104536101718726, '0'), (1.2165525060596438, '0')]
    """
    distances=[distance(p,liste[i]) for i in range(len(liste))]
    distances=sorted(distances,key=space)
    resultat=[distances[i] for i in range(k)]
    return resultat
    


import matplotlib.pyplot as plt#importe le module pour la représentation des graphes

longueur=float(input("longueur du pétale : "))
largeur=float(input("largeur du pétale : "))
k=int(input("valeur de k : "))
       
prediction=caractere_le_plus_commun(proches_voisins(k,(longueur,largeur),donnees))

especes=['setosa','virginica','versicolor']
couleurs=['g','r','b']

for i in range(len(especes)):
    x=extraction(lecture_tableau('iris.csv'),'x',i)#liste des x
    y=extraction(lecture_tableau('iris.csv'),'y',i)#liste des y
    plt.scatter(x[0], y[0], color=couleurs[i], label=especes[i])
    for j in range(1,len(x)):
        plt.scatter(x[j], y[j], color=couleurs[i])

plt.scatter(longueur, largeur,color='k')
plt.legend()

txt="Résultat : "
if prediction=='0':
    txt=txt+"setosa"
if prediction=='1':
    txt=txt+"virginica"
if prediction=='2':
    txt=txt+"versicolor"

plt.text(3,0.5, f"longueur : {longueur} cm largeur : {largeur} cm", fontsize=12)
plt.text(3,0.3, f"k : {k}", fontsize=12)
plt.text(3,0.1, txt,fontsize=12)


plt.show()

if __name__ == '__main__':
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)